tabuada = 0
n=1

for tabuada in range(1,11):
    n=1
    print('-')

    if tabuada == 11:
        break

    for tabuada2 in range(1,11):
        calc = tabuada*n
        print(f'{tabuada}x{n} = {calc}')
        n+=1
