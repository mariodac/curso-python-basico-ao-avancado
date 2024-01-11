"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
from os import system
from platform import system as os_name

palavra_secreta = 'python'
letra_acertadas = ''
tentativas = 0
maximo_tentativas = len(palavra_secreta) * 4
tentativas_restantes = maximo_tentativas
dica_index = 0
dicas = ['é uma linguagem de programação', 'foi criado por um programador holandês', 'foi influenciado pela linguagem C', 'possui o nome de animal', 'é uma linguagem interpretada', 'é uma linguagem multiparadigma', 'linguagem possui tipagem dinamica e forte']
while True:
    print(f'Você possui {tentativas_restantes} tentativas restantes')
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Você deve digitar apenas uma letra!')
        continue
    elif len(letra) == 0:
        print('Você deve digitar apenas uma letra!')
        continue
    else:
        tentativas += 1
        tentativas_restantes -=  1
        if letra in palavra_secreta:
            letra_acertadas += letra
            palavra_formada = ''
            for letra_secreta in palavra_secreta:
                if letra_secreta in letra_acertadas:
                    palavra_formada += letra_secreta
                else:
                    palavra_formada += '*'
            print(palavra_formada)
            if palavra_formada == palavra_secreta:
                if os_name() == 'Windows':
                    system('cls')
                else:
                    system('clear')
                print('Parabéns, você ganhou!'.upper())
                print(f'A palavra secreta é "{palavra_secreta}"')
                print(f'Numero de tentivas: {tentativas}')
                sair = input('Deseja sair? (S)im =>')
                if (sair.lower() == 's') or (sair.lower() == 'sim'): break
                tentativas = 0
                letra_acertadas = ''
                maximo_tentativas = len(palavra_secreta) * 4
                tentativas_restantes = maximo_tentativas
                dica_index = 0
        
        elif tentativas == maximo_tentativas:
            if os_name() == 'Windows':
                system('cls')
            else:
                system('clear')
            print('Você perdeu!')
            print(f'A palavra secreta é "{palavra_secreta}"')
            print(f'Numero de tentativas: {tentativas}')
            sair = input('Deseja sair? (S)im =>')
            if (sair.lower() =='s') or (sair.lower() =='sim'): break
            tentativas = 0
            letra_acertadas = ''
            maximo_tentativas = len(palavra_secreta) * 4
            tentativas_restantes = maximo_tentativas
            dica_index = 0
        else:
            if tentativas % 2 == 0:
                if dica_index == len(dicas):
                    print('Você esgotou todas as dicas'.upper())
                else:
                    print('Aqui vai uma dica:')
                    print(f'{dicas[dica_index].upper()}')
                    dica_index += 1
            continue