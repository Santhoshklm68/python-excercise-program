class Bank:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance

    def display(self):
        print("account_no:", self.account_no)
        print("balance:", self.__balance)


    def deposit(self):
        deposit_amount = int(input("enter the deposit amount: "))
        self.__balance += deposit_amount 
        print("Amount deposited successfully:", self.__balance)

    def withdrawal(self):
        withdrawal_amount = int(input("enter the withdrawal amount: "))
        if withdrawal_amount > self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= withdrawal_amount
            print("amount withdrawal successfully :", self.__balance)

class Hi(Bank):
    def display1(self):
        print(self.account_no)
        print(self._Hi__balance)

name = Bank("12647", 500)
name.withdrawal()
