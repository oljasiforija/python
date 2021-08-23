
class Bank_account():
    def __init__(self, account_name, interest_rate, balance):
        self.acount_name = account_name
        self.interest_rate = interest_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance > amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_acc_info(self):
        print(f"Acc Name: {self.acount_name} Interest rate: {self.interest_rate}% Balance: ${self.balance}")
    def yield_interest(self):
        if self.balance > 0:
            return self.balance*self.interest_rate
        else:
            return self



account1 = Bank_account('Private Account', 4, 500)
account2 = Bank_account('Bussines Account', 2, 540)

account1.deposit(100)
account1.deposit(340)
account1.deposit(2344)
account1.withdraw(300)
account1.display_acc_info()
account2.deposit(700)
account1.deposit(550)
account2.withdraw(440)
account2.withdraw(300)
account2.withdraw(423)
account2.withdraw(110)
account2.yield_interest()
account2.display_acc_info()









