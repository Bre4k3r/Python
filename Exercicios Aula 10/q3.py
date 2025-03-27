import random

numeros = [1,2,3,4,5,6,7,8]
correta = random.randrange(1,8)
print(correta)
escolha = int(input('Digite um numero de 1 a 8: '))
z=0

for c in numeros:
    if c == correta:
        break
    else:
        z+=1

for x in numeros:
    if escolha == x:
        if escolha == correta:
            print(f'Parabens, você acertou!\nNumero correto: {correta} na casa {z} da lista')
        else:
            print(f'Você errou, tente novamente.\nNumero correto: {correta} na casa {z} da lista')

