from tkinter import *
from tkinter import ttk, messagebox
import os
from db import create_db
from ui.db_password_tk import ask_db_password
from ui.Admin_tk import Admin
from ui.Student_tk import Student

def start_app():
    window = Tk()
    window.withdraw()
    if not os.path.exists("db_pass.txt"):
        ask_db_password(window)
        
    try:
        create_db()
    except Exception as e:
        messagebox.showerror(
            "Database Error",
            "Failed to connect to database.\n"
            "Check password and restart the app."
        )
        window.destroy()
        return
    window.deiconify()
# theme
    window.tk.call("source", os.path.dirname(os.path.abspath(__file__))+r"\Azure\Zure.tcl")
    window.tk.call("set_theme", "dark")

# Window
    window.geometry("900x900")
    window.title("Library Management")

# Icon
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ASSETS = os.path.join(BASE_DIR, "assets")
    Labelimg = PhotoImage(
    file=os.path.join(ASSETS, "library__1_-removebg-preview.png"))
    Admimg = PhotoImage(file=os.path.join(ASSETS, "Admin.png"))
    Stdimg = PhotoImage(file=os.path.join(ASSETS, "Student.png"))

    icon = os.path.join(ASSETS, "library.ico")
    window.config(background="#51504f")
    window.wm_iconbitmap(icon)

# Header
    label = Label(
    text=" Library Management System",
    font=("Arial", 40, "bold"),
    fg="White",
    bg="#51504f",
    image=Labelimg,
    compound="left"
)
    label.pack(pady=40)

# Frame for buttons (auto centers)
    button_frame = Frame(window, bg="#51504f")
    button_frame.pack(expand=True)  # centers vertically & horizontally

#Styles
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 20, "bold"))

#Buttons
    def Exi():
        window.destroy()
# Admin Button
    button1 = ttk.Button(
    button_frame,
    text="Admin",
    image=Admimg,
    compound=LEFT,
    style="TButton",
    command=Admin
)
    button1.pack(pady = 20)

# Student Button
    button2 = ttk.Button(
    button_frame,
    text="Student",
    image=Stdimg,
    compound=LEFT,
    style="TButton",
    command=Student
)
    button2.pack(pady=20)

    button3 = ttk.Button(
    button_frame,
    text="Exit",
    style="TButton",
    command=Exi
)
    button3.pack(pady=20)


    window.mainloop()

