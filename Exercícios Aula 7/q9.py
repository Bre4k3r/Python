def conceito_nota(nota):
    if nota < 0 or nota > 10:
        return print('Nota invalída')
    
    elif nota < 3:
        return print('Conceito E')

    elif nota > 3 and nota < 5:
        return print('Conceito D')

    elif nota > 6 and nota < 7:
        return print('Conceito C')

    elif nota > 8 and nota < 9:
        return print('Conceito B')
    
    elif nota == 10:
        return print('Conceito A')
    
nota = int(input('Digite a nota do aluno: '))
conceito_nota(nota)