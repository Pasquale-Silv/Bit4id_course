# Puoi anche inserire dizionari in dizionari, solo come values.

dict_in_dicts = {
    "Pasquale": {"Mestiere": "Data Scientist", "Automunito": True, "Titolo di studio": "Laurea triennale", "Peso": 85},
    "Giulio": {"Mestiere": "Matematico", "Automunito": True, "Titolo di studio": "Laurea magistrale", "Peso": 77},
    "Alfonso": {"Mestiere": "Chirurgo", "Automunito": True, "Titolo di studio": "Laurea magistrale", "Peso": 88},
    "Bryan": {"Mestiere": "Meccanico", "Automunito": True, "Titolo di studio": "Diploma", "Peso": 64},
    "Giacomo": {"Mestiere": "Agricoltore", "Automunito": False, "Titolo di studio": "Diploma", "Peso": 93}
}
print(dict_in_dicts, "\n")
print(dict_in_dicts.items())
print(dict_in_dicts.keys())
print(dict_in_dicts.values())
print()

print(dict_in_dicts["Pasquale"]["Mestiere"])         # Accedi cosi a una chiave di un dict innestato in un altro dict!

print("\nVediamo i dati di Alfonso:")
print(dict_in_dicts['Alfonso'])
print("Mestiere:", dict_in_dicts['Alfonso']['Mestiere'])
print("Automunito:", dict_in_dicts['Alfonso']['Automunito'])
print("Titolo di studio:", dict_in_dicts['Alfonso']['Titolo di studio'])
print("Peso:", dict_in_dicts['Alfonso']['Peso'])
print()

for k, v in dict_in_dicts.items():
    print(k, "e rispettivo valore:", v)

print()

for k, v in dict_in_dicts.items():
    print("Chiave", k, ", e rispettivo mestiere:", v['Mestiere'])


print("\nMestiere precedente:", dict_in_dicts['Alfonso']['Mestiere'])
dict_in_dicts['Alfonso']['Mestiere'] = "Medico"
print("Nuovo mestiere:", dict_in_dicts['Alfonso']['Mestiere'], "\n")

print("Mestieri presenti:")
for v in dict_in_dicts.values():
    print("Mestiere:", v['Mestiere'])

dict_in_dicts['John Maynard Keynes'] = {"Mestiere": "Economista", "Automunito": True, "Titolo di studio": "Dottorato di ricerca", "Peso": 76}

print("\nNuove chiavi presenti:")
for k in dict_in_dicts.keys():          # .keys() di default in dict class
    print("Individuo:", k)

del(dict_in_dicts['Giacomo'])
print("\nDopo l'eliminazione:")
for k in dict_in_dicts.keys():
    print("Individuo:", k)
print("Giacomo è stato eliminato!\n")

def PrintaDict(dictOfDicts):
    """This function takes a dict and returns a k:v pairs."""
    for k, v in dictOfDicts.items():
        print("key:", k, ",Value:", v)
    print("This is the function! Good job!")

print("\nAdesso proviamo con la funzione:")
PrintaDict(dict_in_dicts)
