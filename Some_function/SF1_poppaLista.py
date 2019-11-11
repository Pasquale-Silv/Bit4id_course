def poppaLista(lista):
    """Poppa l'intera lista passata come argomento."""
    for i in range(0, len(lista)):
        val_poppato = lista.pop()
        print(val_poppato)
        print(lista)


list1 = [3, 4, 5, 8]
print(list1)
poppaLista(list1)
