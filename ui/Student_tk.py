from tkinter import *
from tkinter import ttk, messagebox
import backend.login as lg
import backend.register as rg
import backend.get_book as gb

def Student():
    root = Toplevel()
    root.title("Student Portal")
    root.geometry("500x550")
    root.config(bg="#333333")

    # ---- TITLE (unchanged, top) ----
    Label(
        root,
        text="Student Login",
        font=("Arial", 26, "bold"),
        fg="white",
        bg="#333333"
    ).pack(pady=30)

    # ---- CENTERED CONTENT FRAME ----
    content = Frame(root, bg="#333333")
    content.pack(expand=True)

    # ---- INPUT FIELDS (centered) ----
    Label(content, text="Student ID", fg="white", bg="#333333").pack(pady=(0, 5))
    id_entry = Entry(content, width=25)
    id_entry.pack(pady=(0, 15))

    Label(content, text="Username", fg="white", bg="#333333").pack(pady=(0, 5))
    name_entry = Entry(content, width=25)
    name_entry.pack(pady=(0, 25))

    # ---- LOGIN ----
    def login_student():
        sid = id_entry.get()
        name = name_entry.get()

        data = lg.login(name, sid)
        if data:
            bc, book = gb.check_bc(sid, name)   # 🔑 DB truth
            has_book = (bc == 1)

            root.destroy()                     # ✅ close student login window
            student_dashboard(sid, name, has_book)
            
        else:
            messagebox.showerror("Error", "Invalid credentials")
            root.destroy()

    # ---- REGISTER ----
    def register_student():
        root.destroy()                         # ✅ close student login window

        reg = Toplevel()
        reg.title("Register")
        reg.geometry("400x350")

        Label(reg, text="Full Name").pack(pady=5)
        name = Entry(reg)
        name.pack(pady=5)

        Label(reg, text="Class").pack(pady=5)
        cl = Entry(reg)
        cl.pack(pady=5)

        Label(reg, text="Section").pack(pady=5)
        sec = Entry(reg)
        sec.pack(pady=5)

        Label(reg, text="Roll").pack(pady=5)
        roll = Entry(reg)
        roll.pack(pady=5)

        def submit():
            uname, uid = rg.register(
                name.get(), cl.get(), sec.get(), roll.get()
            )
            messagebox.showinfo("Registered", f"ID: {uid}")
            reg.destroy()

        ttk.Button(reg, text="Submit", command=submit).pack(pady=15)

    # ---- BUTTONS (lowered) ----
    ttk.Button(content, text="Login", command=login_student).pack(pady=(20, 10))
    ttk.Button(content, text="Register", command=register_student).pack()


# ----------------- DASHBOARD -----------------

def student_dashboard(sid, name, has_book):
    dash = Toplevel()
    dash.attributes("-topmost", True)
    dash.title("Student Dashboard")
    dash.geometry("400x350")
    dash.config(bg="#333333")

    center = Frame(dash, bg="#333333")
    center.pack(expand=True)

    Label(
        center,
        text=f"Welcome, {name}!",
        font=("Arial", 22, "bold"),
        fg="white",
        bg="#333333"
    ).pack(pady=(0, 25))

    # ---- BUTTONS (defined early so we can control state) ----
    btn_status = ttk.Button(center, text="Check Status")
    btn_add = ttk.Button(center, text="Add Book")
    btn_remove = ttk.Button(center, text="Remove Book")

    btn_status.pack(pady=8)
    btn_add.pack(pady=8)
    btn_remove.pack(pady=8)

    # ---- APPLY STATE BASED ON bc ----
    def apply_state(bc):
        if bc == 1:
            btn_add.config(state=DISABLED)
            btn_remove.config(state=NORMAL)
        else:
            btn_add.config(state=NORMAL)
            btn_remove.config(state=DISABLED)

    apply_state(1 if has_book else 0)

    # ---- STATUS CHECK (DB TRUTH) ----
    def status():
        bc, book = gb.check_bc(sid, name)

        if bc is None:
            messagebox.showerror("Error", "Unable to fetch status")
            return

        apply_state(bc)

        messagebox.showinfo(
            "Status",
            "Book Issued" if bc == 1 else "No Book Issued"
        )
    def status_():
        bc, book = gb.check_bc(sid, name)

        if bc is None:
            messagebox.showerror("Error", "Unable to fetch status")
            return

        apply_state(bc)

    # ---- ADD / REMOVE ----
    def add_book():
        addw = Toplevel(dash)
        addw.transient(dash)   
        addw.title("Select Book")
        addw.geometry("440x350")
        addw.config(bg="#333333")

        Label(
            addw,
            text="Select a book",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#333333"
        ).pack(pady=15)

        # ---- FETCH BOOK LIST ----
        try:
            rows = gb.get_books()   # from tbooks
            book_list = [r[0] for r in rows]
        except Exception as e:
            messagebox.showerror("Error", str(e))
            addw.destroy()
            return

        if not book_list:
            messagebox.showinfo("Info", "No books available")
            addw.destroy()
            return

        # ---- DROPDOWN ----
        selected_book = StringVar()

        combo = ttk.Combobox(
            addw,
            textvariable=selected_book,
            values=book_list,
            state="readonly",
            width=30
        )
        combo.pack(pady=10)
        combo.current(0)

        # ---- TAKE BUTTON ----
        def take_book():
            book = selected_book.get()
            gb.add_book(name, book, sid)   # 🔑 YOUR FUNCTION
            messagebox.showinfo("Success", f"Book '{book}' taken")
            addw.destroy()
            status_()   # 🔁 refresh dashboard state

        ttk.Button(addw, text="Take", command=take_book).pack(pady=15)
        ttk.Button(addw, text="Cancel", command=addw.destroy).pack()

    def remove_book():
        bc, book = gb.check_bc(sid, name)
        gb.remove_book(name,book, sid)
        messagebox.showinfo("Success", "Book removed")
        status_()   # 🔁 refresh state from DB

    # ---- CONNECT COMMANDS ----
    btn_status.config(command=status)
    btn_add.config(command=add_book)
    btn_remove.config(command=remove_book)

