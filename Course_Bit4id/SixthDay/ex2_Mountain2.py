mountainHeights = {
    "Kilimangiaro": 5895,
    "Camerun": 4040,
    "Elgon": 4321,
    "Sinai": 2285,
    "Everest": 8848,                    # Puoi anche chiudere il dizionario con una virgola...Non genera errore.
}
print(mountainHeights)

new_dict = {}
print(type(new_dict))

for key, value in mountainHeights.items():
    new_dict[key] = [value, round(value * 3.28, 2)]

print(new_dict)

print()
for key, value in new_dict.items():
    print(key, ":", value)

print("-----------------------------------------------\nSeconda parte esercizio:")
print("Solo nome delle montagne:")
for key in new_dict.keys():
    print(key)

print("\nSolo altezza in metri:")
for value in new_dict.values():
    print("Altezza in metri:", value[0])

print("\nSolo altezza in feet:")
for value in new_dict.values():
    print("Altezza in feet:", value[1])

print("\nStatement:")
for k, v in new_dict.items():
    print("La montagna {} è alta {} metri, l'equivalente in feet è {}.".format(k, v[0], v[1]))
