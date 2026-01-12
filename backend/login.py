# import library as li
from db import get_connection

def login(nam, id):
    conn, cursor = get_connection()
    cursor.execute(
    "SELECT 1 FROM registry WHERE name=%s AND id=%s LIMIT 1",
    (nam, id)
    )
    exists = cursor.fetchone() is not None
    
    if exists:
        # print(f"welcome, {nam}!") #printing welcome - change this as you want subh
        cursor.execute(
        "SELECT bc, book FROM books WHERE name=%s AND id=%s",
        (nam, id)
    )
        data = cursor.fetchone()
        if data:
            bc, book= data
        else:
            bc=book=None     
        conn.close()  
        return bc, book
    else:
        print("credentials are not found")
        return None
    
# the data here we got is the book-count as bc, book(if), nam and id. use this for get_book and etc, there exists a separate check_bc for same purpose but you can remove if you want
# ~sup 28th dec