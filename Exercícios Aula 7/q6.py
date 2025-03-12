P = 'Positivo'
N = 'Negativo'

def comparar(Num):
    if Num > 0:
        return print(f'{Num} é {P}')
    else:
        return print(f'{Num} é {N}')
        ...


Num = int(input('Digite um número: '))
comparar(Num)