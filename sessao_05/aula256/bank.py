from people import Client
from accounts import Account, SavingAccounts, CheckingAccounts

class Bank:
    def __init__(self, accounts:list[Account]|None=None, clients:list[Client]|None=None, agencies: list[int]|None=None):
        self.accounts = accounts or []
        self.clients = clients or []
        self.agencies = agencies or []

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.agencies!r}, {self.clients!r}, {self.accounts!r})'
        return f'{class_name}{attrs}'

    def _check_accounts(self, account:Account):
        if account in self.accounts:
            return True
        return  False

    def _check_clients(self, client:Client):
        if client in self.clients:
            return True
        return False

    def _check_agency(self, account:Account):
        if account._agency in self.agencies:
            return True
        return False
    
    def _check_account_client(self, client:Client, account:Account):
        if client._account is account:
            return True
        return False

    def authenticate(self, client:Client, account:Account):
        return self._check_accounts(account) and self._check_clients(client) and self._check_agency(account) and self._check_account_client(client, account)
        

if __name__ == '__main__':
    saving_account = SavingAccounts(111, 333, 2000)
    checking_accounts = CheckingAccounts(222,333, 100, 1000)
    client1 = Client('Mario', 29, saving_account)
    client2 = Client('João', 39, checking_accounts)
    bank = Bank()
    bank.clients.extend([client1, client2])
    bank.accounts.extend([checking_accounts, saving_account])
    bank.agencies.extend([111, 222, 333])
    if bank.authenticate(client1, saving_account):
        saving_account.cash_deposit(100)