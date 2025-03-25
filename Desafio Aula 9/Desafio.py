X = True
while X == True:
    G = str(input('O país está em guerra ou não? (S/N)'))
    Idade = int(input('Digite a sua idade: '))

    paz = True



    if G == 'S':
        paz = False

        if Idade > 17:
            print('Você sera convocado para a guerra')
            break

        else:
            print('Você não sera convocado para a guerra')
            break



    else:
        if Idade == 17:
            Decisao = str(input('Você faz 18 anos este ano? (S/N): '))

            if Decisao == 'S':
                Alistar = str(input('Você deseja se alistar? (S/N): '))

                if Alistar == 'S':
                    print('Você está apto a se alistar')
                    break

                else:
                    print('Você não participara do alistamento')
                    break

            else:
                print('Você não é elegível para o alistamento, retorne no ano em que faz 18 anos')
                break

        elif Idade >= 18:
            Alistar = str(input('Você deseja se alistar? (S/N): '))

            if Alistar == 'S':
                print('Você está apto a se alistar')
                break

            else:
                print('Você não participara do alistamento')
                break
            

        elif Idade >= 45:
            print('Você não está apto a se alistar')
            break


        else:
            print('Você não é elegível para o alistamento, retorne no ano em que faz 18 anos')
            break