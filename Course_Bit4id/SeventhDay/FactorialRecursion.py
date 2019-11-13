def fattorialeRec(numInt):
    if (numInt < 0):
        return "Impossibile effettuare il fattoriale con numeri minori di zero"
    if(numInt == 0 or numInt == 1):
        return 1
    factorial = numInt * fattorialeRec(numInt - 1)
    return factorial

fatt5 = fattorialeRec(5)
print(fatt5)

fatt4 = fattorialeRec(4)
print(fatt4)

fatt3 = fattorialeRec(3)
print(fatt3)

fatt1000 = fattorialeRec(998)
print(fatt1000)
