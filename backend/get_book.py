# import library as li 
import backend.login as lg
from db import get_connection

def check_bc(id, name):
    conn, cursor = get_connection()
    cursor.execute(
    "SELECT bc, book FROM books WHERE name=%s AND id=%s",
    (name, id)
)
    data = cursor.fetchone()
    conn.close()
    return data if data else (None, None)

def get_books():
    conn, cursor = get_connection()
    cursor.execute("SELECT bname FROM tbooks WHERE number=1")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_book(name, book, id):
    conn, cursor = get_connection()
    cursor.execute(
    "UPDATE books set bc= 1, book=%s WHERE name=%s AND id=%s",
    (book, name, id))
    cursor.execute("UPDATE tbooks set number=0 WHERE bname=%s",
    (book,))
    conn.close()
    return 1
    

def remove_book(name,book, id):
    conn, cursor = get_connection()
    cursor.execute(
    "UPDATE books sET bc= 0, book='' WHERE name=%s AND id=%s",
    (name, id)) 
    cursor.execute("UPDATE tbooks set number=1 WHERE bname=%s",
    (book,))
    conn.close()
    return 1
   
# if check_bc(name,id)==0:
#     add_book(name,book,id)
# else:
#     remove_book(name, id)
    
# force users to use check bc after every use of add_book and remove_book for latest data on their activities