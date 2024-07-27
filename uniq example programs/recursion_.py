def odd_num(n):
    if n <= 0:
        return 0
    elif n % 2 !=0:
        return n + odd_num(n-2)
    else:
        return odd_num(n-1)
n = int(input("enter the number: "))   
ans = odd_num(9)
print(ans)


   