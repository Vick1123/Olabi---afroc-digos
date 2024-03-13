def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FIZZBUZZ')
        elif i % 3 == 0:
            print('FIZZ')
        elif i % 5 == 0:
            print('BUZZ')
        else:
            print(i)

# Recebe a entrada do usuário
entrada = int(input("Digite um número inteiro: "))

# Chama a função fizzbuzz com a entrada fornecida
fizzbuzz(entrada)
