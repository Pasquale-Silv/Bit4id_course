nomi = ["Pasquale", "Alfonso", "Luca"]

for nome in nomi:
    print(nome)

risp = int(input("\nQuanti nomi presenti nella lista vuoi vedere?\n"))

try:
    for i in range(0, risp):
        print(nomi[i])
except (IndexError):            # Se non specifichi nessun tipo di errore, Python catturerà tutti i tipi d'errore sollevabili(portata generale)
    print("Sei andato fuori dal range degli indici della lista!")
    print("Numero massimo di nomi in lista:", len(nomi))
else:
    print("Qua ci arrivi solo se va tutto bene !")
finally:
    print("Io sono l'onnipresente finally ! mi vedrai sempre!")


print("\nQua non ci arrivi se non gestisci tutte le possibili eccezioni verificabili!")
