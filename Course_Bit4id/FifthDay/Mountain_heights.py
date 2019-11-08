mountainHeights = {
    "Kilimangiaro": 5895,
    "Camerun": 4040,
    "Elgon": 4321,
    "Sinai": 2285,                        # Puoi anche chiudere il dizionario con una virgola...Non genera errore.
}
print(mountainHeights)

print("\nKEYS:")
for key in mountainHeights.keys():
    print(key)

print("\nVALUES:")
for value in mountainHeights.values():
    print(value, "metri.")

print("\nSTATEMENT:")
for k, v in mountainHeights.items():
    print("La montagna '%s' è alta esattamente %d metri." % (k, v))

print("\nIn ordine alfabetico:")
for key in sorted(mountainHeights):     # La funzione sorted() ordina solo sulle keys per quanto concerne il dizionario.
    print("La montagna '%s' è alta metri %d." % (key, mountainHeights[key]))
