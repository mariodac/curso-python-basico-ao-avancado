
texto = """
O Python é uma linguagem de programação multiparadigma.
Python foi criado por Guido van Rossum
""".lower()

i = 0 
mais_vezes = 0
letra_mais_vezes = ''
contar_letra_atual = 0
while i < len(texto):
    if texto[i] == ' ':
        i += 1
        continue
    contar_letra_atual = texto.count(texto[i])
    if  contar_letra_atual > mais_vezes:
        mais_vezes = contar_letra_atual
        letra_mais_vezes = texto[i]
    i += 1
print(f'Na frase {texto}. A letra que aparece mais vezes é "{letra_mais_vezes}", aparecendo no total {mais_vezes} vezes')
