from db import get_connection

def get_books():
    conn, cursor = get_connection()
    cursor.execute("SELECT bname FROM tbooks")
    rows = cursor.fetchall()
    conn.close()
    # book = [row[0] for row in rows]
    return rows

def user_books():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    cursor.close()    
    conn.close()
    return rows


def add_books(book :str):
    book= book.strip() # type: ignore
    
    conn, cursor = get_connection()

    cursor.executemany(
        "INSERT INTO tbooks (bname, number) VALUES (%s, 1)",
        (book,)
    )
    cursor.close()
    conn.close()
    return 1

def remove_books(book :str):
    conn, cursor = get_connection()

    try:
        cursor.execute(
            "DELETE FROM tbooks WHERE bname = %s",
            (book,)
        )
        cursor.close()
        conn.close()
        return 1
    except:
        cursor.close()
        conn.close()
        return 0

def show_database():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM registry")
    rows = cursor.fetchall()
    cursor.close()    
    conn.close()
    return rows