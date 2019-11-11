def numDivList(numInt):
    """Ritorna una lista contenente tutti i numeri per cui è divisibile il numero inserito come argomento."""
    list1 = [x for x in range(2, numInt) if numInt % x == 0]
    return list1

listaDiv33 = numDivList(33)
print(listaDiv33)

listaDiv100 = numDivList(100)
print(listaDiv100)

listaDiv101 = numDivList(101)
print(listaDiv101)

listaDiv500 = numDivList(500)
print(listaDiv500)
