nome = str(input('Digite o seu nome: '))
nascimento = int(input('Digite o seu ano de nascimento: '))
ctps = str(input('Digite a sua carteira de trabalho (xxx.xxxxx.xx-X): '))

salario = float(input('Digite o seu salario (Sem R$): ').replace(',','.'))
idade = 2025-nascimento
ano_contratacao = int(input('Digite o seu ano de contratação: '))
aposentadoria = idade+35


trabalho = {}
if ctps != '0':
    trabalho = {
    nome : [nascimento, ctps, idade, salario, ano_contratacao, aposentadoria]
    }
    print(trabalho)
else: 
    print('Parametros incorretos')
