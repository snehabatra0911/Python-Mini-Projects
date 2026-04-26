print("Welcome to ATM System")
from account import Account
from atm_operations import *

my_account = Account()

while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Thank you for using ATM")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance(my_account)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        deposit_money(my_account, amount)

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        withdraw_money(my_account, amount)

    elif choice == "4":
        show_transactions(my_account)

    elif choice == "5":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice, try again")
