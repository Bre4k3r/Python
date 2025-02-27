qtd = int(input('Digite a quantidade de pessoas que você deseja adicionar a lista: ',))
var = qtd-1
lista = []

while qtd > 0:
    x = int(input('Digite a primeira idade: '))

    if x == -99:
        print('Idade inválida, encerrando programa...')
        break
    else:
        ...

    lista.append(x)
    qtd-=1

var2 = 0
menor21 = []
maior50 = []

while var2 < lista[var]:
    if lista[var2] <= 21:
        menor21.append(lista[var2])
    else:
        ...
    if lista[var2] >= 50:
        maior50.apend(lista[var2])
    else:
        ...

print(f'A quantidade de pessoas com menos de 21 anos é: {len(menor21)}\nA quantidade de pessoas com mais de 50 anos é: {len(maior50)}')