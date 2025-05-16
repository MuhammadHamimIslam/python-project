import sqlite3
import time

conn = sqlite3.connect("student_info.db") # connect to database 
c = conn.cursor() # pit the cursor

"""Create a table named students if it's not exists
table column -> Name(TEXT), Age(INTEGER), ID_No(INTEGER), Address(TEXT), Date(TEXT ) (When it's updated)
"""
c.execute("""CREATE TABLE IF NOT EXISTS students (
    Name TEXT,
    Age INTEGER,
    ID_No INTEGER UNIQUE,
    Address TEXT,
    Date TEXT)""")

# add students to the database 
def add_student(name, age, id_no, address):
    """
    DESCRIPTION: add student to the databases 
    
    args: 
    name -> student's name
    age -> student's age 
    id_no -> student's ID No
    Address -> student's Address
    
    how it works:
    using context manager INSERT data to the table 
    """
    with conn: 
        c.execute("INSERT INTO students VALUES(:name, :age, :id_no, :address, :time)", {"name": name, "age": age, "id_no": id_no, "address": address, "time": time.asctime()})

# update info of the students 
def update_student_info(id_no, update_field, data):
    """
    DESCRIPTION: update student info 
    
    args: 
    id_no -> student's ID No to identify 
    update_field -> field that will be updated
    data -> updated data
    
    how it works:
    using context manager UPDATE data to the table 
    """
    with conn: 
        c.execute(f"UPDATE students SET {update_field} = :data, Date = :time WHERE ID_No = :id_no", {"time": time.asctime(), "data": data, "id_no": id_no})
        
# delete students 
def delete_student(id_no):
    """
    DESCRIPTION: delete student 
    
    args: 
    id_no -> student's ID No to identify 
    
    how it works:
    using context manager DELETE the targeted student
    """
    with conn: 
        c.execute("DELETE FROM students WHERE ID_No = :id_no", {"id_no": id_no})

# get the students by info
def get_student(id_no):
    """
    DESCRIPTION: get the student info by id
    
    args: 
    id_no -> student's ID No to identify 
    
    how it works:
    using context manager then find student by id
    """    
    with conn: 
        c.execute("SELECT * FROM students WHERE ID_No = :id_no", {"id_no": id_no})
    return c.fetchall()

# take valid input 
def take_inp(prompt):
    """
    DESCRIPTION: taking valid input 
    
    args: 
    prompt -> prompt while taking the input
    
    how it works:
    run an infinite while loop then put a try, except block if user input is invalid it goes to except block. If user input is correct return the value by trimming whitespaces and break the loop
    """
    while True:
        try:
            data = input(prompt)
            return data.strip()
            break
        except ValueError:
            print("Enter a valid input")
            
help_msg = """ Choose one
1. to add student
2. to update student's info
3. to get the student's info
4. to delete a student from database 
5. or q to quit the program 
6. to print this message 
"""

print(help_msg) # print the help message initially 

while True:
    choice = input("Enter your choice: ") # get the choice to perform operation 
    
    match choice: # a match case operation 
        case "1":
            "if choice is 1 then take the necessary input the call add_student()"
            name = take_inp("Enter the name: ")
            age = int(take_inp("Enter the age: "))
            id_no = int(take_inp("Enter the id no: "))
            address = take_inp("Enter the address: ")
            add_student(name, age, id_no, address)
        case "2":
            "if choice is 2 then take the necessary input the call update_student_info()"
            
            id_no = int(take_inp("Enter the ID No: "))
            field = take_inp("Enter the field name (Name, Age, ID_No, Address) to update: ")
            data = take_inp("Enter the correct data of the field: ")
            update_student_info(id_no, field, data)
        case "3":
            "if choice is 3 then take the necessary input the call get_student()"
            id_no = int(take_inp("Enter the ID No: "))
            print(get_student(id_no))
        case "4":
            "if choice is 4 then take the necessary input the call delete_student()"
            id_no = int(take_inp("Enter the ID No: "))
            delete_student(id_no)
        case "5" | "q": 
            "if choice is 5 or q simply break the while loop and leave the program"
            print("Left program successfully!")
            break
        case "6": 
            "if choice is 6 then print the help_msg"
            print(help_msg)
        case _: 
            "if choice is invalid then print error message"
            print("Invalid input")