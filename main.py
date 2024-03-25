from calculadora import Calculadora

# Obtém os números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Cria uma instância da classe Calculadora
calc = Calculadora(num1, num2)

# Realiza as operações matemáticas e imprime os resultados com frases específicas
soma = calc.adicao()
print(f"O resultado da soma é: {soma}")

subtracao = calc.subtracao()
print(f"O resultado da subtração é: {subtracao}")

multiplicacao = calc.multiplicacao()
print(f"O resultado da multiplicação é: {multiplicacao}")

divisao = calc.divisao()
print(f"O resultado da divisão é: {divisao}")
