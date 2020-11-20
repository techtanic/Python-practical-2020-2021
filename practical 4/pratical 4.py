from time import sleep
from shape import *

print("1- Perimeter of Circle \n2- Area of Circle")
print("3- Perimeter of Rectangle \n4- Area of Rectangle")
print("5- Exit")
while True:
    ch=int(input("Your choice: "))
    if ch==1:
        r=float(input("Radius of the circle: "))
        print("The perimeter is: ",circle.p(r))
    if ch==2:
        r=float(input("Radius of the circle: "))
        print("The area is: ",circle.a(r))
    if ch==3:
        l=float(input("length: "))
        b=float(input("breadth: "))
        print("The perimeter is: ",rectangle.p(l,b))
    if ch==4:
        l=float(input("length: "))
        b=float(input("breadth: "))
        print("The area is: ",rectangle.a(l,b))
    if ch==5:
        exit()
    print()
    sleep(1)