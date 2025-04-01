import random
combate=False
running = True
            
class jogador():
    def __init__(self):
        self.hp = 10
        self.ataque = 4
        self.defesa = 2
        self.ouro = 0
        self.nivel = 0

    def adicionar_ataque(self,ataque):
        self.ataque += ataque
        return self.ataque

    def adicionar_defesa(self,defesa):
        self.defesa += defesa
        return self.defesa
    
    def adicionar_ouro(self,ouro):
        self.ouro += ouro
        print(f'{ouro} foi adquirido')
        return self.ouro
    
    def ataque_personagem(self, hp_inimigo, defesa_inimigo):
        dano = max(0, self.ataque - defesa_inimigo)
        hp_inimigo -= dano
        print(f'{dano} foi causado ao inimigo!')
        return hp_inimigo

    def ataque_inimigo(self, hp_jogador, ataque_inimigo):
        dano = max(0, ataque_inimigo - self.defesa)
        self.hp -= dano
        print(f'{dano} foi recebido!')
        return self.hp

    def combateR(self,combate,dificuldade):
        hp_inimigo = 10*dificuldade
        ataque_inimigo = 3*dificuldade
        defesa_inimigo = 2*dificuldade

        print('1: Ataque\n2:Defesa\n3:Correr')
        while combate == True:
            escolha = int(input('Escolha a sua ação: ')) 

            if escolha == 1:
                hp_inimigo = Player.ataque_personagem(hp_inimigo, defesa_inimigo)
                print(hp_inimigo)


                if hp_inimigo <= 0:
                    print('Inimigo derrotado!')
                    combate = False
                

            Player.hp = Player.ataque_inimigo(Player.hp, ataque_inimigo)
            print(f"Seu HP: {Player.hp}\nHP do Inimigo: {hp_inimigo}")

            if Player.hp <= 0:
                    print("Você foi derrotado!")
                    running = False
                    

            elif escolha == 2:
                Player.defesa = 4
                print('Defesa!')


            elif escolha == 3:
                roll = random.randint(1,2)
                if roll == 1:
                    combate = False
                else:
                    combate = True

Player = jogador()

class mundo():
    def cidade():
        print('Você deseja ir para aonde?\n1: Loja\n2: Descansar\n3: Explorar')

    def loja():
        print('O que deseja comprar?\n1: Espada(100G) \n2: Armadura(150G)\n 3: Voltar')
        compra = int(input('Digite a sua escolha: '))
        if compra == 1:
            Player.adicionar_ataque(2)
            Player.remover_ouro(100)
            return
        elif compra == 2:
            Player.adicionar_defesa(2)
            Player.remover_ouro(150)
            return
        elif compra == 3:
            mundo.cidade()




#encontro = ['Monstro','Cidade','Tesouro'] #0
#monstro = ['Dragão', 'Goblin', 'Troll', 'Lobo']
#tesouro = ['Ouro', 'Item', 'Monstro'] #1
#cidade = ['Loja', 'Descansar'] #2

rodada = 0
combateR = Player.combateR

while running:
    roll = random.randint(0,2)
    if roll == 0:
        x = random.randint(0,3)
        if x == 0:
            dificuldade = Player.nivel*3
            combate=True
            combateR(combate,dificuldade)
        elif x == 1:
            dificuldade = Player.nivel*0.5
            combate=True
            combateR(combate,dificuldade)
        elif x == 2:
            dificuldade = Player.nivel*1.5
            combate=True
            combateR(combate,dificuldade)

        elif x == 3:
            dificuldade = Player.nivel*1
            combate=True
            combateR(combate,dificuldade)

    elif roll == 1:
        x = random.randint(0,2)
        if x == 0:
            Player.adicionar_ouro(100)
        elif x == 1:
            print('Um bau foi encontrado!')
            z = random.randint(0,2)
            if z == 0:
                print('Uma espada foi encontrada! seu ataque aumentou em 3.')
                Player.adicionar_ataque(3)
            if z == 1:
                print('Uma armadura foi encontrada! sua defesa aumentou em 1.')
                Player.adicionar_defesa(1)
            if z == 2:
                print('Você não encontrou nada no bau')
        elif x == 2:
            print('Um lobo sai de dentro do bau!')
            combateR(1)
    
    
    elif roll == 2:
        mundo.cidade()
        choice = int(input('Digite a sua escolha: '))
        if choice == 1:
            mundo.loja()

            
