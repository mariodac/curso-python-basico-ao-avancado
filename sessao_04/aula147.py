# Introdução as Generator functions em Python
# generator = (n for n in range(10000))

def generator(n=0):
    yield 1 #Pausar
    print('Continuando ...')
    yield 2 #Pausar
    print('Mais uma ...')
    yield 3 #Pausar
    print('Vou terminar')
    return 'ACABOU'

def other_generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum: 
            return

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
other_gen = other_generator(maximum=100)
for n in other_gen:
    print(n)