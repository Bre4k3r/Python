repetir = True

while repetir == True:
    valor = float(input('Digite a quantidade de euros que você deseja converter: ',).replace(',','.'))
    valorDolar = (valor)*1.84
    confirm = str(input(f'O valor convertido é: {valorDolar:.2f}\nVocê deseja continuar utilizando o programa? (S/N): '))

    confirm.capitalize()
    if confirm == 'S':
        repetir = True
    else:
        repetir = False
        break