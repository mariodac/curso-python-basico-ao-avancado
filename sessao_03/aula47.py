"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome ")
while True:
    try:
        idade = int(input("Digite a sua idade "))
        break
    except:
        print("Digite um numero")
if nome and idade:
    print(f'Seu nome é {nome}')
    nome_invertido = nome[::-1]
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f"Seu nome tem {len(nome.strip())} letras")
    ultima_letra = nome[-1]
    print(f"A última letra do seu nome é {ultima_letra}")
    print(f"Sua idade em hexadecimal é {int(idade):X}")
else:
    print("Desculpe, você deixou campos vazios.")