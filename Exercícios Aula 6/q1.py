qtd = int(input('Digite a quantidade de numeros que você deseja: ',))
lista = []

while qtd > 0:
    x = int(input('Digite o primeiro numero: '))

    if x < 0:
        print('Numero inválido, encerrando programa...')
        break

    lista.append(x)
    qtd = qtd - 1

z = len(lista)
print(f'Os numeros digitados foram: {lista}\nMedia: {(sum(lista))/z}\nSoma: {sum(lista)}')

    