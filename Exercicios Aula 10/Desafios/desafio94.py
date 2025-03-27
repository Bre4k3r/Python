fem = []

nome1 = str(input('Digite o nome da primeira pessoa: '))
sexo1 = str(input('Digite o sexo da primeira pessoa: '))
idade1 = int(input('Digite a idade da primeira pessoa: '))

if sexo1 == 'Feminino':
    fem.append(nome1)
    

nome2 = str(input('Digite o nome da segunda pessoa: '))
sexo2 = str(input('Digite o sexo da segunda pessoa: '))
idade2 = int(input('Digite a idade da segunda pessoa: '))

if sexo2 == 'Feminino':
    fem.append(nome2)

nome3 = str(input('Digite o nome da terceira pessoa: '))
sexo3 = str(input('Digite o sexo da terceira pessoa: '))
idade3 = int(input('Digite a idade da terceira pessoa: '))

if sexo3 == 'Feminino':
    fem.append(nome3)

idade = (idade1+idade2+idade3)/3

pessoa1 = {
    "nome": nome1,
    "sexo": sexo1,
    "idade": idade1
}

pessoa2 = {
    "nome": nome2,
    "sexo": sexo2,
    "idade": idade2
}

pessoa3 = {
    "nome": nome3,
    "sexo": sexo3,
    "idade": idade3
}


cadastros = [pessoa1, pessoa2, pessoa3]

print(f'Foram cadastradas {len(cadastros)} pessoas.')
print(f'A media de idade é: {idade}')
print(f'As mulheres cadastradas são: {fem}')

acima_media = []
if idade1>idade:
    acima_media.append(nome1)
if idade2>idade:
    acima_media.append(nome2)
if idade3>idade:
    acima_media.append(nome3)

print(f'As pessoas acima da media de idade são: {acima_media}')
