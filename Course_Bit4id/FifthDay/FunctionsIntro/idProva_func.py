lista1 = [0, 1, 2]
lista2 = lista1

print(id(lista1))
print(id(lista2))    # Stesso id() perchè stesso oggetto passato per riferimento.

print("\nAdesso cambierà poichè non la passiamo più per riferimento, ma la copiamo passando un altro oggetto:")
print(id(lista1[:]))
lista2 = list(lista1)
print(id(lista2))

# Per i dizionari vale lo stesso ragionamento...Ma devi copiarlo con dict() per passarlo per valore!

print("\nOra proviamo con un dizionario(Vale lo stesso ragionamento fatto con la lista):")
dict1 = {"Pasquale": 1, "Alfonso": 2}
dict2 = dict1
print(id(dict1))
print(id(dict2))
print("Adesso copiamolo creando un nuovo oggetto:")
print(id(dict(dict1)))
dict3 = dict(dict1)
print(id(dict3))

# Quindi se lo passi a una funzione e non vuoi che venga modificato ricorda questa regola fondamentale!!!
