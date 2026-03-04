# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    print(num1 / num2)
else:
    print("Operador inválido")