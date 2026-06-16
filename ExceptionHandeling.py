import random
import datetime

from BankClass import WithdrawError, DepositError


class Bank:
    def __init__(self, account_name, balance):
        self.account_name=account_name
        self.balance=balance
        self.account_number= "".join(str(random.randint(0,9)) for i in range(16))
        self.created_at=datetime.now()


    def deposit(self,amount):
        if amount >100:
            self.balance+=amount
            print(f'Rs.{amount} deposited to A/c no. {self.account_number}')
        else:
            raise DepositError('Deposit amount must be more than 100')
    def withdraw(self,amount):
        if amount>0:
            if amount < self.balance:
                self.balance-=amount
                print(f'Rs.{amount} has been withdrawn from A/c no. {self.account_number}')
            else:
                raise WithdrawError('Withdraw amount must be less than balance.')
        else:
            print("Withdrawn amount must be higher than 0")

    def show_details(self):
        print("Account Details")
        print ('-'*40)
        print ('-'*40)
        print(f'Account Name: {self.account_name}')
        print(f'Account Balance: {self.balance}')
        print(f'Account Number: {self.account_number}')
        print(f'Account Created at: {self.created_at}')
