# Decoradores com parâmetros

def params_decorator(nome):
    def decorator(func):
        print('Decorador:', nome)

        def new_function(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return new_function
    return decorator



@params_decorator(nome='5')
@params_decorator(nome='4')
@params_decorator(nome='3')
@params_decorator(nome='2')
@params_decorator(nome='1')
def sum_x_y(x, y):
    return x + y

sum_ten_five = sum_x_y(10, 5)
print(sum_ten_five)