qtd = int(input('Digite a quantidade de numeros que você deseja: ',))
lista = []

while qtd > 0:
    x = int(input('Digite o primeiro numero: '))

    if x < 0:
        print('Numero inválido, encerrando programa...')
        break
    
    if x == 0:
        print('Aplicação encerrada')
        break

    lista.append(x)
    qtd = qtd - 1

z = len(lista)
multiplos = []
i = 0

while i < z:
    calc = lista[i]
    if calc % 3 == 0:
        multiplos.append(lista[i])
    else: ...
    i+=1

print(f'Os números digitados foram: {multiplos}\nA média desses números é: {sum(multiplos)/(len(multiplos))}')
