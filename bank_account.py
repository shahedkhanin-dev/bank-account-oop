class BankAccount:
    def __init__(self, account_holder, account_number, pin, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number 
        self.__pin = pin
        self.balance = balance
    
    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited successfully."
        else:
            return "Invalid deposit amount."
        
    def withdraw(self,amount):
        if amount<=0:
            return "Invalid withdrawal amount."
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"${amount} withdrawn successfully."
        
#  -----------------------main program ------------------------
account = BankAccount(
    account_holder="Nishinoya Yuu",
    account_number="1234567890",
    pin=1234,
    balance=5000
)

print("===== Welcome to Bank Account System =====")

entered_pin = int(input("Enter PIN: "))

if account.verify_pin(entered_pin):
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(f"Balance: ₹{account.check_balance()}")

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            print(account.deposit(amount))

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))
            print(account.withdraw(amount))

        elif choice == 4:
            print("Thank you for banking with us ")
            break

        else:
            print("Invalid choice")

else:
    print("Incorrect PIN ")