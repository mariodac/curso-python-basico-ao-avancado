# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
    if d == 0: 
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def divide2(n, d):
    try:
        return n /d
    except ZeroDivisionError:
        return n

def deve_ser_numero(n):
    if not isinstance(n, (float, int)):
        tipo_n = type(n)
        raise TypeError(
            f'{n} deve ser int ou float'
            f'{tipo_n.__name__} enviado'
        )
    return True

def divide(n, d):
    deve_ser_numero(n)
    deve_ser_numero(d)
    nao_aceito_zero(d)
    return n / d

print(divide(1,'0'))