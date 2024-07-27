a=['a','b','e','d','i','f','o','u','A','E','e']
def fun(n):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if n in  vowels :
        return vowels
filter_vowels = list(filter(fun, a))
print(filter_vowels)
print(filter_vowels.pop(a))
