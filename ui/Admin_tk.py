from tkinter import *
import os
from tkinter import ttk, messagebox
import admin as ad

# --- Admin credentials ---
ADMIN_ID = "admin123"
ADMIN_PASS = "password123"

def Admin():
    root = Toplevel()
    root.title("Admin Login")
    root.geometry("500x500")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ASSETS = os.path.join(BASE_DIR, "assets")
    root.wm_iconbitmap( os.path.join(ASSETS, "Admin.ico"))
    root.config(bg="#333333")

    Admimg = PhotoImage(file=os.path.join(ASSETS, "Admin.png"))
    root.Admimg = Admimg   # type: ignore

    Label(
        root,
        text=" Admin Panel Login",
        font=("Arial", 28, "bold"),
        fg="white",
        bg="#333333",
        image=Admimg,
        compound="left"
    ).pack(pady=30)



    Label(root, text="Admin ID:", bg="#333333", fg="white", font=("Arial", 16)).pack(pady=5)

    id_entry = Entry(root, font = ("Arial", 16), show="*")

    id_entry.pack(pady=0)





    Label(root, text="Password:", bg="#333333", fg="white", font=("Arial", 16)).pack(pady=5)

    pass_entry = Entry(root, font=("Arial", 16), show="*")

    pass_entry.pack(pady=0)


    def check_login():
        entered_id = id_entry.get().strip()
        entered_pass = pass_entry.get().strip()

        if entered_id == ADMIN_ID and entered_pass == ADMIN_PASS:
            messagebox.showinfo("Access Granted", "Welcome, Admin!")
            root.destroy() 
            open_admin_panel()
        else:
            messagebox.showerror("Access Denied", "Invalid ID or Password")
            root.destroy()

    # --- Login button ---
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 16, "bold"))
    ttk.Button(root, text="Login", style="TButton", command=check_login).pack(pady=20)


def open_admin_panel():
    panel = Toplevel()
    panel.title("Admin Panel")
    panel.geometry("900x900")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ASSETS = os.path.join(BASE_DIR, "assets")
    panel.wm_iconbitmap(os.path.join(ASSETS, "Admin.ico"))
    panel.config(bg="#51504f")

    Label(
        panel,
        text="Welcome to Admin Panel",
        font=("Arial", 30, "bold"),
        fg="white",
        bg="#51504f"
    ).pack(pady=50)
    
    def view_students_window():
        win = Toplevel()
        win.title("Student Records")
        win.geometry("900x400")

        cols = ("e_id", "id", "name", "mname", "surname", "class", "sec", "roll")

        tree = ttk.Treeview(win, columns=cols, show="headings")
        tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

        for col in cols:
            tree.heading(col, text=col, anchor="center")
            tree.column(col, width=100, anchor="center")

        try:
            rows = ad.show_database()
            for row in rows:
                tree.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", str(e))

        ttk.Button(win, text="Exit", command=win.destroy).pack(pady=10)

    def v_user_books():
            win = Toplevel()
            win.title("Issued Books")
            win.geometry("900x400")

            cols = ("entry_id", "id", "name", "bc", "book")

            tree = ttk.Treeview(win, columns=cols, show="headings")
            tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

            for col in cols:
                tree.heading(col, text=col, anchor="center")
                tree.column(col, anchor="center", width=150)

            try:
                rows = ad.user_books()
                for row in rows:
                    tree.insert("", END, values=row)
            except Exception as e:
                messagebox.showerror("Error", str(e))

            ttk.Button(win, text="Exit", command=win.destroy).pack(pady=10)
    
    def manage_books_window():
        win = Toplevel()
        win.attributes("-topmost", True)
        win.title("Manage Books")
        win.geometry("500x450")

        Label(
            win,
            text="Manage Library Books",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        # ---- VIEW BOOKS ----
        def view_books():
            view = Toplevel(win)
            view.transient(win)   
            view.title("All Books")
            view.geometry("400x300")

            listbox = Listbox(view, font=("Arial", 12))
            listbox.pack(fill=BOTH, expand=True, padx=10, pady=10)

            try:
                rows = ad.get_books()
                for row in rows:
                    listbox.insert(END, row[0])
            except Exception as e:
                messagebox.showerror("Error", str(e))

            ttk.Button(view, text="Exit", command=view.destroy).pack(pady=10)

        # ---- ADD BOOKS ----
        def add_books_ui():
            addw = Toplevel(win)
            addw.transient(win)   
            addw.title("Add Books")
            addw.geometry("400x250")

            Label(addw, text="Enter book name:").pack(pady=10)
            entry = Entry(addw, width=40)
            entry.pack(pady=5)

            def submit():
                if not entry.get().strip():
                    messagebox.showerror("Error", "Input cannot be empty")
                    return
                ad.add_books(entry.get())
                messagebox.showinfo("Success", "Books added")
                addw.destroy()

            ttk.Button(addw, text="Add", command=submit).pack(pady=15)

        # ---- REMOVE BOOK ---
        
        def remove_books_ui():
            rem = Toplevel(win)
            rem.transient(win)   
            rem.title("Remove Book")
            rem.geometry("400x250")

            Label(rem, text="Enter book name to remove:").pack(pady=10)
            entry = Entry(rem, width=40)
            entry.pack(pady=5)

            def submit():
                if ad.remove_books(entry.get()):
                    messagebox.showinfo("Success", "Book removed")
                    rem.destroy()
                else:
                    messagebox.showerror("Error", "Book not found")

            ttk.Button(rem, text="Remove", command=submit).pack(pady=15)

        # ---- MAIN BUTTONS ----
        ttk.Button(win, text="View Books", command=view_books).pack(pady=10)
        ttk.Button(win, text="Add Books", command=add_books_ui).pack(pady=10)
        ttk.Button(win, text="Remove Book", command=remove_books_ui).pack(pady=10)
        ttk.Button(win, text="Exit", command=win.destroy).pack(pady=20)

    
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 18, "bold"))

    ttk.Button(panel, text="Manage Books", style="TButton", command=manage_books_window).pack(pady=10)
    ttk.Button(panel, text="View Students", style="TButton", command=view_students_window).pack(pady=10)
    ttk.Button(panel, text="User Books", style="TButton", command=v_user_books).pack(pady=10)
    ttk.Button(panel, text="Logout", style="TButton", command=panel.destroy).pack(pady=20)
