# Classes decoradoras (Decorator classes)

class Multiple:
    # def __init__(self, func) -> None:
    #     self.func = func
    #     self._z = 10

    def __init__(self, z) -> None:
        self._z = z

    def __call__(self, func):
        def interna(*args, **kwargs):
            result = func(*args, **kwargs) 
            return result * self._z
        return interna

    # def __call__(self, *args, **kwargs):
    #     result = self.func(*args, **kwargs) 
    #     return result * self._z
    ...
@Multiple(10)
def sum_x_y(x, y):
    return x + y



one_two = sum_x_y(1, 2)
print(one_two)