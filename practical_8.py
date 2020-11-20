'''Write a python program to create a stack called Employee,
to perform the basic operations on stack using list.
The list contains two values – employee number and employee name.'''

Employee = []

while True:
    print("\n1 Add\n2 Remove\n3 Show")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        e_num = int(input("Employee number: "))
        e_name = input("Employee name: ")
        l = [e_num, e_name]
        Employee.append(l)

    if ch == 2:
        if Employee:
            print("Removed:",Employee.pop())
        else:
            print("\nStack is empty")

    if ch == 3:
        print(Employee[::-1])