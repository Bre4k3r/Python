x = 10
lista = []
qtd = 0

consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']
c = len(consoantes)
c -= 1
while x > 0:
    lista.append((str(input('Digite uma letra: '))).lower())
    x-=1

for i in lista:
    if i in consoantes:
        qtd+=1

print(f'Foram lidas {qtd} consoantes')