qtd = int(input('Digite a quantidade de numeros que você deseja: ',))
lista = []

while qtd > 0:
    x = int(input('Digite o primeiro numero: '))

    if x > 1000:
        print('Numero inválido, encerrando programa...')
        break

    lista.append(x)
    qtd = qtd - 1

var = 0

Impares = []
Pares = []

while var < len(lista):
    if lista[var] % 2 == 0:
        Pares.append(lista[var])

    else:
        Impares.append(lista[var])
    var+=1

print(f'A soma dos números pares é: {sum(Pares)}\nA soma dos números inpares é: {sum(Impares)}')