from time import sleep
def prime():
    num=int(input("Enter the number: "))
    if num>1:
        for i in range(2, num):
            if (num % i)==0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

def perf():
    num=int(input(" Please Enter any Number: "))
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
    if (sum==num):
        print(num,"is a Perfect Number")
    else:
        print(num,"is not a Perfect Number")
while True:
    print("1 for Prime or not \n2 for Perfect or not")
    ch=int(input('Enter your choice: '))
    if ch==1:
        prime()
    if ch==2:
        perf()
    print()
    sleep(1)