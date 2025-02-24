def caixa():
    #Entrada
    valor = float(input('Digite o valor da peça: ', ).replace(",","."))
    qtd = int(input('Digite a quantidade: ',))
    perDesconto = 0
    
    #Processamento
    total = valor * qtd

    #Saída -> Concatenação
    print(f"Total da compra: R${total}")
    quantidade = [9, 99, 999]
    for i in range (len(quantidade)):
        quantidade[i] = int(quantidade[i])
    for i in range (len(quantidade)):
        if qtd >= quantidade[i]:
            perDesconto = perDesconto + 0.05
    #Processamento
    desconto = total*perDesconto
    print(f"Seu desconto é de: R${desconto:,.1f}") #Saída

    totalDesc = total - desconto
    print(f'Total da compra: R${totalDesc:,}') #Saída
caixa()
