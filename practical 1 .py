student={}
n=int(input("Enter number of winners: "))
print()
for i in range(n):
    print(i+1)
    name=input("Enter name of winner: ")
    wins=int(input("Enter number of wins: "))
    student[name]=wins
    print()

print("Name of the winners","\t","Number of wins")

for j in student:
    print(j,"\t","\t","\t",student[j])
