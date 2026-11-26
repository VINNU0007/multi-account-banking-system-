class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print("\n======ACCOUNT DETAILS======")
        print("Account holder:", self.account_holder)
        print("Account number:", self.account_number)
        print("Current balance:", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount should be greater than zero")
        else:
            self.balance += amount
            print("Deposit successfull")
            print("Updated balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount should be greater than zero")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print("Withdraw Successfull")
            print("Current balance:", self.balance)

    def check_balance(self):
        print("\nAvailable balance:", self.balance)


def create_account(accounts):
    acc_num = input("Enter New Account Number: ").strip()

    if not acc_num:
        print("Account number cannot be empty.")
        return
        
    if acc_num in accounts:
        print(f"Account #{acc_num} already exists for {accounts[acc_num].account_holder}.")
        return
        
    name = input("Enter Account Holder name: ").strip()

    if not name:
        print("Account holder name cannot be empty.")
        return
    
    new_account = BankAccount(name, acc_num)
    accounts[acc_num] = new_account
    print(f"Account created successfully for {name} (#{acc_num})!")

def find_account(accounts):
    acc_num = input("Enter Account number: ").strip()

    if not  acc_num:
        print("Account number cannot be empty.")
        return None
    account = accounts.get(acc_num)

    if account is None:
        print(f"Account #{acc_num} not found. please create an account first.")
        return None
    return account

def main():
    print("===================================")
    print("   BANK ACCOUUNT APPLICATION       ")
    print("===================================")

    accounts = {}

    while True:
        print("\n====== MAIN MENU ======")
        print("1. Create New Account")
        print("2, View All Account Holders")
        print("3. Display Account Details")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Check balance")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            if not accounts:
                print("\nNo accounts in the bank yet.")
            else:
                print("\n----- All Account Holders -----")
                for acc in accounts.values():
                    print(
                        f"Name: {acc.account_holder} | "
                        f"Acc No: {acc.account_number} | "
                        f"Balance: {acc.balance}"
                    )

        elif choice == "3":
            account = find_account(accounts)
            if account:
                account.display_details()

        elif choice == "4":
            account = find_account(accounts)
            if account:
                try:
                    amount = float(input("Enter Deposit Amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "5":
            account = find_account(accounts)
            if account:
                try: 
                    amount = float(input("Enter Withdrawal Amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("enter a valid number.")
        elif choice == "6":
            account = find_account(accounts)
            if account:
                account.check_balance()
        elif choice == "7":
            print("Thank you for using our banking application!")
            break 
        else:
            print("Invalid choice. Please try again🔁.")

if __name__ == "__main__":
    main()