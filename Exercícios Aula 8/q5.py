x=5
c=5
lista1=[]
lista2=[]
lista3=[]

while x > 0:
    lista1.append(int(input('Lista 1 - Digite um número: ')))
    x-=1
while c > 0:
    lista2.append(int(input('Lista 2 - Digite um número: ')))
    c-=1

lista3 = lista1 + lista2
print(lista3)