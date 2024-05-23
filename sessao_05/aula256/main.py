from accounts import SavingAccounts, CheckingAccounts
from people import Client
from bank import Bank
from random import choice, randint

def only_int(input_str:str) ->int:
    while True:
        try:
            return int(input_str)
        except ValueError:
            print("Digite apenas numeros")
            input_str = input('Digite a idade => ')

option = -1
bank = Bank()
bank.agencies.extend([111, 222, 333, 444, 555, 666])
while option != 0:
    print('#'*80)
    print('1 - Criar Cliente')
    print('2 - Criar Conta')
    print('3 - Depositar')
    print('4 - Sacar')
    print('0 - Sair')
    option = only_int(input('Escolha uma opção => '))
    if option == 1:
        name = input('Digite o nome do cliente => ')
        age = only_int(input('Digite a idade => '))
        client = Client(name, age)
        bank.clients.append(client)
    elif option == 2:
        for index, client_item in enumerate(bank.clients):
            print(f'{index+1} - {client_item.name}')
        client_index = only_int(input('Escolha o cliente => '))
        if client_index-1 in [x for x in range(len(bank.clients))]:
            print('1 - Conta Corrente\n2 - Conta Poupança')
            type_account = only_int(input('Digite o tipo da conta => '))
            if type_account in [1, 2]:
                if type_account == 1:
                    agency = choice(bank.agencies)
                    account_number = randint(1, 1000)
                    account = CheckingAccounts(agency,  account_number, limit=100)
                    bank.clients[client_index]._account = account
                elif type_account == 2:
                    agency = choice(bank.agencies)
                    account_number = randint(1, 1000)
                    account = SavingAccounts(agency, account_number)
                    bank.clients[client_index]._account = account
                bank.accounts.append(account)
            else:
                print('Opção inválida')
        else:
            print('Cliente não encontrado')

    elif option == 3:
        for index, client_item in enumerate(bank.clients):
            print(f'{index+1} - {client_item.name}')
        client_index = only_int(input('Digite o numero do cliente => '))
        if client_index-1 in [x for x in range(len(bank.clients))]:
            value = only_int(input('Digite o valor a depositar =>'))
            bank.clients[client_index]._account.cash_deposit(value)
    elif option == 4:
        ...