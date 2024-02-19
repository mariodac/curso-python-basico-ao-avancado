# Váriáveis livres + nonlocal
print(globals())

def out(x):
    a = x
    def inside():
        print(locals())
        # print(inside.__code__.co_freevars)
        return a
    return inside

inside1 = out(10)
inside2 = out(20)

print(inside1())
print(inside2())

def concat(init_string):
    final_value = init_string
    
    def inside(value_to_concat=''):
        nonlocal final_value
        final_value += value_to_concat
        return final_value
    return inside
    
c = concat('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
