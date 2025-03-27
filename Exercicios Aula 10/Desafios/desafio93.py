nome = str(input('Digite o nome do jogador: '))
partidas = int(input('Digite quantas partidas foram jogadas: '))

x = partidas
z=1
gols = []
while x > 0:
    gols.append(int(input(f'Digite quantos gols foram realizados na [{z}] partida: ')))
    z+=1
    x-=1

totalgols = sum(gols)

jogador = {
    nome : [partidas, gols, totalgols]
}

print(jogador)