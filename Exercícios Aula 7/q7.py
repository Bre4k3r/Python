def soma_imposto(TaxaImposto, Custo):
    return print(f'O valor após taxa é: {Custo*(1-(TaxaImposto/100))}')

TaxaImposto = int(input('Digite a taxa de imposto: '))
Custo = float(input('Digite o custo do produto: ').replace(',','.'))

soma_imposto(TaxaImposto, Custo)