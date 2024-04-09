"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('SE condição desejada ENTÃO faça algo')
else:
    print('SENÃO ENTÃO faça outra coisa')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')