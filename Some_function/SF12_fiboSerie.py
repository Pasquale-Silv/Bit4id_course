def fiboSerie(numInt):
    a = 0
    b = 1
    temp = 0
    while(numInt > 0):
        print(a, end=" ")
        temp = a
        a = a + b
        b = temp
        numInt -= 1
    print()

fiboSerie(10)

fiboSerie(20)