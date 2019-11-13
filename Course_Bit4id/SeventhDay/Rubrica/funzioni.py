rubrica = {}

def aggiungiContatto(id, nome, cognome, numero_di_cellulare, dizionario=rubrica):
    """
    Aggiunge un nuovo contatto alla rubrica con gli argomenti passati, i contatti sono salvati in un dizionario avente
    come chiave l' id univoco del contatto e come valore un altro dizionario avente i dati informativi del contatto.
    """
    if (id in dizionario):
        print("Il contatto con tale id({}) è già presente in rubrica, esso è {}.".format(id, dizionario[id]))
        print("Quindi non è possibile proseguire, per la modifica è prevista un'altra procedura.")
        return
    dizionario[id] = {"nome":nome, "cognome":cognome, "cell":numero_di_cellulare}

def rimuoviContatto(id, nome, dizionario=rubrica):
    "Rimuove un contatto dalla rubrica."
    if id in dizionario:
        del dizionario[id]
        print("Il contatto %s è stato correttamente rimosso dalla rubrica." % nome)
    else:
        print("Il contatto selezionato non esiste in rubrica! %s inesistente!" % nome)

def elencaContatti(dizionario=rubrica):
    "Mostra tutti i contatti presenti in rubrica."
    for chiave, valore in dizionario.items():
        print("Matricola-chiave del contatto:", chiave, "\n\t\tDati del contatto:", valore )

def cercaContatto(id, nome, dizionario=rubrica):
    "Cerca un contatto in rubrica mediante suo id e nome."
    if(dizionario[id]['nome'] == nome):
        print("Contatto trovato, ecco i dati del contatto %s" % nome)
        print(dizionario[id]['nome'], ":", dizionario[id])
    else:
        print("In rubrica non esiste il contatto selezionato! Contatto %s inesistente" % nome)

def modificaContatto(id, nome, dizionario=rubrica):
    "Modifica un dato contatto già presente in rubrica."
    try:
        if id in dizionario:
            if dizionario[id]['nome'] == nome:
                print("Hai scelto di modificare il contatto {}".format(dizionario[id]))
                modifica = input("Cosa vuoi modificare? nome / cognome / cell\n").lower()
                if(modifica == "nome" or modifica == "cognome" or modifica == "cell"):
                    nuovoValore = input("Inserisci il nuovo valore: ")
                    dizionario[id][modifica] = nuovoValore
            else:
                print("Matricola esatta...Ma nessun nome corrisponde a quello digitato o semplicemente non è quello associato alla matricola inserita({}), quindi impossibile proseguire.".format(nome))
        else:
            print("Nessuna matricola corrisponde a quella digitata, ossia matricola digitata:{}.".format(id))

        print("Riepilogo del contatto: {}".format(dizionario[id]))
    except KeyError:
        print("Nella rubrica non è presente la chiave selezionata! id:{} inesistente in rubrica (KeyError evitato)".format(id))
