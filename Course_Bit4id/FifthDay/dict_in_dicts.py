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

