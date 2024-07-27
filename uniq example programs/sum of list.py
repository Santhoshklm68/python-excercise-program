n = [1,2,3,4,5,6,7,8]
b = int(input("enter the number: "))
for i in range(len(n)):
    if b == i:
        n.remove(b)
        print(n)
    else:
        print(sum(n))