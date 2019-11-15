def fiboSomma(numInt):
    if(numInt == 0 or numInt == 1):
        return 1
    return fiboSomma(numInt - 1) + fiboSomma(numInt - 2)

fiboSomma10 = fiboSomma(10)
print(fiboSomma10)
