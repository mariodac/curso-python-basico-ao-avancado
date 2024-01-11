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
while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Você deve digitar apenas uma letra!')
        continue
    elif len(letra) == 0:
        print('Você deve digitar apenas uma letra!')
        continue
    else:
        tentativas += 1
        if letra in palavra_secreta:
            letra_acertadas += letra
            astericos = 0
            for letra_secreta in palavra_secreta:
                if letra_secreta in letra_acertadas:
                    print(letra_secreta, end='')
                else:
                    astericos += 1
                    print('*', end='')
            print('')
            if astericos == 0:
                print('Parabéns, você ganhou!')
                print(f'A palavra secreta é "{palavra_secreta}"')
                print(f'Numero de tentivas: {tentativas}')
                sair = input('Deseja sair? (S)im =>')
                if (sair.lower() == 's') or (sair.lower() == 'sim'): break
                if os_name() == 'Windows':
                    system('cls')
                else:
                    system('clear')
                tentativas = 0
                letra_acertadas = ''
                
        else:
            continue


