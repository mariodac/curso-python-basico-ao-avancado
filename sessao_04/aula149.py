# Try, except, else e finally

try:
    a = 18
    b = 0
    # print(d)
    print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except NameError:
    print('A variável não existe!')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:
    print('Erro desconhecido!')