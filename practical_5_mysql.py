import mysql.connector as mc

cnx = mc.connect(host="localhost",user="root", password="root")
cursor = cnx.cursor()
cursor.execute("use practicals")

def add_student():
    name = input("Name: ")
    marks = input("Marks: ")
    print()
    add = "INSERT INTO student(name, marks) " "VALUES (%s, %s)"
    data = (name, int(marks))
    cursor.execute(add,data)
    
def remove_student():
    name = input("Name: ").strip().title()
    remove= "DELETE FROM student WHERE name LIKE %s"
    data = (name,)
    cursor.execute(remove,data)
    print(f"Query OK. {cursor.rowcount} rows affected.\n")

def display_student():
    print("Leave blank to show all.")
    name = input("Name: ").strip().title()
    print()
    if name == "":
        display= "select * from student"
        student_data = tuple()
    else:
        display= "select * from student where name like %s"
        student_data = (name,)
    cursor.execute(display, student_data)
    match_list = cursor.fetchall()
    if match_list:
        for id_no, name_, marks in match_list:
            print(f"[{id_no}]{name_}: {marks}")
        print()
    else:
        print("No students found.\n")

def modify_student():
    name = input("Name: ").strip().title()
    marks = input("New Marks: ")
    modify= "update student SET marks=%s where name=%s"
    data = (int(marks), name)
    cursor.execute(modify,data)
    print(f"Query OK. {cursor.rowcount} rows affected.\n")

print("1- Add student")
print("2- Remove student")
print("3- Display student Marks")
print("4- Modify student Marks")
print("5- Exit\n")
while True:
    choice = input("choice: ")
    print()
    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        display_student()
    elif choice == "4":
        modify_student()
    elif choice == "5":
        cursor.close()
        cnx.close()
        break