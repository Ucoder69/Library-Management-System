import keyring
import getpass

SERVICE_NAME = "PythonLibrarySystem"
ACCOUNT_NAME = "mysql_root"

def use_password():
    """Looks for the password in the os vault. 
    If first run, it prompts the user securely."""
    
    password = keyring.get_password(SERVICE_NAME, ACCOUNT_NAME)
    
    if password is None:
        print("--- First Time Database Setup ---")
        # getpass hides the typing so no one can shoulder-surf the password
        password = getpass.getpass("Enter your MySQL root password: ")
        
        keyring.set_password(SERVICE_NAME, ACCOUNT_NAME, password)
        print("Password saved securely in your system's credential manager!\n")
        
    return password
    
def clear_password():
    """Wipes the stored password if it's incorrect."""
    try:
        keyring.delete_password(SERVICE_NAME, ACCOUNT_NAME)
    except keyring.errors.PasswordDeleteError:
        pass
