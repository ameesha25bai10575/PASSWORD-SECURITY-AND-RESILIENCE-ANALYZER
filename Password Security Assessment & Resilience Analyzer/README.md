PASSWORD SECURITY AND RESILIENCE ANALYZER BY DIGITAL VAULT

Project Overview
PASSWORD SECURITY AND RESILIENCE ANALYZER BY DIGITAL VAULTis a cybersecurity dashboard that
helps users evaluate the strength of their passwords in real time.

It provides: - Password strength score - Entropy calculation - Crack
time estimation (Online, Offline, GPU) - Security criteria checklist -
Strong password generator


 Features

1 Real-time password strength analysis
2 Entropy-based security calculation
3 Crack time visualization
4 Criteria validation (length, uppercase, digits, symbols, etc.)
5 Secure random password generator
6 Professional cybersecurity dashboard UI


 Technologies Used

Frontend: - HTML - CSS - JavaScript

Backend: - Python - Flask

Data Communication: - JSON


 Project Structure

PASSWORD SECURITY AND RESILIENCE ANALYZER BY DIGITAL VAULT/ │ ├── app.py ├── templates/ │ └── index.html ├──
static/ │ ├── style.css │ └── script.js ├── requirements.txt └──
README.txt

How to Run the Project

1.  Install Python (3.8+ recommended)

2.  Install dependencies:

    pip install -r requirements.txt

3.  Run the Flask application:

    python app.py

4.  Open browser and go to:

    http://127.0.0.1:5000/



 How It Works

1.  User enters a password
2.  JavaScript captures input using DOM manipulation
3.  Password is sent to Flask backend via POST request
4.  Backend calculates:
    -   Entropy
    -   Crack time
    -   Security criteria
5.  Results are returned in JSON format
6.  UI updates dynamically with strength bar and metrics



 Security Concepts Used

-   Entropy calculation
-   Brute-force attack modeling
-   Character pool analysis
-   Real-time UI feedback

This project helps users understand
- Why weak passwords are dangerous
- How entropy affects security
- Best practices for password creation


Future Improvements

-   Cloud deployment (Render/Heroku)
-   User authentication module
-   Database integration
-   Advanced AI-based password scoring
-   Admin dashboard


Developed By

Ameesha Kumari 
By Digital Vault team

