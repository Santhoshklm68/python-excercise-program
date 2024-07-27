class Bank:
    def __init__(self, account_number, name, branch, mobile, balance):
        self.account_number = account_number
        self.name = name
        self.branch = branch
        self.mobile = mobile
        self.balance = balance

    def display(self):
        print("account_number:", self.account_number)
        print("name:", self.name)
        print("branch:", self.branch)
        print("mobile:", self.mobile)
        print("balance:", self.balance)

    def withdrawal(self):
        amount = int(input("enter the withdrawal amount: "))
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount 
            print("withdrawal successfully", self.balance)

    def deposit(self):
        deposit_amount = int(input("enter the deposit amount: "))
        self.balance += deposit_amount
        print('amount deposited successfully your balance amount is: ',self.balance)        
            
customer1 = Bank("123456", "santhosh","cbe","6380526174",balance=1000)

customer1.withdrawal()
customer1.display()
customer1.deposit()
customer1.display()