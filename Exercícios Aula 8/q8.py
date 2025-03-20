pessoas = {15:1.70,
           18:1.50,
           19:1.90,
           60:1.64,
           75:1.63}

z = len(pessoas)
x = z - 1


while x > -1:
    key = list(pessoas.keys())[x]
    val = list(pessoas.values())[x]

    key = str(key)
    val = str(val)

    teste = key + ":" + val

    x-=1

    print(teste)