import re

def striing(clause: str):
    string=input(f"input your full {clause}: ").title()
    if not isinstance(string, str):
        raise TypeError("expected a string")
    return string
def namecheck(str_value: str):
    if p:=str_value.strip().split(" "):
        Name=p[0]
        Surname=p[-1]
        middle="".join(p[1:-1]) if len(str_value)>2 else ""
        # print(Name.title())
        return [Name, middle, Surname]
    else:
        print("you have entered something wrong")
    
def get_pwhole_no(prompt:str):
        try:
            s = int(input(f"Enter {prompt}: "))
        except ValueError:
            raise ValueError(f"Error: Please enter a valid number for {prompt.lower()}")
        if s < 0:
            raise ValueError(f"Error: {prompt} must be a positive whole number")
        return s

class library:
    @classmethod
    def name(cls):
        name=namecheck(striing("Name"))
        return name
    @classmethod
    def section(cls):
        sec=(striing("Section"))
        if re.search(r"^[a-zA-Z0-9]+$", sec, re.IGNORECASE):
            return sec.upper()
        else:
            raise ValueError("you wrote something that shouldnt be there[only alphanumeric supported]")
    @classmethod
    def roll(cls):
        return get_pwhole_no("Roll")
    @classmethod
    def Class(cls):
        return get_pwhole_no("Class")
    
def get_input():  
    name=library.name()
    try:
        clss= library.Class()
    except ValueError as e:
        print(e)
    try:
        section=library.section()
    except ValueError as e:
        print(e)
    try:
        roll= library.roll()
    except ValueError as e:
        print(e)
    return [name,clss,section,roll]

def Id():
    while True:
        id=int(input("Enter Your Id: "))
        if 1000<id<9999:
            break
    return id
