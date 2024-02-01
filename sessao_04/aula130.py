# Exemplo de uso do tipo set

letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra)

    if 'l' in letras:
        print('PARABÉNS')
    print(letras)