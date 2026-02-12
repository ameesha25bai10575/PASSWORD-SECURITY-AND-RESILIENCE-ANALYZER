from flask import Flask, render_template, request, jsonify
import math
import string
import secrets

app = Flask(__name__)

# -----------------------------
# Password Generator
# -----------------------------

def generate_password(length=14, exclude_ambiguous=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if exclude_ambiguous:
        ambiguous = "O0l1"
        lowercase = ''.join(c for c in lowercase if c not in ambiguous)
        uppercase = ''.join(c for c in uppercase if c not in ambiguous)
        digits = ''.join(c for c in digits if c not in ambiguous)

    all_chars = lowercase + uppercase + digits + symbols

    # Ensure at least one of each type
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    # Fill remaining length
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


# -----------------------------
# Entropy Calculation
# -----------------------------
def calculate_entropy(password):
    pool = 0

    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)


# -----------------------------
# Crack Time Estimation
# -----------------------------
def crack_time(entropy):
    guesses_per_sec = 1_000_000_000
    seconds = (2 ** entropy) / guesses_per_sec

    if seconds < 60:
        return f"{round(seconds,2)} seconds"
    elif seconds < 3600:
        return f"{round(seconds/60,2)} minutes"
    elif seconds < 86400:
        return f"{round(seconds/3600,2)} hours"
    elif seconds < 31536000:
        return f"{round(seconds/86400,2)} days"
    else:
        return f"{round(seconds/31536000,2)} years"


# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate")
def generate():
    password = generate_password()
    return jsonify({"password": password})


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    password = data.get("password", "")

    entropy = calculate_entropy(password)
    time = crack_time(entropy)

    criteria = {
        "Minimum 8 characters": len(password) >= 8,
        "Minimum 12 characters": len(password) >= 12,
        "Contains lowercase": any(c.islower() for c in password),
        "Contains uppercase": any(c.isupper() for c in password),
        "Contains digit": any(c.isdigit() for c in password),
        "Contains special character": any(c in string.punctuation for c in password),
    }

    if entropy < 40:
        strength = "Weak"
    elif entropy < 60:
        strength = "Moderate"
    elif entropy < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"
  
    score = min(100, int((entropy / 100) * 100))


    return jsonify({
        "entropy": entropy,
        "crack_time": time,
        "criteria": criteria,
        "score": score,
        "strength": strength
    })


if __name__ == "__main__":
    app.run(debug=True)
