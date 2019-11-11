def factorial_WithoutRec(numInt):
    """Ritorna il fattoriale del numero inserito come argomento."""
    if (numInt <= 0):
        return 1
    factorial = 1
    while(numInt > 0):
        factorial *= numInt
        numInt -= 1
    return factorial

factorial5 = factorial_WithoutRec(5)
print("5! =", factorial5)

factorial4 = factorial_WithoutRec(4)
print("4! =", factorial4)

factorial3 = factorial_WithoutRec(3)
print("3! =", factorial3)

while(True):
    num = int(input("Inserisci il numero di cui vuoi vedere il fattoriale:\n"))
    factorialNum = factorial_WithoutRec(num)
    print("{}! = {}".format(num, factorialNum))
    risposta = input("Desideri ripetere l'operazione?\nPremi S per confermare, qualunque altra cosa per annullare.\n").upper()
    if(risposta != "S"):
        break
