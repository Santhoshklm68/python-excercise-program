# number = int(input("enter the number: "))
# if number%2 == 0:
#     print("its a even number")
# else: 
#     print("its a odd number")

class Numbers:
    def __init__(self, number):
        self.number = number
        if self.number%2 == 0:
            print("its a even number")
        else:
            print("its a odd number")
num = int(input("enter the number"))
ans = Numbers(num)

print(ans)