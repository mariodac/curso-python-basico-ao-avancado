while True:
    num1 = input("Digite o primeiro numero => ")
    if num1.isdigit():
        numero1 = int(num1)
    else:
        print("Deve digitar um numero")
        continue
    num2 = input("Digite o segundo numero => ")
    if num2.isdigit():
        numero2 = int(num2)
    else:
        print("Deve digitar um numero")
        continue
    operadores_permitidos = ['+', '-', '/', '*']
    op = input("Digite a operador (+-*/) => ")
    if op in operadores_permitidos:
        if op == '+':
            resultado = numero1 + numero2
        elif op == '-':
            resultado = numero1 - numero2
        elif op == '*':
            resultado = numero1 * numero2
        elif op == '/':
            resultado = numero1 / numero2
        print(f"{numero1} {op} {numero2} = {resultado}")
    else:
        print("Operador invalida")
        continue
    sair = input("Deseja sair? ")
    "".lower()
    if sair.lower() == 's' or sair.lower() == 'sim':
        break
    else:
        continue