import csv


try:
    with open("employee.csv", "r", newline="") as csvfile:
        empreader = csv.reader(csvfile)
        EMPLOYEES = list(empreader)
except FileNotFoundError:
    EMPLOYEES = []


def save():
    with open("employee.csv", "w", newline="") as csvfile:
        empwriter = csv.writer(csvfile)
        empwriter.writerows(EMPLOYEES)


def new_employee():
    emp_no = input("Employee Number: ")
    name = input("Name: ")
    salary = input("Salary: ")
    print()

    EMPLOYEES.append((emp_no, name, salary))
    save()


def search_for_employee():
    emp_no = input("Employee Number to Search for: ")
    print()
    for employee in EMPLOYEES:
        if employee[0] == emp_no:
            print("Name:", employee[1])
            print("Salary:", employee[2], "\n")
            break
    else:
        print("Employee Not Found\n")


while True:
    print("1: Add New Employee")
    print("2: Search for Employee")
    print("3: Exit\n")

    choice = input("Choice: ")
    print()

    if choice == "1":
        new_employee()
    elif choice == "2":
        search_for_employee()
    elif choice == "3":
        break
