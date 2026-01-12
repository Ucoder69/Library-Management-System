import pymysql
import random
from db import get_connection

def namecheck(str_value: str):
    if p:=str_value.strip().split(" "):
        Name=p[0]
        Surname=p[-1]
        middle="".join(p[1:-1]) if len(str_value)>2 else ""
        # print(Name.title())
    else:
        print("you have entered something wrong")
    return Name, middle, Surname 
        
def register(sname :str , class_, sec, roll):
    id_=random.randint(1000, 99999)
    try:
        name, mname , surname = namecheck(sname)
    except Exception:
        name, mname , surname =''
        
    conn, cursor = get_connection()

    cursor.execute(
    """
    INSERT INTO registry (id, name, mname, surname, class, sec, roll)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,
    (id_, name, mname, surname, class_, sec, roll))


    cursor.execute(
    """
    INSERT INTO books (id, name, bc, book)
    VALUES (%s, %s, 0, '')
    """,
    (id_, name)
)

    cursor.close()
    conn.close()
    return name, id_


# register("Suparno Dey", 12, "a2", 35)