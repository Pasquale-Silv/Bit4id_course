a_tuple = (1, 2, 3)
a, b, c = a_tuple       # Le variabili da assegnare devono essere uguali al numero degli elementi presenti nella tupla

print(a)
print(b)
print(c)

print()

print(a)
print(b)
a, b = b, a              # E' come usare una variabile di appoggio c = a per assegnare il valore di a modificato a b una volta cambiato a = b
print(a)
print(b)
