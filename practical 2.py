from time import sleep
#Sum of digits
def sumd():
    n=int(input("Enter the number:"))
    t=n
    sum=0
    while t>0:
        r=t%10
        sum=sum+r
        t//=10
    print("The sum of the digits of",n,"is",sum)

#Palindrome or not
def pal():
    num=int(input("Enter anything: "))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome.")
    else:
        print("The number is not a palindrome.")
#Armstrong or not
def arm():
    n=int(input("Enter the number:"))
    t=n
    sum=0
    while t>0:
        r=t%10
        sum=sum+r**3
        t//=10
    if sum==n:
        print(n,"is an Armstrong")
    else:
        print(n,"is NOT an Armstrong")

while True:
    print("1 for Palindrome or not \n2 for Sum of digits \n3 for Armstrong or not")
    print()
    ch=int(input("Enter your choice: "))    
    if ch==1:
        pal()
    if ch==2:
        sumd()
    if ch==3:
        arm()
    print()
    sleep(1)