class Bank_accouunt:

    def __init__(self, account_holder, account_number, balance=0):

        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print("Name:", self.account_holder)
        print("Number:", self.account_number)
        print("Amount:", self.balance)

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount should be greater than zero📈")

        else:
            self.balance += amount
            print("Deposited successfully₹✔")
            print("Updated balance:", self.balance)

    def withdraw(self, amount):

        if amount <= 0:
            print("Withraw amount should be greater than zero📈")

        elif amount > self.balance:
            print("Insufficient funds")

        else:
            self.balance -= amount
            print("Withdrawal successfull₹✔")
            print("Remaining balance:",self.balance)

    def check_balance(self):
        print("\n Available balance:", self.balance)

def main():

    print("====================================")
    print("     BANK ACCOUNT APPLICATION       ")
    print("====================================")

    name = input("Enter the account holder name: ").strip()
    account_number = input("Enter the account number: ").strip()

    if not name or not account_number:
        print("Details cannot be empty.")
        return 
    account = Bank_accouunt(name, account_number)

    while True:
        print("\n========OPTIONS========")
        print("1. Display account details")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            account.display_details()
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdraw amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            account.check_balance()
        elif choice == "5":
            print("Thank for using our bank system")
            break

        else:
            print("Invalid choice, please try again🔁")

if __name__ == "__main__":
    main()