x = 4
notas = []
while x > 0:
    notas.append(int(input('Digite a nota a ser inserida: ')))
    x-=1

print('As notas são: ', notas)
print(f'A média das notas é: {sum(notas)/len(notas)}')
    