"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
cpf_usuario = input("CPF -> ")
cpf_formatado = cpf_usuario.replace('-', '').replace('.', '').strip()

soma = 0
multiplicador = 10
resultado_multiplicado = 0

try:
    for digito in cpf_formatado:
        digito_int = int(digito)
        soma += digito_int * multiplicador
        multiplicador -= 1
        if multiplicador < 2:
            break
    resultado_multiplicado = soma * 10

    primeiro_digito = resultado_multiplicado % 11
    primeiro_digito = primeiro_digito if primeiro_digito < 9 else 0

    print(f"Primeiro digito: {primeiro_digito}")

    multiplicador = 11
    soma = 0
    for digito in cpf_formatado:
        digito_int = int(digito)
        soma += digito_int * multiplicador
        multiplicador -= 1
        if multiplicador < 3:
            break
    soma += primeiro_digito * multiplicador 
    
    segundo_digito = (soma * 10) % 11
    segundo_digito = segundo_digito if segundo_digito < 9 else 0

    print(f"Segundo digito: {segundo_digito}")

    cpf_gerado = f'{cpf_formatado[:9]}{primeiro_digito}{segundo_digito}'
    if cpf_gerado == cpf_formatado:
        print("CPF válido")
    else:
        print("CPF inválido")
except ValueError:
    print("Digito invalido")