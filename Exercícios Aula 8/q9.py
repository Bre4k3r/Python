al = 1
n = 0
media = []
notas = []

while al <= 10:
    n = 4
    while n > 0:
        notas.append(int(input(f'{al} - Digite as notas: ')))
        n-=1
    x = sum(notas)/len(notas)
    media.append(x)
    notas.clear()
    al+=1

for i in media:
    if i >= 7:
        print(i)
    else:
        ...