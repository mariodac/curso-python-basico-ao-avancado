from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency:int, account_number:int, balance:float=0) -> None:
        self._agency = agency
        self._account_number = account_number
        self._balance = balance

    # metodo sacar
    @abstractmethod
    def withdraw_money(self, value_cash: float) -> float: ...

    # metodo depositar
    def cash_deposit(self, value_cash:float) -> float: 
        self._balance += value_cash
        self.details(f'Foi realizado o depósito de R$ {value_cash:.2f}')
        return self._balance

    def details(self, msg: str='') -> None: 
        if self._balance < 0:
            print('O seu saldo está negativo')
        print(f'Você possui um saldo de: R$ {self._balance:.2f} --- {msg}')
        print('-' * 80)


class SavingAccounts(Account):
    def withdraw_money(self, value_cash: float) -> float: 
        pos_balance = self._balance - value_cash
        if pos_balance < 0:
            self.details(f'Saldo insuficiente. Saque negado R$ {value_cash:.2f}')
            return self._balance
        self._balance -= value_cash
        self.details(f'Foi realizado o saque de R$ {value_cash:.2f}')
        return self._balance


class CheckingAccounts(Account):
    def __init__(self, agency : int, account_number: int, balance: float = 0, limit: float = 0):
        super().__init__(agency, account_number, balance)
        self._limit = limit
    def withdraw_money(self, value_cash: float) -> float:
        pos_balance = self._balance - value_cash
        if pos_balance < -self._limit:
            self.details(f'Estourou o limite. Saque negado R$ {value_cash:.2f}')
            print(f'Seu limite é: R$ {self._limit:.2f}')
            return self._balance
        self._balance -= value_cash
        self.details(f'Foi realizado o saque de R$ {value_cash:.2f}')
        return self._balance

if __name__ == '__main__':
    saving_account = SavingAccounts(111, 333)
    saving_account.withdraw_money(1)
    saving_account.cash_deposit(1000)
    saving_account.withdraw_money(1001)
    print('#'*80)
    checking_account = CheckingAccounts(111, 333,0, 300)
    checking_account.withdraw_money(1)
    checking_account.withdraw_money(1000)
    checking_account.withdraw_money(1001)
    print('#'*80)