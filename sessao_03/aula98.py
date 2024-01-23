"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input("CPF -> ")
cpf_formatado = cpf.replace('-', '').replace('.', '').strip()

soma = 0
multiplacador = 10
resultado_multiplicado = 0

try:
    for digito in cpf_formatado:
        digito_int = int(digito)
        soma += digito_int * multiplacador
        multiplacador -= 1
        if multiplacador < 2:
            break
    resultado_multiplicado = soma * 10

    primeiro_digito = resultado_multiplicado % 11
    primeiro_digito = primeiro_digito if primeiro_digito < 9 else 0

    print(f"Primeiro digito: {primeiro_digito}")
except ValueError:
    print("Digito invalido")

