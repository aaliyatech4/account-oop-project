class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Rs.", amount, "was debited. New balance is Rs.", self.get_balance())
        else:
            print("Insufficient balance!")

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited. New balance is Rs.", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account("1234567890", 1000)

transaction = input("Enter transaction (debit/credit): ").lower()
amount = int(input("Enter amount: "))

if transaction == "debit":
    acc1.debit(amount)

elif transaction == "credit":
    acc1.credit(amount)

else:
    print("Invalid transaction")

