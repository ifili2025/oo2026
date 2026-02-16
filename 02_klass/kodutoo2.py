class BankAccount:    
    def __init__(self, owner_name, initial_balance):
        self.owner = owner_name
        self.balance = initial_balance
        self.transactions = []
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return f"Balance: {self.balance}"
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("withdraw", amount))
            return f"Balance: {self.balance}"
        else:
            return f"{self.owner} teie kontol puudub piisavalt raha"
    def showBalance(self):
        return f"{self.owner} teie balansil on: {self.balance}EUR"
    def showHistory(self):
        return self.transactions

account1 = BankAccount("Igor", 1000)
acoount2 = BankAccount("Muhamet", 2000)


print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.withdraw(2000))
print(account1.showBalance())
print(account1.showHistory())

print(acoount2.deposit(1000))
print(acoount2.withdraw(500))
print(acoount2.showBalance())
print(acoount2.showHistory())
