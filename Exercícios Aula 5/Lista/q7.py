tabuada = int(input('Digite o NR da tabuada: ',))
vr_menor = int(input('Digite o VR menor da tabuada: ',))
vr_maior = int(input('Digite o VR maior da tabuada: '))

vr_maior = vr_maior + 1
n=vr_menor


for tabuada2 in range(vr_menor,vr_maior):
    calc = tabuada*n
    print(f'{tabuada}x{n} = {calc}')
    n+=1
