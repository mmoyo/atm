# This programe imitate the ATM Code
# User must First Deposit Amount before withdrawal
# First User is presented with a menu:
# D for deposit, B check balance, C exit transaction

def manual():
    print('''
Welcome to Bank ABDC ATM
==================================
To Use this ATM First Declare the amount in your bank
Enter W to withdraw your money
Enter C to Check your balance
''')

def options():
    input('''Please Enter : 
W to Withdraw Money
C to Check balance
Q to Quite the programe    
''')

def withdrawal():
    try:
        withdrawal_money = float(input('Please enter the money you want to withdraw '))

    except ValueError:
        print("Money can only be a number with decimal only")

    else:
        return withdrawal_money

def choice():
    optional=input("Please select Your Option : ")
    return optional

manual()
while True:
    try:
        amount_bank = float(input('Please enter the money in your account: '))

    except ValueError:
        print("Money can only be a number with decimal only")
    break

selection=choice()

if selection == 'W':
    amount_withdrawal = withdrawal()
    while amount_bank> amount_withdrawal:
            new_balance = amount_bank-amount_withdrawal
            print('''You have withdrew {} from your account
    Your new balance is {}
'''.format(amount_withdrawal,new_balance))
            break

    else:
            print("You have insufficient funds first deposit money in your account")
elif selection=='C':
        print("Your balance is ${} ".format(amount_bank))
        choice()
elif selection=='Q':
    print("Thank you for banking with us")
else:
    print(" You selected an Invalid Option")







