class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
print("Balance:", acc.get_balance())
acc.deposit(500)
print("Balance:", acc.get_balance())
acc.withdraw(300)
print("Balance:", acc.get_balance())  # Outputs: Balance: 1200
