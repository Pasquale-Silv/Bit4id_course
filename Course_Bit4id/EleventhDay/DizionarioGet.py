dizionario = {
    1: "Pasquale",
    2: "Alfonso",
    3: "Pippo"
}

print(dizionario.get(1))
print(dizionario.get(8))                                          # None by default
print(dizionario.get(11, "Non esiste questa chiave."))
print(dizionario.get(22, "Non esiste !!!"))
