
n = "india"
b = len(n)

for i in range(b):
    for j in range(b):
        if i == j:
            print(n[i], end="")
        else:
            print("-", end="")
    print()
# i=9
# while i > 5:
#     i -= 1
#     if i == 3:
#         continue
#     print(i)
