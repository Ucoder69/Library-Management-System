import os
import getpass

PASS_FILE = "db_pass.txt"

def get_password(pwd):
    # pwd = getpass.getpass("Enter MySQL root password: ")
    with open(PASS_FILE, "w") as f:     # to store
        f.write(pwd)

    return pwd

def use_password():
    if os.path.exists(PASS_FILE):
        with open(PASS_FILE, "r") as f:
            return f.read().strip()     # password already store
    raise RuntimeError("Database password not found")