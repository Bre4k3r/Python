import random

dado1 = random.randint(1,20)
dado2 = random.randint(1,20)
dado3 = random.randint(1,20)
dado4 = random.randint(1,20)

jogo = {
    "Jogador_1": dado1,
    "Jogador_2": dado2,
    "Jogador_3": dado3,
    "Jogador_4": dado4
}

jogo = dict(sorted(jogo.items(), key=lambda item: item[1], reverse=True))
print(jogo)