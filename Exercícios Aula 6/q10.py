while True:
        sexo = input("Digite o sexo (F para feminino, M para masculino): ").strip().upper()
        idade = int(input("Digite a idade: "))
        escolaridade = int(input("Digite a escolaridade (1 para Fundamental, 2 para Médio, 3 para Superior): "))
        
        if sexo == 'F' and idade <= 25 and escolaridade == 2:
            # É possível utilizar and para multiplas verificações ao mesmo tempo
            print("Cargo disponível: Recepcionista")

        elif sexo == 'M' and idade >= 40 and escolaridade == 1:
             print("Cargo disponível: Servente")

        elif idade <= 30 and escolaridade == 3:
             print("Cargo disponível: Axuiliar de RH")

        else:
            print("Não há posição disponível.")
        
        continuar = input("Deseja continuar? (sim ou não): ").strip().lower()
        if continuar == 'não':
            print("Programa finalizado.")
            break
        else: ...
