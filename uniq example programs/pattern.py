
n = int(input("Enter the number of lines: "))
row=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
        row +=1
    print()
