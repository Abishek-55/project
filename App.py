from storage import all_accounts
from Functions import FindAccountNumber

from ExceptionHandeling import Bank
from BankClass import DepositError, WithdrawError
def main():   
    while True:
        print('-'*80)
        print('Welcome to Bank application')
        print('-'*30)
        print("1. Create Account")
        print('2. Deposit Amount')
        print('3. Withdraw Amount')
        print('4. Show Details')
        print('5. EXIT')


        try:
            choice=int(input("Enter your choice (1 - 5)"))

            if choice == 1:
                yn=input('Do you really want to create account? (y/n): ').lower()
                if yn == 'y':
                    name = input('Enter customers full name: ')
                    init_balance = int(input("Enter initial Balance: "))
        
                    if init_balance > 100:
                        b=Bank(name, init_balance)
                        all_accounts.append(b)
                        print(f'Account created with name: {name} and account number {b.account_number}')
                        print(f"Rs. {init_balance} deposited to A/C no. {b.account_number}")
        
                    else:
                        print('Initial deposit balance must be more than 100.')
                elif yn == 'n':
                    print ("Continue with your transaction")
                    
                else:
                    print("Enter only y/n")

                    
            elif choice == 2:
                yn=input('Do you really want to find Account Number? (y/n): ').lower()

                if yn == 'y':
                    acc_number = input("Enter your Account Number: ")
                    find_acc=FindAccountNumber(acc_number)
        
                    if find_acc:  # if find_acc has any value
                        amount = int(input("Enter deposit amount"))
                        try:
                            find_acc.deposit(amount)
                        except DepositError as e:
                            print (e)
                    else:
                        print("No account found with provided account number")
                elif yn == 'n':
                    print ("Continue with your transaction")
                    
                else:
                    print("Enter only y/n")

                
                        

            elif choice == 3:
                yn=input('Do you really want to withdraw amount? (y/n): ').lower()
                
                if yn == 'y':
                    acc_number = input("Enter your Account Number: ")
                    find_acc=FindAccountNumber(acc_number)
        
                    if find_acc:  # if find_acc has any value
                        amount = int(input("Enter withdraw amount: "))
                        try:
                            find_acc.withdraw(amount)
                        except DepositError as e:
                            print (e)
                    else:
                        print("No account found with provided account number")
                elif yn == 'n':
                    print ("Continue with your transaction")
                    
                else:
                    print("Enter only y/n")





                
            elif choice == 4:

                yn=input('Do you really want to withdraw amount? (y/n): ').lower()
                if yn == 'y':
                    acc_number = input("Enter your Account Number: ")
                    find_acc=FindAccountNumber(acc_number)

                    if find_acc:
                        find_acc.show_details()

                    else:
                        print("No account found with provided account number")

                elif yn == 'n':
                    print ("Continue with your transaction")

                else:
                    print("Enter only y/n")


                
                
                
            elif choice == 5:
                break
            else:
                print('Invalid Output')

        except ValueError:
            print('Error: Please enter only value from 1 to 5. \n')