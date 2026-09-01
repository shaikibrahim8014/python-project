import tkinter as tk
from tkinter import messagebox
import sqlite3


# ---------------- DATABASE ----------------

def create_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Create default user
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", "1234")
        )
    except sqlite3.IntegrityError:
        pass

    connection.commit()
    connection.close()


# ---------------- LOGIN ----------------

def login():
    username = username_entry.get()
    password = password_entry.get()

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()

    connection.close()

    if user:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror(
            "Login",
            "Invalid username or password"
        )


# Create database
create_database()


# ---------------- GUI ----------------

window = tk.Tk()
window.title("Login Form")
window.geometry("350x250")

title = tk.Label(
    window,
    text="Login Form",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)


# Username
username_label = tk.Label(window, text="Username")
username_label.pack()

username_entry = tk.Entry(window, width=30)
username_entry.pack(pady=5)


# Password
password_label = tk.Label(window, text="Password")
password_label.pack()

password_entry = tk.Entry(
    window,
    width=30,
    show="*"
)
password_entry.pack(pady=5)


# Login button
login_button = tk.Button(
    window,
    text="Login",
    width=15,
    command=login
)
login_button.pack(pady=20)


window.mainloop()