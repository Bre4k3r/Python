nome = str(input('Digite o nome da mercadoria: ',))
preco = float(input('Digite o preço da mercadoria: ',).replace(',','.'))

x = preco/20
preco = preco + x

print(f'A mercadoria [{nome}] custara {preco}')
