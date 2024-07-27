# # a = 10 #public
# # _b = 20 #protected
# # __c = 30 #private


# class Hi:
#     def __init__(self):
#         self.a = 10
#         self._b = 20
#         self.__c = 30

#     def hello(self):
#         print(self.a)
#         print(self._b)
#         print(self.__c)

# class Bye(Hi):
#     def hello1(self):
#         print(self.a)
#         print(self._b)
#         print(self._Hi__c)



# print(a)
from bank import Hi

ans = Hi("122", 500)
ans.display1()
