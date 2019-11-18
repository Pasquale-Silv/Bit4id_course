class CifrarioAvanzato():

    def __init__(self, messaggioConfidenziale):
        self.messaggioConfidenziale = messaggioConfidenziale.lower()
        self.cifratura = {
                            'a':'jdsjl43315',
                            'b':'dvnhm79114',
                            'c':'12617ghd19',
                            'd': '45433gfd13',
                            'e': '98bbbv2115',
                            'f': '008767ggv3',
                            'g': 'jdsjl43321',
                            'h': 'dvnhm7922q',
                            'i': '12617ghd3r',
                            'l': '45433gfd4v',
                            'm': '98bbbv2554',
                            'n': '008767ggvx',
                            'o': 'jdsjl43387',
                            'p': 'dvnhm7977z',
                            'q': '12617ghd0v',
                            'r': '45433gfd9c',
                            's': '98bbbv288y',
                            't': '008767ggvj',
                            'u':'67ghgwjdvn',
                            'v':'798ghvshc ',
                            'z':'jdyvghc32e',
                            ' ':'z2u45y7891'
                        }
        self.decifratura = {v:k for k, v in self.cifratura.items()}

    def cifraMessaggioConfidenziale(self):
        self.parolaCifrata = ''
        for lettera in self.messaggioConfidenziale:
            for k in self.cifratura.keys():
                if lettera == k:
                    self.parolaCifrata += self.cifratura[k]
        return self.parolaCifrata

    def decifraMessaggioConfidenziale(self, decifratura):
        self.parolaDecifrata = ''
        for k in decifratura.keys():
            for lettera in self.parolaCifrata:
                if lettera == k:
                    self.parolaDecifrata += decifratura[k]
        return self.parolaDecifrata


def decifraMessaggioConfidenziale(parolaCifrata, decifratura):
    parolaDecifrata = ''
    for i in range(0, len(parolaCifrata), 10):
        for k in decifratura.keys():  # Chiavi tuple
            if parolaCifrata[i:i + 10] == k:
                parolaDecifrata += decifratura[k]
                break
    return parolaDecifrata



parola = CifrarioAvanzato('il cane abbaia troppo')
print(parola.decifratura)

print("\nCIFRATURA:")
parola_cifrata = parola.cifraMessaggioConfidenziale()
print(parola_cifrata)

print("\nDECIFRATURA:")
parolaDecifrata = decifraMessaggioConfidenziale(parola_cifrata, parola.decifratura)
print("Parola decifrata:", parolaDecifrata)
