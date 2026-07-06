# 🔐 Password Strength Analyzer

A Python-based Password Strength Analyzer that evaluates password security using multiple cybersecurity principles instead of simple length checks.

This project was built as part of the **CyberSpec** learning roadmap to understand how modern systems evaluate passwords and defend against password attacks.

---

# Features

- ✅ Password length analysis
- ✅ Uppercase detection
- ✅ Lowercase detection
- ✅ Number detection
- ✅ Symbol detection
- ✅ Password strength scoring
- ✅ Password entropy calculation
- ✅ Estimated brute-force crack time
- ✅ Common password detection
- ✅ Actionable security recommendations
- ✅ Professional command-line interface (CLI)

---

# Cybersecurity Concepts Covered

This project demonstrates the following concepts:

- Authentication
- Authorization
- Password Policies
- Search Space
- Password Entropy
- Brute Force Attacks
- Dictionary Attacks
- Offline vs Online Password Cracking
- Password Hashing
- Password Salting

---

# Project Structure

```
Password-Strength-Analyzer/

├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   └── utils.py
│
├── tests/
│   └── test_analyzer.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# Example Output

```
Password Analysis Report

Length:                12
Uppercase:             ✔ Yes
Lowercase:             ✔ Yes
Numbers:               ✔ Yes
Symbols:               ✔ Yes

Strength:              Strong
Entropy:               78.66 bits
Entropy Rating:        Good
Estimated Crack Time:  Millions of years

Suggestions

• No suggestions. Your password meets the current policy.
```

---

# What I Learned

While building this project I learned:

- Why long passwords are stronger than short complex passwords
- How entropy estimates password unpredictability
- Why attackers prefer dictionary attacks before brute force
- Why passwords should never be stored in plaintext
- How hashing and salting protect stored passwords
- Why password policies exist
- How password strength analyzers work internally

---

# Future Improvements

- Detect keyboard patterns (qwerty, asdf)
- Detect repeated characters
- Detect sequential characters
- Detect personal information inside passwords
- Check against leaked password databases
- Build a graphical user interface
- Export password reports
- Improve entropy estimation using advanced algorithms

---

# Technologies Used

- Python 3
- Git
- GitHub

---

# License

This project is part of my CyberSpec cybersecurity learning roadmap.