def ordinaLista(lista):
    """Ordina una lista in maniera crescente."""
    for i in range(len(lista)):
        for j in range((i+1), len(lista)):
            if(lista[i] > lista[j]):
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp


lista1 = [100, 80, -2, 0,50, 10]
print(lista1)

ordinaLista(lista1)
print(lista1)

lista2 = [500, 100, -100, -2, -4, 0, -1000, 1000]
print("\nSeconda lista:")
print(lista2)

ordinaLista(lista2)
print(lista2)
