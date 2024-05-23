from accounts import SavingAccounts, CheckingAccounts

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

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'

class Client(Person):
    def __init__(self, name:str, age:int, account:SavingAccounts|CheckingAccounts|None = None) -> None:
        super().__init__(name, age)
        if account is not None:
            self._account = account



if __name__ == '__main__':
    # saving_account = 'Str'
    saving_account = SavingAccounts(111, 333)
    # saving_account.cash_deposit(1000)
    # saving_account.withdraw_money(1)
    client = Client('Mario', 29, saving_account)
    print(saving_account)

    

