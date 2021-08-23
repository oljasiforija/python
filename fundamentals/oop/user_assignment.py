user1 = {'first_name': 'Michael', 'last_name': 'Michaelson','email':'michaelemail@gmail.com'}
user2 = {'first_name': 'Brad', 'last_name': 'Pitt', 'email':'bradpitt@gmail.com'}
user3 = {'first_name': 'Jane', 'last_name': 'Doe', 'email':'janedoe@gmail.com'}


class User():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{first_name} {last_name}"
        self.account_balance = 0
        self.email = email
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def deposit(self, amount):
        self.account_balance += amount
    def display_user_balance(self):
        print(f"User:{self.name} Balance:${self.account_balance}")


user1 = User('Michael','Michaelson','michaelemail@gmail.com')
user2 = User('Brad','Pitt','bradpitt@gmail.com')
user3 = User('Jane','Doe','janedoe@gmail.com')

user1.make_withdrawal(100)
user1.deposit(200)
user1.deposit(700)
user1.deposit(400)
user1.display_user_balance()
user2.deposit(230)
user2.deposit(234)
user2.make_withdrawal(56)
user2.make_withdrawal(12)
user2.display_user_balance()
user3.deposit(4456)
user3.make_withdrawal(234)
user3.make_withdrawal(100)
user3.make_withdrawal(676)
user3.display_user_balance()







        
        

