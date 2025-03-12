def soma_impares(n1, n2):
    lista_impares = []

    if n1 > n2:
        return print('Numero 1 invalído')
    
    else:
        for i in range(n1,n2+1):
            if i % 2 == 0:
                ...
            else: 
                lista_impares.append(i)

    return print(f'A soma dos números impares entre {n1} e {n2} é: {sum(lista_impares)}')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma_impares(n1,n2)