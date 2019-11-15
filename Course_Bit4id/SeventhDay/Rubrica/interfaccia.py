from Course_Bit4id.SeventhDay.Rubrica.funzioni import aggiungiContatto, elencaContatti, rimuoviContatto, \
    mostraChiaviRubrica, cercaContatto, modificaContatto

username = "Pasquale-admin"
password = "rubrica01"

def interfacciaUtente():
    print("  _________________________________________________________        \n" 
          " /                                                         \       \n"
          "|  1 - Aggiungi contatto                                    |      \n"
          "|  2 - Mostra elenco contatti                               |      \n"
          "|  3 - Rimuovi contatto                                     |      \n"
          "|  4 - Cerca contatto già presente                          |      \n"
          "|  5 - Modifica contatto presente in rubrica                |      \n"
          "|  Premi qualsiasi altro tasto per terminare le operazioni. |      \n"
          " \__________________________________________________________/      ")

def chiediOperazioneAgain():
    op = int(input("\n\nQuale operazione desideri effettuare sulla tua rubrica?\n"))
    return op


def autenticazioneRubrica():
    print("Benvenuto nella tua rubrica personale, desideri avviare l'interfaccia?")
    risp = input("Scegli si/no per proseguire:\n").lower()
    if (risp == "si" or risp == "s"):
        user = input("username: ")
        psw = input("password: ")
        if(user == username and password == psw):
            print("\nBenvenuto Pasquale-admin, proceda con le operazioni da amministratore :)\n")
            interfacciaUtente()
            operazione = int(input("\nQuale operazione desideri effettuare sulla tua rubrica?\n"))

            try:
                while (operazione in [1, 2, 3, 4, 5]):
                    if (operazione == 1):
                        print("Ricorda che gli id già presenti sono: ", mostraChiaviRubrica())
                        print("Inserisci i dati del contatto che intendi aggiungere alla rubrica")
                        id = int(input("id: "))
                        nome = input("nome: ")
                        cognome = input("cognome: ")
                        cell = input("numero di cellulare: ")
                        aggiungiContatto(id, nome, cognome, cell)
                        interfacciaUtente()
                        operazione = chiediOperazioneAgain()
                    elif (operazione == 2):
                        elencaContatti()
                        interfacciaUtente()
                        operazione = chiediOperazioneAgain()
                    elif (operazione == 3):
                        print("Ricorda che gli id già presenti sono: ", mostraChiaviRubrica())
                        print("Inserisci i dati del contatto che intendi rimuovere:")
                        id = int(input("id: "))
                        nome = input("nome: ")
                        rimuoviContatto(id, nome)
                        interfacciaUtente()
                        operazione = chiediOperazioneAgain()
                    elif (operazione == 4):
                        print("Inserisci i dati del contatto da cercare:")
                        id = int(input("id: "))
                        nome = input("nome: ")
                        cercaContatto(id, nome)
                        interfacciaUtente()
                        operazione = chiediOperazioneAgain()
                    elif (operazione == 5):
                        print("Inserisci i dati del contatto da modificare:")
                        id = int(input("id: "))
                        nome = input("nome: ")
                        modificaContatto(id, nome)
                        interfacciaUtente()
                        operazione = chiediOperazioneAgain()
                    else:
                        print("L'operazione da lei inserita non è contemplata.\nRiprovare inserendo un carattere valido(numero da 1 a 5)")
                        interfacciaUtente()
                        operazione = chiediOperazioneAgain()
            except ValueError:
                print("Inserire solamente numeri interi da 1 a 5.")
        else:
            print("Username o password errati...Impossibile proseguire.")
    elif(risp == "no" or risp == "n"):
        print("Come desidera,\nOperazione conclusa.")
    else:
        print("Risposta non riconosciuta, inserire solamente i caratteri validi s/n")
