"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

input_usuario = input('Digite um número inteiro => ')

try:
    numero_inteiro = int(input_usuario)
    if numero_inteiro%2 == 0:
        print(f'{numero_inteiro} é número par')
    else:
        print(f'{numero_inteiro} é número impar')
except:
    print('Não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_informada = input('Informe a hora => ')

if hora_informada.isdigit():
    hora_inteiro = int(hora_informada)
    if hora_inteiro >= 0 and hora_inteiro <= 11:
        print('Bom dia')
    elif hora_inteiro >= 12 and hora_inteiro <= 17:
        print('Boa tarde')
    elif hora_inteiro >= 18 and hora_inteiro <= 23:
        print('Boa noite')
    else:
        print('Hora inválida')
else:
    print('Informe apenas a hora')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome => ')

if len(nome) > 1:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) == 5 or len(nome) == 6:
        print('Seu nome é normal')
    elif len(nome) >6:
        print('Seu nome é muito grande')