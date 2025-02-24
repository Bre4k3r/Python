cidade = str(input('Digite o nome da cidade: '),)
eleitores = int(input('Digite o número de eleitores: '),)
votos = int(input('Digite o número total de votos: '),)

total = (votos/eleitores)*100
print(f'Na cidade de {cidade}, {total}% votaram')