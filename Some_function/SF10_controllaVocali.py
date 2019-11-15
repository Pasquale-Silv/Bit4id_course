def controllaVocali(parola):
    "Controlla se la parola contiene almeno una vocale!"
    parola2 = parola.upper()
    vocali = ['A', 'E', 'I', 'O', 'U']
    for vocale in vocali:
        if vocale in parola2:
            print("La parola '%s' contiene almeno una vocale." % parola)
            break
    else:
        print("La parola '%s' non contiene nessuna vocale." % parola)

controllaVocali("Archimede")
controllaVocali("Pasquale")
controllaVocali("brrrh")
