mountainHeights = {
    "Kilimangiaro": 5895,
    "Camerun": 4040,
    "Elgon": 4321,
    "Sinai": 2285,                        # Puoi anche chiudere il dizionario con una virgola...Non genera errore.
}
print(mountainHeights)

print("\nIn ordine alfabetico:")
for key in sorted(mountainHeights):     # La funzione sorted() ordina solo sulle keys per quanto concerne il dizionario.
    print("La montagna '%s' è alta metri %d." % (key, mountainHeights[key]))
print()

print(mountainHeights)

print("\nIn ordine alfabetico inverso:")
for key in sorted(mountainHeights, reverse=True):
    print("La montagna '%s' è alta circa %d metri." % (key, mountainHeights[key]))

print("----------------------------------------------------")
print(mountainHeights)

print(mountainHeights)
