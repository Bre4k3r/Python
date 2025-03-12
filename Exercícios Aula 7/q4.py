def area_triangulo(B, H):
    return (B*H)/2

B = int(input(print('Digite a base do triangulo em cm: ')))
H = int(input(print('Digite a altura do triangulo em cm: ')))

print(f'A area do triangulo é: {area_triangulo(B, H)}cm²')
