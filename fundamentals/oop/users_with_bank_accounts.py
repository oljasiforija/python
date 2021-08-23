
class Bank_account():
    def __init__(self, account_type, interest_rate, balance):
        self.acount_type = account_type
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
        print(f"Acc type: {self.acount_type} Interest rate: {self.interest_rate}% Balance: ${self.balance}")
    def yield_interest(self):
        if self.balance > 0:
            return self.balance*self.interest_rate
        else:
            return self
    

class User():
    def __init__(self, first_name, last_name, email, account_name, interest_rate, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{first_name} {last_name}"
        self.email = email
        self.account = Bank_account(account_name, interest_rate, balance)




user1 = User('Michael','Michaelson','michaelemail@gmail.com','Private Account', 4, 500)
user2 = User('Brad','Pitt','bradpitt@gmail.com', 'Bussines Account', 2, 540)
user3 = User('Jane','Doe','janedoe@gmail.com', 'Private Account', 4, 600)

user1.account.deposit(100)
user1.account.display_acc_info()
user1.account.deposit(200)
user1.account.deposit(700)
user1.account.deposit(400)
user1.account.display_acc_info()
user2.account.deposit(230)
user2.account.deposit(234)
user2.account.withdraw(56)
user2.account.withdraw(12)
user2.account.display_acc_info()
user3.account.deposit(4456)
user3.account.withdraw(234)
user3.account.withdraw(100)
user3.account.withdraw(676)
user3.account.display_acc_info()







        
        










