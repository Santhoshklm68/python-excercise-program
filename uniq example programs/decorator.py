num = input("enter the number: ")
def fun(func):
    def wrapper():
        input_format = ('+91')
        i = len(num)
        if i == 10:
            print( input_format," " +num)
        else:
                print("enter the correct number")
    return wrapper

@fun
def faf():
    pass
faf()