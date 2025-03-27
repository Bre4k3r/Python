numeros = [30,60,90,20,10,15,50,5]
maior_30 = []

for x in numeros:
    if x >= 30:
        maior_30.append(x)
    else:
        ...

print(numeros)
print(f'{len(maior_30)} Numeros são maiores que 30.\n A soma dos numeros é: {sum(maior_30)}')
