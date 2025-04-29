# 🛡️ Registration and Login System (Python + MySQL)

This is a simple command-line-based Registration and Login system built with **Python** and **MySQL**. It allows users to register with validation and login securely with stored credentials.

---

## 📌 Features

- Register a new user with:
  - Unique username and email
  - Strong password validation (length, uppercase, lowercase, digit, special character)
- Secure password confirmation
- User login with validation
- Data storage in a MySQL database
- Print all users (for admin/debug use)

---

## 🛠️ Tech Stack

- **Backend:** Python
- **Database:** MySQL (via `pymysql`)

---

## 🗃️ Database Schema

**Database Name:** `register_db`  
**Table Name:** `user`

```sql
CREATE TABLE user (
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    user_name VARCHAR(200),
    email VARCHAR(200),
    password1 VARCHAR(200),
    password2 VARCHAR(200)
);
