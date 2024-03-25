def calcular_preco_total():
    preco_total = 0  # Variável para armazenar o preço total
    
    while True:
        try:
            preco = float(input("Digite o preço da fruta (ou 0 para encerrar): "))
            if preco == 0:
                break  # Encerra o loop quando o usuário digitar 0
            elif preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
                continue  # Volta para o início do loop

            preco_total += preco  # Adiciona o preço da fruta ao preço total
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    return preco_total

# Função principal para executar o programa
def main():
    print("=== Calculadora de Preço Total de Frutas ===")
    preco_total = calcular_preco_total()

    # Imprime o preço total das frutas
    print(f"O preço total das frutas é: R$ {preco_total:.2f}")

if __name__ == "__main__":
    main()
