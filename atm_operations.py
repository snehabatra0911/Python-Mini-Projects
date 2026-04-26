def check_balance(account):
    print("Your balance is:", account.balance)


def deposit_money(account, amount):
    account.balance += amount
    account.transactions.append(f"Deposited {amount}")
    print("Money deposited successfully")


def withdraw_money(account, amount):
    if amount <= account.balance:
        account.balance -= amount
        account.transactions.append(f"Withdrew {amount}")
        print("Please collect your cash")
    else:
        print("Insufficient balance")


def show_transactions(account):
    if len(account.transactions) == 0:
        print("No transactions yet")
    else:
        print("Transaction History:")
        for t in account.transactions:
            print("-", t)