class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited. New balance is Rs.", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited. New balance is Rs.", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account("1234567890", 1000)

acc1.debit(200) 
acc1.credit(500)

