# Un set è una lista non ordinata di oggetti distinti! unorderd collection of distinct objects

primoSet = {"Pasquale", "Luca", "Giulio", 1, 2, 3}                                 # Il set non è ordinato
print("Primo set:", primoSet)

primoSet.add("Gennaro")                                                            # Aggiunge elemento al set
print(primoSet)

list1 = ["Pasquale", "Giulio", 3, 3, 8]

secondSet = set(list1)                                                             # Converte una lista in set
print("Secondo set:", secondSet)

print("\nCon intersection:")                                        # intersection ritorna i valori comuni ai due set
print(primoSet.intersection(secondSet))
print(secondSet.intersection(primoSet))

print("\nCon difference:")                      # difference ritorna i valori presenti nel primo set ma non nel secondo
print(primoSet.difference(secondSet))
print(secondSet.difference(primoSet))

print("\nCon union:")                          # union ritorna tutti i valori presenti nel set
print(primoSet.union(secondSet))
print(secondSet.union(primoSet))
