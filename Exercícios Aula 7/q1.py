def comparar(n1,n2):
    if n1 > n2:
        print(f'{n1} é maior que {n2}')
    else:
        print(f'{n2} é maior que {n1}')

n1 = int(input('Digite o primeiro número: ',))
n2 = int(input('Digite o segundo número: '))

comparar(n1,n2)