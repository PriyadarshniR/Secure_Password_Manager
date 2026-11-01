# 🔐 Secure Password Manager

## 📌 Project Overview

Secure Password Manager is a Python-based application designed to generate strong passwords, evaluate password strength, calculate password entropy, and securely store passwords using encryption.

The application helps users create stronger passwords and protect their stored credentials using a master password.

## ✨ Features

- **Random Password Generation:** Generates passwords using uppercase letters, lowercase letters, numbers, and special characters.
- **Smart Password Generation:** Creates readable passwords by combining letters, numbers, and symbols.
- **Password Strength Checker:** Evaluates passwords and classifies them as Weak, Medium, or Strong.
- **Password Entropy Calculation:** Calculates password entropy in bits to estimate password complexity.
- **SHA-256 Hashing:** Generates SHA-256 hashes of passwords.
- **Encrypted Password Storage:** Uses Fernet symmetric encryption to protect stored credentials.
- **Master Password Protection:** Uses a master password to derive the encryption key.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Cryptography | Fernet encryption |
| Hashlib | SHA-256 hashing |
| Base64 | Encryption key encoding |
| Random | Password generation |
| String | Character sets for password generation |
| Math | Entropy calculation |
| Regex | Password strength validation |

## 📥 Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/PriyadarshniR/Secure_Password_Manager.git
```

**Step 2: Navigate to the project directory**

```bash
cd Secure_Password_Manager
```

**Step 3: Install the required dependency**

```bash
pip install cryptography
```

## ▶️ How to Run the Project

Run the following command:

```bash
python main.py
```

The application displays a menu with the following options:

1. Generate Password
2. Save Password
3. Smart Readable Password
4. View Saved Passwords
5. Exit

Follow the menu instructions to generate passwords, check their strength, calculate entropy, and save credentials.

## 🔒 Security

- Password entries are encrypted using Fernet symmetric encryption.
- The master password is used to derive the encryption key.
- SHA-256 is used to generate password hashes.

**Note:** This is an educational project. The current implementation uses Python's `random` module for password generation and a directly derived encryption key. It should not be used to protect real-world credentials without further security improvements.

## 👩‍💻 Author

**Priyadarshni R**

GitHub: [PriyadarshniR](https://github.com/PriyadarshniR)
