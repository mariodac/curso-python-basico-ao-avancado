from account import SavingAccounts, CheckingAccounts

class Person:
    def __init__(self, name:str, age:int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name:str):
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age:int):
        self._age = age

class Client(Person):
    def __init__(self, name:str, age:int, account:SavingAccounts|CheckingAccounts) -> None:
        super().__init__(name, age)
        self._account = account


if __name__ == '__main__':
    # saving_account = 'Str'
    saving_account = SavingAccounts(111, 333)
    # saving_account.cash_deposit(1000)
    # saving_account.withdraw_money(1)
    client = Client('Mario', 29, saving_account)

    

