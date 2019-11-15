# Adenina Guanina Timina Citosina             codone = tre nucleotidi in sequenza

gene_str = 'AAACCCACTGACTGAAAACCCTTTGGGGTACAAAATCCAAACTTGGGTCCTTTCGTCCCCCCCAAACCCGTCCCC'

def quantiCodoni(stringaNuc):
    "Scopri quanti codoni contiene una struttura DNA."
    leng = (len(stringaNuc))
    codoni = leng / 3
    print("Il numero dei codoni presenti è:", codoni)

def contaCreaCodoni(stringaNuc):
    """
    Elabora e restituisce un dizionario contenente i codoni presenti nella stringa passata in argomento come chiave
    e la frequenza della sequenza(codone) come valore.
    """
    try:
        if(len(stringaNuc) % 3 == 0):
            nuovo_dict = {}
            for i in range(0, len(stringaNuc), 3):
                if stringaNuc[i:i+3] in nuovo_dict.keys():
                    nuovo_dict[stringaNuc[i:i+3]] += 1
                else:
                    nuovo_dict[stringaNuc[i:i + 3]] = 1
            return nuovo_dict
        else:
            return "Controllare meglio la struttura della stringa inserita, " \
                   "numero di nucleotidi incongruente con l'operazione richiesta."
    except:
        return "Controllare meglio la struttura della stringa inserita, " \
               "numero di nucleotidi incongruente con l'operazione richiesta."

def cercaCodone(strutturaDNA, nucleotideSpecifico):
    """
    Ricerca se è presente uno specifico nucleotide all'interno di una data struttura del DNA;
    inoltre quantifica tale frequenza.
    """
    try:
        if(nucleotideSpecifico in strutturaDNA.keys()):
            print("Il nucleotide '{}' è presente nella struttura DNA in esame.".format(nucleotideSpecifico))
            print("Numero di volte in cui è presente:", strutturaDNA[nucleotideSpecifico], "\n")
        else:
            print("Il nucleotide indicato({}) non è presente nella struttura DNA in esame.\n".format(nucleotideSpecifico))
    except:
        print("Controllare meglio la struttura della stringa inserita, "
               "numero di nucleotidi incongruente con l'operazione richiesta.")

strutturaDati = contaCreaCodoni(gene_str)
print(strutturaDati, "\n")

cercaCodone(strutturaDati, 'CCC')
cercaCodone(strutturaDati, 'AGT')
cercaCodone(strutturaDati, 'TTC')
cercaCodone(strutturaDati, 'AAA')
