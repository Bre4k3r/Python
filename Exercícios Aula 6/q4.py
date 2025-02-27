qtd = int(input('Digite a quantidade de alunos que você deseja adicionar a média: ',))
var = qtd-1
lista = []

while qtd > 0:
    x = int(input('Digite a primeira média: '))

    if x < 0:
        print('Média inválida, encerrando programa...')
        break
    else:
        ...

    lista.append(x)
    qtd-=1
lista.sort()

print(f'A menor média foi: {lista[0]}\nA maior média foi: {lista[var]}\n A média aritmetica foi: {(sum(lista))/(len(lista))}')
