import random

for _ in range(100):
    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))
    soma = 0
    multiplacador = 10


    for digito in nove_digitos:
        digito_int = int(digito)
        soma += digito_int * multiplacador
        multiplacador -= 1
        if multiplacador < 2:
            break

    primeiro_digito = (soma * 10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito < 9 else 0



    multiplicador = 11
    soma = 0
    for digito in nove_digitos:
        digito_int = int(digito)
        soma += digito_int * multiplicador
        multiplicador -= 1
        if multiplicador < 3:
            break
    soma += primeiro_digito * multiplicador 

    segundo_digito = (soma * 10) % 11
    segundo_digito = segundo_digito if segundo_digito < 9 else 0

    cpf_gerado = f'{nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:]}-{primeiro_digito}{segundo_digito}'
    cpf_gerado = f'{nove_digitos[:3]}{nove_digitos[3:6]}{nove_digitos[6:]}{primeiro_digito}{segundo_digito}'
    print(cpf_gerado)