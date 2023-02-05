
a = input()
b = int(input())

class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposite(self, sum):
        self.balance += sum
        print( "Balance", self.balance)
    def withdraw(self, sum):
        if sum > self.balance:
            print("Withdrawal declined, insufficient funds")
        else:
            self.balance -= sum
            print( "New balance", self.balance)

acc = Account(a,b)

acc.deposite(500)
acc.withdraw(2000)
acc.withdraw(300)

