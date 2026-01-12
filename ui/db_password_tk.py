from tkinter import *
from tkinter import ttk, messagebox
import auth

def ask_db_password(parent):
    popup = Toplevel(parent)
    popup.title("Database Password Required")
    popup.geometry("400x200")
    popup.grab_set()
    popup.resizable(False, False)

    Label(
        popup,
        text="Enter MySQL root password",
        font=("Arial", 14)
    ).pack(pady=20)

    pwd_entry = Entry(popup, show="*", font=("Arial", 14))
    pwd_entry.pack(pady=10)
    pwd_entry.focus()

    def submit():
        pwd = pwd_entry.get().strip()
        if not pwd:
            messagebox.showerror("Error", "Password cannot be empty")
            return
        auth.get_password(pwd)
        popup.destroy()

    ttk.Button(popup, text="Save", command=submit).pack(pady=15)

    popup.wait_window()
