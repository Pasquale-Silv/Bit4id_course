cifratura = {
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
        ' ':'z2x45q7yw0'
    }
decifratura = {}

print(cifratura)

for k, v in cifratura.items():
    decifratura[v] = k

print(decifratura)


def cifraMessaggioConfidenziale(messaggioConfidenziale):
        messaggioConfidenziale = messaggioConfidenziale.lower()
        parolaCifrata = ''
        for lettera in messaggioConfidenziale:
                for k in cifratura.keys():
                        if lettera == k:
                                parolaCifrata += cifratura[k]
        return parolaCifrata

def decifraMessaggioConfidenziale(parolaCifrata):
    parolaDecifrata = ''
    for i in range(0, len(parolaCifrata), 10):
        for k in decifratura.keys():  # Chiavi tuple
            if parolaCifrata[i:i + 10] == k:
                parolaDecifrata += decifratura[k]
                break
    return parolaDecifrata


parolaCifrata = cifraMessaggioConfidenziale('Il cane abbaia troppo')
print("\nParola Cifrata: " + parolaCifrata)

print("\nDECIFRATURA:")
parolaDecifrata = decifraMessaggioConfidenziale(parolaCifrata)
print(parolaDecifrata)

print("\nPROVA CON UN'ALTRA PAROLA:")
messaggio = "La guerra sta per iniziare, preparatevi!"
parolaCif = cifraMessaggioConfidenziale(messaggio)
print(parolaCif)
parolaDecif = decifraMessaggioConfidenziale(parolaCif)
print(parolaDecif)