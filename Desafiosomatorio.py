def somatorio(n):
    if n <= 0:
        return []
    
    numeros = list(range(1, n+1))  # Cria uma lista de 1 até n
    soma = sum(numeros)            # Calcula o somatório da lista
    return numeros, soma           # Retorna a lista e o somatório

# Exemplo de uso da função
numero = 15
lista_numeros, resultado_somatorio = somatorio(numero)

print(f"A lista de números até {numero} é: {lista_numeros}")
print(f"O somatório dos números até {numero} é: {resultado_somatorio}")
