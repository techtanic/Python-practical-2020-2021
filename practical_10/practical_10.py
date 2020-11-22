'''10.	Write a menu driven program using binary file

a)  Insert Student Record (Rollno, Name, Marks)

b)	Display Record
c)	Search based on Roll no

d)	Update Marks

e)	Delete a record

f)	Exit'''

import pickle

try:
    with open("bin.dat", "rb") as f:
        student_record = pickle.load(f)
except FileNotFoundError:
    student_record = {}


def save():
    with open("bin.dat", "wb") as f:
        pickle.dump(student_record, f)


def insert_record():
    roll_no = int(input("Roll Number: "))
    name = input("Name: ")
    marks = input("Marks: ")
    print()

    student_record[roll_no] = [name, marks]
    print("Record added.")


def display_records():
    if len(student_record) == 0:
        print("No students found.")
    else:
        print("Roll No | Name | Marks\n")
        for student in student_record:
            print(student, *student_record[student], sep=" | ")


def search_for_record():
    roll_no = int(input("Roll Number to search for: "))
    print()

    if roll_no in student_record:
        print(roll_no, *student_record[roll_no], sep=" | ")
    else:
        print("Student not found.")


def update_marks():
    roll_no = int(input("Roll Number: "))
    print()

    if roll_no in student_record:
        print(roll_no, *student_record[roll_no], sep=" | ")
        marks = int(input("New Marks: "))
        student_record[roll_no][1] = marks
    else:
        print("Student not found.")


def delete_record():
    roll_no = int(input("Roll Number: "))
    print()

    if roll_no in student_record:
        print(roll_no, *student_record[roll_no], sep=" | ")
        confirm = input("Confirm delete? (y/n): ")
        if confirm.lower() == "y":
            del student_record[roll_no]
    else:
        print("Student not found.")



print("1: Insert Record")
print("2: Display Records")
print("3: Search based on Roll Number")
print("4: Update Marks")
print("5: Delete Record")
print("6: Exit\n")

while True:
    choice = int(input("Choice: "))
    print()

    if choice == 1:
        insert_record()
    if choice == 2:
        display_records()
    if choice == 3:
        search_for_record()
    if choice == 4:
        update_marks()
    if choice == 5:
        delete_record()
    if choice == 6:
        break

    save()
    print()
