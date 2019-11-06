names = ["Pasquale", "Bruno", "Lucia", "Antonio", "Giacomo", "Barbara", "Giorgia", "Alfonso", "Alberto"]

names.sort()

for name in names:
    print(name.title())

names.sort(reverse=True)

print()

for name in names:
    print(name.title())

# metodo .sort()      -------> lista.sort()          Cambia permanentemente l'oggetto sul quale è chiamato!
# funzione sorted()   -------> sorted(lista)         Non cambia la lista che c'è per argomento!

