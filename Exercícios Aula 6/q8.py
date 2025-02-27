entrada = False

while entrada == False:

    numero = int(input('Escolha um numero de 1 a 4: ',))
    
    if numero not in range(1,5):
        print('Entrada inválida')
        entrada == False
    else:
        print(f'O número digitado foi: {numero}')
        break