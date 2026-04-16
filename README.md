# Bank-account-management-system

📌 Project Overview

This project is a simple Bank Account Management System built using Object-Oriented Programming (OOP) in Python.

It simulates real banking operations such as:

Deposit
Withdraw
Transfer
Interest rewards
Savings account with withdrawal fees

🚀 Features
Create bank accounts
Deposit money
Withdraw money with balance validation
Transfer money between accounts
Custom exception handling (BalanceException)
Interest reward system (5% bonus on deposit)
Savings account with transaction fee


🧠 OOP Concepts Used
Classes and Objects
Inheritance
Method Overriding
Custom Exceptions
Encapsulation


📂 Project Structure
bank-account-oop/
│
├── oop_project.py        # Main program execution
├── bank.py        # All classes (BankAccount, SavingAcct, etc.)
└── README.md      # Documentation


🧾 Classes Description
🔹 BankAccount
Handles basic operations:
Deposit
Withdraw
Transfer
Balance check
🔹 InterestRewardAcct
Inherits from BankAccount
Adds 5% bonus on every deposit
🔹 SavingAcct
Inherits from InterestRewardAcct
Adds withdrawal fee (₹5)


⚙️ How It Works
Create accounts
Perform transactions:
Deposit money
Withdraw money
Transfer money
System checks balance before transactions
Displays updated balance


▶️ How to Run
Install Python
Download or clone this repository
Run:
python oop_project.py
💻
