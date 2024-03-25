def calcular_preco_final(preco_original, desconto_percentual):
    preco_final = preco_original * (1 - desconto_percentual / 100)
    return preco_final

# Solicita ao usuário o preço original do produto e o desconto percentual
preco_original = float(input("Digite o preço original do produto: R$ "))
desconto_percentual = float(input("Digite o desconto percentual (%): "))

# Chama a função para calcular o preço final após o desconto
preco_final = calcular_preco_final(preco_original, desconto_percentual)

# Imprime o preço final após o desconto
print(f"O preço final do produto após o desconto é: R$ {preco_final:.2f}")
