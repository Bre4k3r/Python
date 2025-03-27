numeros = [12, 25, 7, 38, 19, 45, 30, 22, 9, 41]
print(f'Media: {sum(numeros)/len(numeros)}')

multiplos = 0
maior10menor30 = 0
for x in numeros:
    if x % 5 == 0:
        multiplos+=1
    if x > 10 and x < 30:
        maior10menor30+=1
    
print(f'{multiplos} numeros são multiplos de 5')
print(f'{maior10menor30} numeros são maiores que 10 e menores que 30')

numeros.sort()

print(f'{numeros[0]} é o menor numero da lista e {numeros[9]} é o maior')
