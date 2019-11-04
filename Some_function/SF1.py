def poppaLista(lista):
    print(lista)
    for i in range(0, len(lista)):
        poppato = lista.pop()
        print(poppato)
        print(lista)


list1 = [3, 4, 5, 8]
poppaLista(list1)