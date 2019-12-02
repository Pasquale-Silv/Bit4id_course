# Prendi stringa e inverti caratteri della stringa. Per ogni stringa, la ribaltiamo.
# Associare un numero intero a ogni carattere della stringa e separarli con una |pipe| o altro carattere speciale.
# Per associare il numero usa la funzione ord() che restituisce l'equivalente in codice ASCII.
# pipe anche all'inizio e alla fine

import random

# Associazione di un carattere casuale per tutti gli interi generati e per il carattere che li separa.
cifratura = {
    111: "ABC",           # o
    97: "FDS",            # a
    105: "PQL",           # i
    99: "OIM",            # c
    124: "ZNK",           # Pipe |
    32: "poi",            # " "
    80: "uyt",            # P
    115: "rew",           # s
    113: "qas",           # q
    117: "dfg",           # u
    108: "hjk",           # l
    101: "lmn"            # e
}


def inverti_stringa(stringa):
    return stringa[::-1]

def cifra(stringa):
    stringa2 = ""
    for el in stringa:
        stringa2 += str(ord(el)) + "|"
    return "|" + stringa2

def cifra_random(messaggioConPipe):
    mess = messaggioConPipe[1:-1]
    daCifrare = mess.split("|")
    listaCifrata = []
    for elemento in daCifrare:
        elemento2 = int(elemento)
        if elemento2 in cifratura:
            listaCifrata.append(random.choice(cifratura[elemento2]))
    return "|" + "|".join(listaCifrata) + "|"

def decifraMess(messCifrato2):
    messDec = ""
    for lettera in messCifrato2:
        for k, v in cifratura.items():
            if lettera in v:
                messDec += chr(k)
    messDec = messDec.replace("|", "")
    messDec = inverti_stringa(messDec)
    return messDec

def rimuoviPipe(stringa):
    return stringa.replace("|", '')

if __name__ == "__main__":
    parola = "ciao Pasquale"
    parolaRev = inverti_stringa(parola)
    messaggioConPipe = cifra(parolaRev)
    print(messaggioConPipe)
    messCifrato = cifra_random(messaggioConPipe)
    print(messCifrato)
    print("Messaggio cifrato:", rimuoviPipe(messCifrato))
    messDecifrato = decifraMess(messCifrato)
    print("Messaggio decifrato:", messDecifrato)
