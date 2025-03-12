def comparar(n1,n2):
    if n1 % n2 == 0:
        return print(f'O primeiro número ({n1}) é multiplo do segundo ({n2})')
    else:
        return print(f'O primeiro número não é multiplo do segundo')     

n1 = int(input('Digite o primeiro número: ',))
n2 = int(input('Digite o segundo número: '))

comparar(n1,n2)