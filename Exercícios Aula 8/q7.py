V = [9, 8, 7, 12, 0, 13, 21]
listaPar = []
listaImpar = []

for i in V:
    if i % 2 == 0:
        listaPar.append(i)
        
    else:
        listaImpar.append(i)

print(f'{listaPar}')
print(f'{listaImpar}')