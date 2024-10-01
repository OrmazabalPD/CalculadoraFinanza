
global_accounts_id = 0

def create_account(accounts, name, account_type):

    global global_accounts_id
    account ={
        "name": name,
        "type": account_type,
        "balance":0,
        "transactions":[]
    }

    accounts.append(account)
    global_accounts_id  += 1

    return accounts ['id']


def find_account_by_name (accounts, account_name):

    for account in accounts:
        if account['name'] == account_name:
            return account
    return None

def add_transactiion(accounts, description, account_name, amount):
    account = find_account_by_name(accounts, account_name) 
    if account:
        account['transactions'].append({"description":description,"amount":amount})
    else:
        print(f"La cuenta {account_name} no existe")
        
    
def calculate_transactions(account):
    return sum(transaction['amount'] for transaction in account ['transactions'])


def get_account_balance(accounts, account_name):