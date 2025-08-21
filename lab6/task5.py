class BankAccount:
    def __init__(self, name, balance=0):
        """Initialize account with name and balance"""
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance = {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance = {self.balance}")
    def check_balance(self):
        """Display current account balance"""
        print(f"Account Holder: {self.name}, Current Balance: {self.balance}")
name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(name, initial_balance)
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Exiting... Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
