"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistente na lista
"""
import os
import platform
lista_compras = []
while True:
    opcao = input('Selecione uma opção \n[I]nserir\n[A]pagar\n[L]istar-> ')
    if opcao.upper() == 'I':
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        valor = input('Valor-> ')
        lista_compras.append(valor)
    elif opcao.upper() == 'A':
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        if len(lista_compras) > 0:
            indice = input('Escolha o indice para apagar-> ')
            try:
                indice = int(indice)
                lista_compras.pop(indice)
            except ValueError:
                print('Insira apenas numero inteiro'.upper())
            except IndexError:
                print('Indice inserido não existe'.upper())
            except:
                print('ERRO DESCONHECIDO')
        else:
            print('A lista está vazia'.upper())
            
    elif opcao.upper() == 'L':
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        if len(lista_compras) > 0:
            for indice, item in enumerate(lista_compras):
                print(indice, item)
        else:
            print('A lista está vazia'.upper())
    else:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        print('Opção não existe'.upper())
