def factorialWithRec(numInt):
    if(numInt <= 1):
        return 1
    factorial = numInt * factorialWithRec(numInt - 1)
    return factorial

factorial5 = factorialWithRec(5)
print("5! =", factorial5)

factorial4 = factorialWithRec(4)
print("4! =", factorial4)
