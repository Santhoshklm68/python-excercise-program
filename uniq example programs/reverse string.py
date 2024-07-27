n = input("enter the string: ")
reverse_string = ""
for i in range(len(n)-1,-1,-1):
    reverse_string += n[i]
print(reverse_string)