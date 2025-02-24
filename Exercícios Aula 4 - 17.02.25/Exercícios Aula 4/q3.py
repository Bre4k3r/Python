nome = str(input('Digite o nome da pessoa: ',)) #Entrada
salario = float(input('Digite o salário da pessoa: ',).replace(",",".")) #Entrada
indice = float(input('Digite o índice percentual: ',).replace(",",".")) #Entrada

reajuste = (salario*indice)/100 #Processamento
salario = salario-reajuste #Processamento

print(f'O salário apos reajuste é de R${salario:,.1f}') #Saida
