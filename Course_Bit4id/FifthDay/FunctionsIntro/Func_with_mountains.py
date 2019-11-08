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

