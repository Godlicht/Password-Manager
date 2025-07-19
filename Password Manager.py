import tkinter as tk
from tkinter import messagebox, ttk
import string
import secrets
import json
import os
import webbrowser

# WINDOW
window = tk.Tk()
window.title("Password Manager")
window.geometry("1200x720")
window.configure()

# TABS
notebook = ttk.Notebook(window)
notebook.pack(fill='both')
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Main")
notebook.add(tab2, text="Your passwords")

# TAB WITH PASSWORDS
table = ttk.Treeview(tab2)
table["columns"] = ("Address", "Username", "Password")

table.heading("Address", text="Address")
table.column("Address", anchor="w", width=200)

table.heading("Username", text="Username")
table.column("Username", anchor="w", width=200)

table.heading("Password", text="Password")
table.column("Password", anchor="w", width=200)

table.column("#0", width=0, stretch=tk.NO)

table.pack(fill='both', expand=True, padx=10, pady=10)

# SAVE DATA BUTTON
def save_button():
    address = address_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if address and username and password:
        table.insert('', 'end', values=(address, username, password))

        entry = {
            "address": address,
            "username": username,
            "password": password
        }

        data = []
        if os.path.exists("passwords.json"):
            with open("passwords.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []

        data.append(entry)

        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo("Success", "Your data has been saved")

        address_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Error", "Please fill all fields")
# DATA STORAGE
def load_data():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            try:
                data = json.load(file)
                for entry in data:
                    table.insert('', 'end', values=(
                        entry["address"], entry["username"], entry["password"]
                    ))
            except json.JSONDecodeError:
                pass

table.pack(fill='both', expand=True)
load_data()
# REDIRECT AND COPY TO CLIPBOARD
def on_table_click(event):
    item_id = table.identify_row(event.y)
    column = table.identify_column(event.x)

    if item_id:
        values = table.item(item_id, 'values')
        if not values:
            return

        col_index = int(column.replace('#', '')) - 1

        if col_index == 0:  # Address
            address = values[0]
            if not address.startswith("https://"):
                address = "https://" + address
            webbrowser.open(address)

        elif col_index == 1:  # Username
            username = values[1]
            window.clipboard_clear()
            window.clipboard_append(username)
            messagebox.showinfo("Copied", "Username copied to clipboard")

        elif col_index == 2:  # Password
            password = values[2]
            window.clipboard_clear()
            window.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard")

table.bind("<ButtonRelease-1>", on_table_click)

# GENERATE PASSWORD
def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(22))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# LABELS AND ENTRIES
address_label = tk.Label(tab1, text="Address:", font=("Arial", 12))
address_label.pack(pady=(20, 5))

address_entry = tk.Entry(tab1, width=40, font=("Arial", 12))
address_entry.pack(pady=5)

username_label = tk.Label(tab1, text="Username:", font=("Arial", 12))
username_label.pack(pady=5)

username_entry = tk.Entry(tab1, width=40, font=("Arial", 12))
username_entry.pack(pady=5)

password_label = tk.Label(tab1, text="Password:", font=("Arial", 12))
password_label.pack(pady=5)

password_entry = tk.Entry(tab1, width=40, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

# BUTTONS
generate_button = tk.Button(
    tab1,
    text="Generate password",
    command=generate_password,
    pady=10,
    width=20,
    bg="#add8e6",
    font=("Arial", 11, "bold")
)
generate_button.pack(pady=(20, 10))

save_button = tk.Button(
    tab1,
    text="Save password",
    command=save_button,
    pady=10,
    width=20,
    bg="#90ee90",
    font=("Arial", 11, "bold")
)
save_button.pack(pady=(0, 30))

window.mainloop()
