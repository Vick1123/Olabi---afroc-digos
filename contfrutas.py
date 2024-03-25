def contar_frutas(lista_frutas):
    # Dicionário para armazenar as contagens de cada fruta
    contagem_frutas = {}

    # Percorre a lista de frutas e conta as ocorrências de cada uma
    for fruta in lista_frutas:
        contagem_frutas[fruta] = contagem_frutas.get(fruta, 0) + 1

    return contagem_frutas

# Lista de frutas (exemplo)
lista_frutas = ["Maçã", "Banana", "Maçã", "Pera", "Banana", "Maçã", "Uva", "Uva", "Pera,Amora,Kiwi"]

# Chama a função para contar as frutas
contagem = contar_frutas(lista_frutas)

# Imprime o dicionário com a contagem de frutas
print("Contagem de frutas:")
for fruta, quantidade in contagem.items():
    print(f"{fruta}: {quantidade}")
