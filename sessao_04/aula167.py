# Decoradores com parâmetros

def make_decorators(a=None, b=None, c=None):
    def make_functions(func):
        print('Decoradora 1')

        def nested(*args, **kwargs):
            print('Parâmetros do decorador', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return nested
    return make_functions



@make_decorators(1, 2, 3)
def sum_x_y(x, y):
    return x + y

multiply = make_decorators()(lambda x, y: x * y)

sum_ten_five = sum_x_y(10, 5)
mult_ten_five = multiply(10, 5)
print(sum_ten_five)
print(mult_ten_five)