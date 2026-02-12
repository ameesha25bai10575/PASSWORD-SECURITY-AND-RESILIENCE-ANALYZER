document.addEventListener("DOMContentLoaded", function () {

    const passwordInput = document.getElementById("passwordInput");
    const generateBtn = document.getElementById("generatePassword");
    const toggleBtn = document.getElementById("togglePassword");

    const entropySpan = document.getElementById("entropy");
    const crackTimeSpan = document.getElementById("crackTime");
    const criteriaList = document.getElementById("criteriaList");

    const strengthFill = document.getElementById("strengthFill");
    const strengthText = document.getElementById("strengthText");

    // Generate Password
    generateBtn.addEventListener("click", function () {
        fetch("/generate")
            .then(res => res.json())
            .then(data => {
                passwordInput.value = data.password;
                analyzePassword(data.password);
            });
    });

    // Toggle visibility
    toggleBtn.addEventListener("click", function () {
        passwordInput.type = passwordInput.type === "password" ? "text" : "password";
    });

    // Analyze while typing
    passwordInput.addEventListener("input", function () {
        analyzePassword(passwordInput.value);
    });

    function analyzePassword(password) {

        if (!password) {
            strengthFill.style.width = "0%";
            strengthText.textContent = "Strength: -";
            return;
        }

        fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ password: password })
        })
        .then(res => res.json())
        .then(data => {

            entropySpan.textContent = data.entropy;
            crackTimeSpan.textContent = data.crack_time;

            // Strength Bar
            let score = data.score;
            strengthFill.style.width = score + "%";

            if (score < 40) {
                strengthFill.style.backgroundColor = "#ff4c4c";
                strengthText.textContent = "Strength: Weak";
            } 
            else if (score < 70) {
                strengthFill.style.backgroundColor = "#ffa500";
                strengthText.textContent = "Strength: Medium";
            } 
            else {
                strengthFill.style.backgroundColor = "#00ff88";
                strengthText.textContent = "Strength: Strong";
            }

            // Criteria
            criteriaList.innerHTML = "";

            for (let key in data.criteria) {
                let li = document.createElement("li");
                li.textContent = key + " : " + (data.criteria[key] ? "✔" : "❌");
                li.className = data.criteria[key] ? "valid" : "invalid";
                criteriaList.appendChild(li);
            }
        });
    }

});
