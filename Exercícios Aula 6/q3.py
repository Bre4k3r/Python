qtd = int(input('Digite a quantidade de numeros que você deseja: ',))
var = qtd-1
lista = []

while qtd > 0:
    x = int(input('Digite o primeiro numero: '))

    if x < 0:
        print('Numero inválido, encerrando programa...')
        break

    lista.append(x)
    qtd = qtd - 1

lista.sort()
print(f'Os números digitados foram: {lista}\nO menor número foi: {lista[0]}\nO maior número foi: {lista[var]}')
