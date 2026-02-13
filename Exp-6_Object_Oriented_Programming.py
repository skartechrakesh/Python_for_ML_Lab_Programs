class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Accept user input
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("Enter withdrawal amount: "))
        account.withdraw(amt)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
