def bub_sort(l):
    n=len(l)-1
    for i in range(n):
        for j in range(n):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(f"Sorted list: {l}")

def insert_sort(l):
    for i in range(1,len(l)):
        while l[i-1]>l[i] and i>0:
            l[i],l[i-1]=l[i-1],l[i]
            i-=1
    print(f"Sorted list: {l}")
print("1- Bubble sort \n2- Insertion sort")
print("3- Exit")
while True:
    ch=int(input("Choice: "))
    if ch==3:
        exit()
    l=list(map(int,input("Enter the list: ").strip().split()))
    if ch==1:
        bub_sort(l)
    if ch==2:
        insert_sort(l)
    print()
"[25,34,0,987,65,43,234,567,89,0,369,48,45,7654]"