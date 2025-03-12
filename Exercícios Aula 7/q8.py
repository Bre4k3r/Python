def classe_eleitoral(idade):
    if idade < 16:
        return print('Não-Eleitor')
    elif idade >= 18 and idade <= 65:
        return print('Eleitor Obrigatório')
    elif idade > 65:
        return print('Eleitor Facultativo')
    elif idade >= 16 and idade < 18:
        return print('Eleitor Facultativo')

idade = int(input('Digite a sua idade: '))
classe_eleitoral(idade)