nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana", "Kleber", "Larissa", "Marcos", "Natália", "Otávio", "Priscila", "Ricardo", "Sabrina", "Thiago", "Vanessa"]
salarios = [1500, 2300, 1800, 2750, 3200, 4100, 2900, 3600, 5000, 6200, 7100, 2800, 3400, 4500, 3900, 5200, 4300, 2500, 4700, 3300,]
n=1
v=0

for x in salarios:
    x = x * 1.08
    print(f'{n}.{nomes[v]} - R${x:.2f}')
    n+=1
    v+=1