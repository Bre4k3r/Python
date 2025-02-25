x=0
lista = []

for x in range(1,16):
    num = int(input('Digite um número: ',))
    lista.append(num)
    x += 1

    maior = lista[0]
    menor = lista[0]

    if x == 16:
        for i in lista:
            if i>maior:
                maior = i
            else:
                if i<menor:
                    menor = i
        print(f'O maior numero da lista é: {maior}\n O menor numero da lista é: {menor}')
        break
