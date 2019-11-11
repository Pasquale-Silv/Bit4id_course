def swapKeyValue(dictionary):
    """Scambia la chiave con il valore di un dizionario in un nuovo dizionario."""
    swap = {value:key for key, value in dictionary.items()}
    return swap


dict1 = {"Pasquale": 1, "Alfonso": 2, "Bryan": 3}

print(dict1)

swapDict1 = swapKeyValue(dict1)

print("Dopo la chiamata della funzione swapKeyValue:", swapDict1)

print(dict1)

print(swapKeyValue(dict1))
