def cifra(messaggioDaCifrare, numeroCar):
    nuovaParola = ""
    for lettera in messaggioDaCifrare:
        lettera = ord(lettera) + numeroCar
        nuovaParola += chr(lettera)
    return nuovaParola

par = cifra('Pasquale', 3)
print(par)

def decifra(parola, numeroCar):
    nuovaParola = ""
    for lettera in parola:
        lettera = ord(lettera) - numeroCar
        nuovaParola += chr(lettera)
    return nuovaParola

parola2 = decifra(par, 3)
print(parola2)
