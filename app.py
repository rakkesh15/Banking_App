class Bank:
    total_bal = 0  # Class Variable
    cust_list = []  # Class Variable

    def _init_(self, name, acc_num, ini_bal=1000):
        self.name = name
        self.acc_num = acc_num
        self.ini_bal = ini_bal


class Saving(Bank):
    def _init_(self, name, acc_num, pan_num, balance=0, ini_bal=1000):
        super()._init_(name, acc_num, ini_bal)
        self.pan_num = pan_num
        self.balance = balance + ini_bal
        print(f"Hello Mr. {self.name}, you have successfully created an account with HDFC Bank.")
        print(f"Your available balance is now {self.balance}")
        Bank.total_bal += self.balance
        Bank.cust_list.append(self.name)

    def deposit(self, money):
        self.balance += money
        Bank.total_bal += money
        print(f"Hello Mr. {self.name}, you have deposited {money} in your account.")
        print(f"Your available balance is {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= money
            Bank.total_bal -= money
            print(f"Hello Mr. {self.name}, you have withdrawn {money} from your account.")
            print(f"Your remaining balance is {self.balance}")

    def check_balance(self):
        print(f"Hello Mr. {self.name}, your available balance is {self.balance}")

    def _del_(self):
        print("Closing your account in a few seconds....")


def main():
    accounts = {}
    while True:
        print("\n*** HDFC Bank Console App ***")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            acc_num = input("Enter account number: ")
            pan_num = input("Enter PAN number: ")
            accounts[acc_num] = Saving(name, acc_num, pan_num)
        elif choice == "2":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[acc_num].deposit(amount)
            else:
                print("Account not found!")
        elif choice == "3":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[acc_num].withdraw(amount)
            else:
                print("Account not found!")
        elif choice == "4":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                accounts[acc_num].check_balance()
            else:
                print("Account not found!")
        elif choice == "5":
            print("Thank you for using HDFC Bank. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "_main_":
    main()