class BankAccount:

    @classmethod
    def print(cls):
        print(cls)

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
        return self



account_a = BankAccount(0.01, 100)
account_a.deposit(100).deposit(50).deposit(75).yield_interest().display_account_info()


account_b = BankAccount(0.05, 500)
account_b.deposit(80).deposit(175).withdraw(2).withdraw(4).withdraw(6).withdraw(6).yield_interest().display_account_info()