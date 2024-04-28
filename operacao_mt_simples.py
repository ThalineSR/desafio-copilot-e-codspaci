# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação que você deseja realizar (+, -, /, *):")

if operacao == '+':
    print(numero1 + numero2)
if operacao == '-':
    print(abs(numero1 - numero2))
if operacao == '/':
    print(numero1 / numero2)
if operacao == '*':
    print(numero1 * numero2)        
