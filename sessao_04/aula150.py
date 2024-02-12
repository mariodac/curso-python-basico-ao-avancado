# Try, except, else e finally

try:
    a = 18
    b = 0
    # print(d)
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print('Não é possível dividir por zero!')
except NameError:
    print('A variável não existe!')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('Erro desconhecido!')