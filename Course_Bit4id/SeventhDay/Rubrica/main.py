# Rubrica con nome, cognome, numero di cell
# Aggiungere, rimuovere, cercare, modificare ed elencare contatti

from Course_Bit4id.SeventhDay.Rubrica.funzioni import rimuoviContatto, elencaContatti, cercaContatto, aggiungiContatto, modificaContatto, rubrica

print("Aggiungi contatti:")
aggiungiContatto(1 ,"Pasquale", "Silvestre", "3889988765")
aggiungiContatto(2, "Lanny", "Piscopo", "3889988765")
aggiungiContatto(3, "Luca", "Colucci", "3889988765")
aggiungiContatto(4, "Alfonso", "Silvestre", "3889988765")

print(rubrica)

print("\n\nRimozioni:")
rimuoviContatto(10, "Giacomo")
rimuoviContatto(2, "Lanny")
print()

print(rubrica)

print("\n\nElenca contatti:")
elencaContatti(rubrica)

print("\n\nCerca contatto:")
cercaContatto(4, "Alfonso")

print("\nModifica contatti:")
modificaContatto(3, "Luca")
print("PROVA:", rubrica[3])    # Luca riepilogo
modificaContatto(2, "Filippo")
