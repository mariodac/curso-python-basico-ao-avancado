
#Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# função decoradora
def create_function(func):
    def inside(*args, **kwarg):
        print('Decorando ...')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwarg)
        print(f'O seu resultado foi {result}')
        print('Ok decorado')
        return result
    return inside

def reverse_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param must be a string')
check_param = create_function(reverse_string)
reverse = check_param('mario')
print(reverse)