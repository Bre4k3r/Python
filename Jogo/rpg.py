import random
import os
import time
import math

combate=False
running = True

clear = lambda: os.system('cls')

class jogador():
    def __init__(self):

        self.nivel = 1
        self.exp = 0

        self.hp = 10
        self.max_hp = 10
        
        self.ataque = 3
        self.defesa = 1

        self.ouro = 0

    def adicionar_ataque(self,ataque):
        self.ataque += ataque
        return self.ataque

    def adicionar_defesa(self,defesa):
        self.defesa += defesa
        return self.defesa

    def adicionar_hp(self,hp):
        self.hp += hp
        self.max_hp += hp
        return self.hp

    def adicionar_ouro(self,ouro):
        self.ouro += ouro
        print(f'> {ouro} de OURO foi adquirido\n')
        time.sleep(0.5)
        return self.ouro

    def remover_ouro(self,ouro):
        self.ouro -= ouro
        print(f'> {ouro} de OURO foi gasto\n')
        time.sleep(0.5)
        return self.ouro
    
    def ataque_personagem(self, hp_inimigo, defesa_inimigo):
        dano = max(0, self.ataque - defesa_inimigo)
        hp_inimigo -= dano
        print(f'\n{dano} de dano foi causado ao inimigo!')

        crit = random.randint(1,20)
        if crit == 20:
            dano = max(0 , self.ataque - defesa_inimigo)
            dano = dano*2
            hp_inimigo -= dano
            print(f'\n[CRITICO] - {dano} de dano foi causado ao inimigo!')


        time.sleep(0.5)
        return hp_inimigo

    def ataque_inimigo(self, hp_jogador, ataque_inimigo):
        dano = max(0, ataque_inimigo - self.defesa)
        self.hp -= dano
        print(f'{dano} de dano foi recebido!\n')
        time.sleep(0.5)
        return self.hp
    
    def level_up(self):
        if self.exp == 500*((1.8)*(self.nivel-1)):
            self.nivel+=1
            print(f'Parabens, você upou de nível!\n[NIVEL {self.nivel}]\n[HP] + 5 \n[ATAQUE] + 1\n [DEFESA] + 1\n')
            self.adicionar_hp(5)
            self.adicionar_ataque(1)
            self.adicionar_defesa(1)
            time.sleep(0.5)

    def adicionar_exp(self,experiencia):
        self.exp += experiencia
        print(f'> {experiencia} de EXP foi obtida.\n')
        time.sleep(0.5)
        return experiencia

    def combateR(self,combate,dificuldade):
        print(dificuldade)
        hp_inimigo = 10*dificuldade
        ataque_inimigo = 3*dificuldade
        defesa_inimigo = 2*dificuldade

        turno = 0
        while combate == True:
            time.sleep(0.5)
            turno+=1
            print(f'TURNO: [{turno}]')
            print('1: Ataque\n2: Correr')
            escolha = int(input('Escolha a sua ação: ')) 
            if escolha == 1:
                rolagem = random.randint(1,20)
                if rolagem <= 5:
                    print('Você errou!')
                    print('O hp do inimigo é: ',hp_inimigo,)
                else:
                    hp_inimigo = Player.ataque_personagem(hp_inimigo, defesa_inimigo)
                    print('O hp do inimigo é: ',hp_inimigo,)
                print('\n-----x-----\n')

            elif escolha == 2:
                roll = random.randint(1,4)
                if roll <= 3:
                    combate = False
                else:
                    combate = True

            rolagemI = random.randint(1,20)
            if rolagemI <= 5:
                print('O inimigo errou!')
                print(f'O seu hp é: {self.hp}')
            else:
                Player.hp = Player.ataque_inimigo(Player.hp, ataque_inimigo)
                print(f"Seu HP: {Player.hp}\nHP do Inimigo: {hp_inimigo}\n")
            print('-----x-----\n')

    
            if Player.hp <= 0:
                    print("Você foi derrotado!\n")
                    print('-----x-----\n')
                    
                    break
                    
                    
            if hp_inimigo <= 0:
                print('Inimigo derrotado!\n')
                print('-----x-----\n')
                
                if dificuldade >= 1:
                    ouro = 25*dificuldade
                    exp = 100*dificuldade

                elif dificuldade >= 3:
                    ouro = 50*dificuldade
                    exp = 200*dificuldade
                
                elif dificuldade >= 5:
                    ouro = 75*dificuldade
                    exp = 300*dificuldade
                
                elif dificuldade >= 10:
                    ouro = 100*dificuldade
                    exp = 500*dificuldade
                
                elif dificuldade >= 20:
                    ouro = 125*dificuldade
                    exp = 500*dificuldade
                
                elif dificuldade > 30:
                    ouro = 150*dificuldade
                    exp = 500*dificuldade
                
                Player.adicionar_ouro(ouro)
                Player.adicionar_exp(exp)
                Player.level_up()

                time.sleep(0.5)
                combate = False


    def mostrar_status(self):
        print(f'[NIVEL] - {self.nivel}\n\n[EXP] - {self.exp}/{500*((1.8)*(self.nivel+1))}\n\n[HP] - {self.hp} | {self.max_hp}\n[ATAQUE] - {self.ataque}\n[DEFESA] - {self.defesa}\n[OURO] - {self.ouro}\n-----x-----\n')

Player = jogador()
nivel_monstro = Player.nivel*1.2
nivel_monstro = math.floor(nivel_monstro)

class mundo():

    def cidade():
        print('> Você deseja ir para aonde?\n1: Loja\n2: Descansar\n3: Explorar')
        time.sleep(0.5)
        
        choice = int(input('Digite a sua escolha: '))

        if choice == 1:
            print('-----x-----\n')
            mundo.loja()

        elif choice == 2:
            print('-----x-----\n')
            Player.hp = Player.max_hp
            display()
        
        else:
            ...

    def loja():

        nome = ['Ana Clara', 'João Pedro', 'Helena', 'Miguel', 'Laura', 'Lucas', 'Isabela', 'Rafael', 'Mariana', 'Gustavo',
        'Beatriz', 'Arthur', 'Valentina', 'Enzo', 'Sofia', 'Davi', 'Lívia', 'Theo', 'Júlia', 'Pedro Henrique',
        'Alice', 'Matheus', 'Yasmin', 'Caio', 'Camila', 'Bruno', 'Lara', 'Diego', 'Bianca', 'Daniel',
        'Fernanda', 'Heitor', 'Elisa', 'Igor', 'Heloísa', 'Samuel', 'Letícia', 'Vinícius', 'Vitória', 'Nicolas',
        'Manuela', 'Leonardo', 'Nicole', 'André', 'Milena', 'Marcelo', 'Lorena', 'Rodrigo', 'Clara', 'Felipe',
        'Maitê', 'Eduardo', 'Luna', 'Henrique', 'Melissa', 'Antônio', 'Giovanna', 'Christian', 'Alana', 'Raul',
        'Júlia Vitória', 'Vitor', 'Camilly', 'Luiz Otávio', 'Zoe', 'Francisco', 'Bella', 'Murilo', 'Cecília', 'Jorge',
        'Rebeca', 'Luan', 'Ágatha', 'Leandro', 'Mirella', 'Tiago', 'Emanuelle', 'Allan', 'Rafaela', 'Erik',
        'Talita', 'Jonatas', 'Isadora', 'Bryan', 'Noemi', 'Gabriel', 'Luara', 'Cael', 'Ayla', 'Otávio',
        'Jade', 'Lorenzo', 'Estela', 'Benjamin', 'Alice Maria', 'Gael', 'Clara Sofia', 'Enrico', 'Liz', 'Noah']
        
        x = random.randint(0,99)

        print(f'[{nome[x]}]: O que deseja comprar, aventureiro?\n1: Espada(100G) \n2: Armadura(150G)\n3: Voltar')
        compra = int(input('Digite a sua escolha: '))
        print('\n-----x-----\n')
        if compra == 1:
            if Player.ouro >= 100:
                Player.adicionar_ataque(2)
                Player.remover_ouro(100)
                print(f'[{nome[x]}]: Obrigado pela compra, aventureiro!')
            else:
                print('Ouro insuficiente.\n')
            print('-----x-----\n')
            return
        elif compra == 2:
            print('-----x-----\n')
            if Player.ouro >= 150:
                Player.adicionar_defesa(2)
                Player.remover_ouro(150)
                print(f'[{nome[x]}]: Obrigado pela compra, aventureiro!')
            else:
                print('Ouro insuficiente.')
            print('-----x-----\n')
            return
        elif compra == 3:
            print(f'[{nome[x]}]: Até mais, aventureiro!)\n')
            mundo.cidade()
            

def display():
    roll = random.randint(0,2)

    if roll == 0:
        time.sleep(0.5)
        x = random.randint(0,100)

        if x == 0:
            print('> Você encontrou um [Dragão] se prepare para o combate.\n')
            time.sleep(0.5)
            dificuldade = nivel_monstro*5

            combate=True
            print('-----x-----\n')
            combateR(combate,dificuldade)

        elif x <= 10:
            print('> Você encontrou um [Gigante] se prepare para o combate.\n')
            time.sleep(0.5)
            dificuldade = nivel_monstro*3

            combate=True
            print('-----x-----\n')
            combateR(combate,dificuldade)

        elif x <= 50:
            print('> Você encontrou um [Goblin] se prepare para o combate.\n')
            time.sleep(0.5)
            dificuldade = nivel_monstro*1

            combate=True
            print('-----x-----\n')
            combateR(combate,dificuldade)


        elif x <= 99:
            print('> Você encontrou uma [Horda de Lobos] se prepare para o combate.\n')
            time.sleep(0.5)
            dificuldade = nivel_monstro*1

            combate=True
            print('-----x-----\n')
            combateR(combate,dificuldade)

    elif roll == 1:
        time.sleep(0.5)
        x = random.randint(0,2)
        if x == 0:
            print('> Uma pilha de ouro foi encontrada!')
            Player.adicionar_ouro(100)
            print('-----x-----\n')

        elif x == 1:

            print('> Um bau foi encontrado!\n')
            print('-----x-----\n')
            z = random.randint(0,2)

            if z == 0:
                print('> Uma espada foi encontrada! seu ataque aumentou em 3.\n')
                print('-----x-----\n')
                Player.adicionar_ataque(3)

            if z == 1:
                print('> Uma armadura foi encontrada! sua defesa aumentou em 1.\n')
                print('-----x-----\n')
                Player.adicionar_defesa(1)

            if z == 2:
                print('> Você não encontrou nada no bau\n')
                print('-----x-----\n')

        elif x == 2:
            print('> Um lobo sai de dentro do bau!\n')
            print('-----x-----\n')
            combate = True
            combateR(combate, 1)
    
    elif roll == 2:
        print('> Você encontrou uma cidade!')
        mundo.cidade()
        
combateR = Player.combateR

while running:
    escolha = int(input('1: Explorar\n2: Janela de Status\n3: Sair\n9: Info\nEscolha: '))
    print('\n')
    if escolha == 1:
        display()
    elif escolha == 2:
        Player.mostrar_status()
    elif escolha == 3:
        break
    elif escolha == 9:
        print('Desenvolvedor: Leonardo Domingues de Oliveira\nE-mail: Leo2014coc@gmail.com')
    if Player.hp <= 0:
        break
    else:
        ...