def lin_search():
    l=input("Enter the list: ").split()
    x=input("Element to be searched: ")
    print(f"List:{l}")
    for i in range(0,len(l)):
        if l[i]==x:
            return print (f"Element found at index: {i} ")
    return print("Element not found.")

def bin_search():
    l=list(map(eval,input("\nEnter the numbers : ").strip().split()))
    l.sort()
    print(f"List:{l}")
    x=eval(input("Element to be searched: "))
    low,high=0,len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return print(f"Element found at index: {mid}")
        if l[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return print("Element not found.")
print("1- Linear search \n2- Binary search")
print("3- Exit")
while True:
    ch=int(input("Choice: "))
    if ch==1:
        lin_search()
    if ch==2:
        bin_search()
    if ch==3:
        exit()
    print()