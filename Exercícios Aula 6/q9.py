x=7

idadeL = []
pesoL = []

qtd1860 = 0

while x>0:
    idade = int(input('Digite a idade da pessoa: '))
    idadeL.append(idade)
    peso = int(input('Digite o peso da pessoa: '))
    pesoL.append(peso)

    if idade >= 18:
        if peso >= 60:
            qtd1860+=1

    print('-----')

    if idade < 0:
        break

    x-=1

mediaIdade = (sum(idadeL))/(len(idadeL))


peso90=0
porcentagemI = 0
z=6
while z>=0:
    if pesoL[z] >= 90:
        peso90+=1

    if idadeL[z] >= 10:
        if idadeL[z] <= 30:
            porcentagemI+=1


    z-=1

porcentagemI = porcentagemI/7
porcentagemI = porcentagemI*100

print(f'A quantidade de pessoas com mais de 90kg é: {peso90}\nA média das idades é: {mediaIdade:.1f}\nA quantidade de pessoas maiores de idade com peso abaixo de 60kg é: {qtd1860}\nA porcentagem de pessoas com idade entre 10 e 30 é: {porcentagemI:.2f}%')
