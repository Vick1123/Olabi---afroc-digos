def remover_duplicatas(lista):
    # Converte a lista para um conjunto para remover duplicatas
    conjunto_sem_duplicatas = set(lista)
    # Converte o conjunto de volta para uma lista
    lista_sem_duplicatas = list(conjunto_sem_duplicatas)
    return lista_sem_duplicatas

# Lista de exemplo com duplicatas
lista_com_duplicatas = [1, 2, 3, 4, 2, 3, 5, 6, 1]

# Chama a função para remover as duplicatas
lista_sem_duplicatas = remover_duplicatas(lista_com_duplicatas)

# Imprime a lista resultante sem duplicatas
print("Lista original com duplicatas:", lista_com_duplicatas)
print("Lista sem duplicatas:", lista_sem_duplicatas)
