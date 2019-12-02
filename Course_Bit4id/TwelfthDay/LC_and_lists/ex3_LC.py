lista1 = [1, 2, 3]
lista2 = [3, 1, 4]
listaComb = []

for elemento1 in lista1:
    for elemento2 in lista2:
        if(elemento1 != elemento2):
            listaComb.append((elemento1, elemento2))

print(listaComb)

print("\nCon la LC:")
lc1 = [(lista1[i], lista2[j]) for i in range(0, len(lista1)) for j in range(0, len(lista2)) if lista1[i] != lista2[j]]
print(lc1)

lc2 = [(el1, el2) for el1 in lista1 for el2 in lista2 if el1 != el2]
print(lc2)
