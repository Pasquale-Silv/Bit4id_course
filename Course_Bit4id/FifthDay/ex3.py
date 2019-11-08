python_words = {
    'list': 'A collection of values that are not connected, but have order.',
    'dictionary': 'A collection of key-value pairs',
    'function': 'A named set'
}
print(python_words)
print("\nOra ordiniamo:")

listaOrder = []
for k in python_words.keys():
    listaOrder.append(k)

print(listaOrder)
listaOrder.sort()
print(listaOrder)

print("\nSoluzione:")
for i in range(len(python_words)):
    print(listaOrder[i], ":", python_words[listaOrder[i]])

print("\n--------------------------------------------\nOppure in maniera più veloce:\n")
print(python_words)
print()
print(sorted(python_words))

print("\n\nCon il metodo del prof:")
for word in sorted(python_words.keys()):                          # puoi usare solo la funzione sorted() sul dizionario.
    print("%s: %s" % (word.title(), python_words[word]))
