mountainHeights = {
    "Kilimangiaro": 5895,
    "Camerun": 4040,
    "Elgon": 4321,
    "Sinai": 2285,
    "Everest": 8848,                    # Puoi anche chiudere il dizionario con una virgola...Non genera errore.
}
print(mountainHeights)

for key, value in mountainHeights.items():
    mountainHeights[value] = key
    del mountainHeights[key]

print(mountainHeights)

swap = {value:key for key, value in mountainHeights.items()}
print(swap)
