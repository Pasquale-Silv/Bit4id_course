class GiochiDiParole():

    lista_parole = ["fare", "giocare", "dormire", "fittizio", "lira", "sirena", "fulmine", "polizia", "carabinieri",
                    "luce", "oscuro", "siluro", "razzo", "pazzo", "sillaba", "tono", "oro", "argento", "moneta",
                    "panna", "zanna", "simulare", "creare", "mangiare", "rubare", "ridere"]

    lista_anagramma = [list(parola) for parola in lista_parole]

    def __init__(self, parola):
        self.parola = parola

    def isPalindroma(self):
        parola = self.parola.lower()
        parolaContrario = parola[::-1]
        if parola == parolaContrario:
            return True
        else:
            return False

    def rimario(self):
        rime = []
        parola = self.parola.lower()
        for elemento in self.lista_parole:
            if elemento[-3:] == parola[-3:]:
                rime.append(elemento)
        if (not rime):
            print("Non sono state trovate rime corrispondenti alla parola '{}'!".format(self.parola))
        else:
            print(f"Le rime corrispondenti alla parola '{parola}' sono le seguenti: {rime}")

    # def anagramma(self):
    #     parola = list(self.parola.lower())
    #     anagrammi = []
    #     for lettera in parola:
    #         for
    #
    #                         print(f"La parola{self.parola} e {elemento} sono anagrammi!")
    #     else:
    #         print("Nessun anagramma!")



if __name__ == "__main__":
    parola1 = GiochiDiParole("Salvare")
    print(parola1.isPalindroma())
    parola1.rimario()

    parola2 = GiochiDiParole("AnNA")
    print(parola2.isPalindroma())
    parola2.rimario()

    parola3 = GiochiDiParole("Scarpa")
    print(parola3.isPalindroma())
    parola3.rimario()

    print(GiochiDiParole.lista_anagramma)