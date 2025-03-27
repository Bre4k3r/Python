nome = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana", "Lucas", "Mariana", "Pedro", "Sofia", "André"]
prova1 = [8.5, 7.2, 9.0, 6.8, 5.5, 10.0, 4.3, 7.9, 8.1, 6.0, 5, 6.7, 8.8, 7.0, 5.2]
prova2 = [9.5, 6.7, 8.8, 7.0, 5.2, 4.9, 10.0, 3.6, 7.4, 6.3, 9, 10.0, 3.6, 7.4, 6.3]

z=0
media=0
aprovado=True

for x in nome:
    media = (prova1[z]+prova2[z])/2
    if media >= 6:
        aprovado = True
    else:
        aprovado = False
    print(f'{x} - Media: {media}, Aprovado = {aprovado}')
    z+=1