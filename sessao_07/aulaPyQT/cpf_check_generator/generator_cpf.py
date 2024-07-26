from random import randint

def generate_cpf():
    number = str(randint(100000000, 999999999))

    new_cpf = number    # 9 numeros aleatórios
    reverse = 10    # contador reverso
    total = 0   # o total das multiplicações


    for index in range(19):
        if index > 8:       # Primeiro indice vai de 0 a 9
            index -= 9      # São os 9 primeiros digitos do CPF

        total += int(new_cpf[index]) * reverse # Valor total da multiplicação
        
        reverse -= 1        # Decrementa o contador reverso
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:   # se o digito for > que 9 o valor é 0
                d = 0
            total = 0   # Zera o total
            new_cpf += str(d)  # Concatena o digito gerado no novo cpf
    
    return new_cpf
