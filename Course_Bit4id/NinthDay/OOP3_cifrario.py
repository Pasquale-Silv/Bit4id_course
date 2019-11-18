class Cifrario():

    def __init__(self, parolaDaCifrare, numeroCar):
        self.parola = parolaDaCifrare
        self.numero = numeroCar

    def cifra(self):
        self.parolaCifrata = ""
        for lettera in self.parola:
            lettera = ord(lettera) + self.numero
            self.parolaCifrata += chr(lettera)
        return self.parolaCifrata

    def decifra(self):
        self.parolaDecifrata = ""
        for lettera in self.parolaCifrata:
            lettera = ord(lettera) - self.numero
            self.parolaDecifrata += chr(lettera)
        return self.parolaDecifrata

parola = Cifrario("Pasquale", 3)
parolaCifrata = parola.cifra()
print(parolaCifrata)
parolaDecifrata = parola.decifra()
print(parolaDecifrata)
