import re

def validate_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub('[^0-9]', '', cpf)
    if not cpf or len(cpf) != 11:
        return False
    new_cpf = cpf[:-2] # Elima os dois últimos digitos do CPF
    reverse = 10 # Contador reverso
    total = 0

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

    # Evita sequencias. Ex.: 11111111111, 00000000000, ....
    sequence = new_cpf == str(new_cpf[0] * len(cpf))

    if cpf == new_cpf and not sequence:
        return True
    else:
        return False




