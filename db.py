import pymysql
from auth import use_password, clear_password 

def create_db():
    while True:
        password = use_password()
        try:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password=str(password),
                autocommit=True
            )
            break 
            
        except pymysql.err.OperationalError as e:
            # Error 1045 = Access Denied (Wrong Username/Password)
            if e.args[0] == 1045: 
                print("\n Incorrect MySQL password. Let's try that again.")
                clear_password() 
            else:
                # other error not accounted for
                raise e

    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS `library`")
    cursor.execute("USE `library`")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registry (
    e_id INT AUTO_INCREMENT PRIMARY KEY,
    id INT ,
    name VARCHAR(50),
    mname VARCHAR(50),
    surname VARCHAR(50),
    class INT,
    sec VARCHAR(10),
    roll INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
    entry_id INT AUTO_INCREMENT,
    id INT,
    name VARCHAR(50),
    bc INT DEFAULT 0,
    book VARCHAR(255) DEFAULT '',
    PRIMARY KEY (entry_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbooks (
    entry_id INT AUTO_INCREMENT PRIMARY KEY,
    number INT DEFAULT 1,
    bname VARCHAR(250)
    )           
    """)
    
    cursor.close()
    conn.close()

def get_connection():
    password = use_password()

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=password,
        database="library",
        autocommit=True
    )

    cursor = conn.cursor()
    return conn, cursor

# run this just after the app starts no matter who
