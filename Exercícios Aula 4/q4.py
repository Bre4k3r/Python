time = str(input('Digite o nome do time: ',)) #Entrada
vitorias = int(input('Digite o número de vitorias do time: ',)) #Entrada
empates = int(input('Digite o número de empates do time: ',)) #Entrada

pontos = (vitorias*3)+empates #Processamento

print(f'O time {time} possui {pontos} pontos!') #Saida
