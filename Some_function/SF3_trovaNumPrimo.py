def trovaNumPrimo(num):
    """Scopri se il numero intero passato come argomento è primo oppure no!"""
    isPrimo = True
    for x in range(2, int(num/2 + 1)):
        if(num % x == 0):
            isPrimo = False
            break
    if(isPrimo):
        print("Il numero %d è un numero primo!\n" % num)
    else:
        print("Il numero %d NON è un numero primo!\n" % num)


trovaNumPrimo(3)
trovaNumPrimo(4)
trovaNumPrimo(33)
trovaNumPrimo(100)
trovaNumPrimo(17)
trovaNumPrimo(21)
trovaNumPrimo(53)
trovaNumPrimo(557)