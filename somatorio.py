# Função para calcular o somatório de dois números
def calcular_somatorio(num1, num2):
    soma = num1 + num2
    return soma

# Obtém os números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcula o somatório dos números informados
resultado_somatorio = calcular_somatorio(num1, num2)

# Imprime o resultado na tela
print(f"A soma de {num1} e {num2} é: {resultado_somatorio}")

