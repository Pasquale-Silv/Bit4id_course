# key:value pairs with no order, dictionaries are indexed by key

firstDict = {
              "Pasquale": 120,
              "Alfonso": 98,
              "Bryan": 77
            }

print(firstDict)

for key, value in firstDict.items():
    print("Person:", key, ", points:", value)

for key in firstDict.keys():
    print("Chiave:", key)
# Di default se non metti nessun metodo, Python mappa per keys
for key in firstDict:
    print("Chiave:", key)

for value in firstDict.values():
    print("Valore:", value)

print("\nIl dizionario è un elemento mutabile!")
print(firstDict)
# Il dizionario è un elemento mutabile!
firstDict["Giacomo"] = 56             # Aggiunta di un nuovo elemento
firstDict["Bryan"] = 89               # Modifica di un elemento preesistente se la chiave già esiste nel dict
print(firstDict)

del(firstDict['Giacomo'])
print(firstDict)

print()

valPoppatoDict = firstDict.pop("Bryan")     # Nel dizionario .pop() deve avere almeno un argomento
print(valPoppatoDict)
print(firstDict)
print()

# Come key del dict puoi usare solamente elementi immutabili(stringhe, interi, tuple)
# Elementi mutabili non possono essere usati come key del dizionario(lista)
# I values, invece, possono essere tutti i tipi, compresi gli stessi dizionari
