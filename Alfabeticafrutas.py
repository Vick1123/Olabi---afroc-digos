def ordenar_frutas(frutas):
    frutas.sort(key=str.lower)  # Ordena a lista de frutas de forma case-insensitive
    return frutas

# Lista de frutas
frutas = ["Maçã", "Banana", "abacaxi", "Pera", "uva"]

# Chama a função para ordenar as frutas
frutas_ordenadas = ordenar_frutas(frutas)

# Imprime a lista de frutas ordenadas
print("Lista de frutas ordenadas:", frutas_ordenadas)
