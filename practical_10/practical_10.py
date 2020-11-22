'''10.	Write a menu driven program using binary file

a)  Insert Student Record (Rollno, Name, Marks)

b)	Display Record
c)	Search based on Roll no

d)	Update Marks

e)	Delete a record

f)	Exit'''


import pickle

def insert():
    f = open("bin.dat","ab")
    rollno = int(input("Roll no: "))
    name = input("Name: ")
    marks = int(input("marks: "))
    l = [rollno, name, marks]
    pickle.dump(l, f)
    f.close()
    
def display():
    f = open("bin.dat","rb")
    try:
        while True:
            l = pickle.load(f)
            print(l)
    except EOFError:
        f.close()
    
def search():
    f = open("bin.dat","rb")
    rollno = int(input("Roll no: "))
    try:
        while True:
            l = pickle.load(f)
            if l[0] == rollno:
                print(l)
                break
    except EOFError:
        print("Rollno not found")
        f.close()

def update():
    f = open("bin.dat","rb+")
    rollno = int(input("Roll no: "))def search():
    f = open("bin.dat","rb")
    rollno = int(input("Roll no: "))
    try:
        while True:
            l = pickle.load(f)
            if l[0] == rollno:
                print(l)
                break
    except EOFError:
        print("Rollno not found")
        f.close()
    try:
        while True:
            l = pickle.load(f)
            if l[0] == rollno:
                marks = 
                break
    except EOFError:
        print("Rollno not found")
        f.close()

#menu
print("1. Insert record\n2. Diplay record\n3. Search rollno\n4. Update marks\n5. Delete record\n6. Exit")
while True:
    ch = int(input("Choice: "))
    if ch == 1:
        insert()
    if ch == 2:
        display()
    if ch == 3:
        search()
        
