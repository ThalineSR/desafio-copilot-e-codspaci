# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero_inteiro = int(input("Digite um número inteiro: "))

resultado = verificar_par_ou_impar(numero_inteiro)
print(f"O número {numero_inteiro} é {resultado}.")

