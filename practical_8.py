'''Write a python program to create a stack called Employee,
to perform the basic operations on stack using list.
The list contains two values – employee number and employee name.'''

Employee = [[102,"sample1"],[103,"sample2"]]

while True:
    print("\n1 Add\n2 Remove\n3 Show")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        num = int(input("Employee number: "))
        name = input("Employee name: ")
        l = [num, name]
        Employee.append(l)

    if ch == 2:
        if Employee:
            print("Removed:",Employee.pop())
        else:
            print("\nStack is empty")

    if ch == 3:
        for t in Employee[::-1]:
            print(t)