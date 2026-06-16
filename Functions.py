from storage import all_accounts

def FindAccountNumber(acc_number):
    for account in all_accounts:
        if acc_number == account.account_number:
           return account
    return None