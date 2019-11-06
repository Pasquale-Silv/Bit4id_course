# La funzione sorted() non cambia la lista che c'è per argomento, è un ordinamento temporaneo!

names = ["Pasquale", "Alberto", "Bruno", "Lucia", "Antonio", "Giacomo", "Barbara", "Giorgia", "Alfonso"]

namesOrd = sorted(names)

print(names)
print(namesOrd)

# C'è anche il metodo lista.reverse() che fa il reversing della lista sugli argomenti posizionali!

names.reverse()
print("Lista con .reverse():", names)         # La capovolge sugli indizi posizionale [0, 1, 2] = [2, 1, 0]
