import tkinter as tk
from tkinter import messagebox


def register():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    password = password_entry.get()
    confirm_password = confirm_entry.get()

    # Check empty fields
    if (
        not name
        or not email
        or not phone
        or not gender
        or not password
        or not confirm_password
    ):
        messagebox.showerror("Error", "Please fill all fields")
        return

    # Check password
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Registration successful
    messagebox.showinfo("Success", f"Registration Successful!\n\nWelcome {name}")

    # Clear form
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)
    gender_var.set("Select")


# Create window
window = tk.Tk()
window.title("Registration Form")
window.geometry("450x550")
window.resizable(False, False)


# Title
title = tk.Label(window, text="Registration Form", font=("Arial", 24, "bold"))
title.pack(pady=20)


# Name
tk.Label(window, text="Full Name", font=("Arial", 12)).pack()

name_entry = tk.Entry(window, width=35, font=("Arial", 12))
name_entry.pack(pady=5)


# Email
tk.Label(window, text="Email", font=("Arial", 12)).pack()

email_entry = tk.Entry(window, width=35, font=("Arial", 12))
email_entry.pack(pady=5)


# Phone
tk.Label(window, text="Phone Number", font=("Arial", 12)).pack()

phone_entry = tk.Entry(window, width=35, font=("Arial", 12))
phone_entry.pack(pady=5)


# Gender
tk.Label(window, text="Gender", font=("Arial", 12)).pack()

gender_var = tk.StringVar()
gender_var.set("Select")

gender_menu = tk.OptionMenu(window, gender_var, "Male", "Female", "Other")
gender_menu.config(width=29)
gender_menu.pack(pady=5)


# Password
tk.Label(window, text="Password", font=("Arial", 12)).pack()

password_entry = tk.Entry(window, width=35, font=("Arial", 12), show="*")
password_entry.pack(pady=5)


# Confirm Password
tk.Label(window, text="Confirm Password", font=("Arial", 12)).pack()

confirm_entry = tk.Entry(window, width=35, font=("Arial", 12), show="*")
confirm_entry.pack(pady=5)


# Register Button
register_button = tk.Button(
    window, text="Register", font=("Arial", 12, "bold"), width=20, command=register
)
register_button.pack(pady=20)


# Start application
window.mainloop()
