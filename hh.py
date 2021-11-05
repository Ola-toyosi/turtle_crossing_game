# 1. balance
# 2. withdraw
# 3. deposit

# data
# Account type
# account number
# account name
# pin
# balance

# create dictionary
# collect account type
# -(if)
# collect account number and verify
# return account name

account_db = {
    '2367890451': {'account_type': 'savings', 'account_name': 'James Green', 'pin': '1978', 'balance': 478000},
    '2367546731': {'account_type': 'current', 'account_name': 'Kate West', 'pin': '1424', 'balance': 630000},
    '2367884209': {'account_type': 'current', 'account_name': 'Jesse Johnson', 'pin': '8009', 'balance': 28000},
    '2367755200': {'account_type': 'savings', 'account_name': 'Ali Dakari', 'pin': '2133', 'balance': 156000}
}

trial = 0


def trials(trial):
    while True:
        trial += 1
        if trial == 3:
            print('You have reached maximum amount of attempts(3)')
            break


def check_account_type():
    if account_type == account_db[account_no]['account_type']:
        return True
    else:
        print("Records don't match! Try again")
        trials(trial)


def transactions():
    while True:
        req = input(
            'Select a transaction to perform:\n0. Exit\n1. Check Account Balance\n2. Withdraw money\n3. Deposit Money')

        if req == '0':
            break
        elif req == '1':
            show_balance()

        elif req == '2':
            withdraw()

        elif req == '3':
            deposit()

        else:
            print('Invalid option! Try again!')
            trials(trial)


def show_balance():
    account_name = account_db[account_no]['account_name']
    account_balance = account_db[account_no]['balance']
    print('Account Name \tAccount Number Account Balance')
    print(f'{account_name} \t{account_no}\t{account_balance}')


def withdraw():
    withdraw_amt = int(input('How much would you like to withdraw?\n: '))
    account_balance = account_db[account_no]['balance']
    if withdraw_amt > account_balance:
        print('Insufficient Money! Try again')
    else:
        account_db[account_no]['balance'] -= withdraw_amt
        account_balance = account_db[account_no]['balance']
        print(f"Here's your money! #{withdraw_amt}")
        print(f"Your account balance is #{account_balance}")


def deposit():
    deposit_amt = int(input('How much would you like to deposit?\n: '))
    account_db[account_no]['balance'] += deposit_amt
    account_balance = account_db[account_no]['balance']
    print(f'#{deposit_amt} successfully deposited\nNew account balance: {account_balance} ')


while True:
    account_no = input('Welcome to Heritage Bank\nEnter account number(0 to cancel): ')

    if account_no in account_db:

        account_name = account_db[account_no]['account_name']
        print(f" Hello {account_name}!")

        pin_entry = input('Enter pin: ')

        if pin_entry == account_db[account_no]['pin']:

            account_type = input('Select account type\n0. Exit\n1. Savings\n2. Current: ')

            if account_type == '0':
                exit()

            elif account_type == '1':
                account_type = 'savings'
                check_account_type()
                transactions()

            elif account_type == '2':
                account_type = 'current'
                check_account_type()
                transactions()

            else:
                print("Invalid choice! Try again")
                trial += 1
                if trial == 3:
                    print('You have reached maximum amount of attempts(3)')
                    break

        else:
            print('Wrong pin! Try again')
            trial += 1
            if trial == 3:
                print('You have reached maximum amount of attempts(3)')
                break

    elif account_no == '0':
        break

    else:
        break
