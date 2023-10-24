class BankAccount:

    def __init__(self, int_rate, balance):
        self.interest = int_rate
        self.bal = balance

    def deposit(self, amount):
        self.bal += amount
        return self

    def withdraw(self, amount):
        if amount < self.bal:
            self.bal -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.bal -= 5
        return self

    def yield_interest(self):
        if self.bal > 0:
            self.bal += self.bal * self.interest
            return self

    def display_account_info(self):
        print("Balance $", self.bal)

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)


    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("Balance $", self.account.bal)
        return self



new_user = User("Judah", "judah.kahler1345@somemail.sniff")
new_user.make_deposit(10).make_withdrawl(5).display_user_balance()

# second_user = User("Bill", "Bob", "Blahblah@mail", 46)
# second_user.enroll().spend_points(80).display_info()


# third_user = User("Nigel", "Dill", "mail.mail.mail@mial.com", 99)