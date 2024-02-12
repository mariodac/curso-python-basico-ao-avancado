# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO')
    # 8/0
except ZeroDivisionError as e:
    print('DIVIDIU ZERO')
    print(e.__class__.__name__)
    print(e)

except IndexError as error:
    print('INDEX ERROR')
except (NameError, ValueError):
    print('NameError, ValueError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')