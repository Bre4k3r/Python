codigo = str(input('Digite o codigo da peça: ',)) #Entrada
valor = float(input('Digite o valor da peça: ').replace(",",".")) #Entrada
quantidade = int(input('Digite a quantidade de peças: ')) #Entrada

vTotal = quantidade * valor #Processamento

print(f'O codigo da peça é: {codigo}') #Saida
print(f'O valor total é: R$ {vTotal:,}') #Saida
