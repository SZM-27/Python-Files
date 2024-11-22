# Define the BankAccount class
class BankAccount:
    def __init__(self, owner, balance):
        # Raise ValueError if owner's name is less than 10 characters
        if len(owner) < 10:
            raise ValueError("Owner's name must be at least 10 characters.")
        # Raise ValueError if the balance is negative
        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.owner = owner
        self.balance = balance
        self.transactions = []

    # Method to summarize the account holder and balance
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: ${self.balance}"

    # Deposit method
    def deposit(self, amount):
        # Raise ValueError if deposit amount is less than $1
        if amount < 1:
            raise ValueError("Deposit amount must be at least $1.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")

    # Method to display the current balance
    def display_balance(self):
        return f"Current balance: ${self.balance}"

    # Method to display all transactions
    def display_transactions(self):
        return self.transactions
