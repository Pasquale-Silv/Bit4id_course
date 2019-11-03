from datetime import date

print("Benvenuto in questo programma che calcola i secondi intercorrenti tra due diverse date.")

print("Inserisci la prima data:")
giorno1 = int(input("Giorno: "))
mese1 = int(input("Mese: "))
anno1 = int(input("Anno: "))

data2 = print("Inserisci seconda data: ")
giorno2 = int(input("Giorno: "))
mese2 = int(input("Mese: "))
anno2 = int(input("Anno: "))

print("\n\nControllando le date fornite...Attendere con pazienza")
print("Attendere l'esito del controllo...")

formatoDataValido = True
if((giorno1 <= 0 or giorno1 >30) or ((giorno2 <= 0 or giorno2 >30))):
    print("formato giorni non valido in una delle due date!")
    formatoDataValido = False
if((mese1 <= 0 or mese1 > 12) or (mese2 <= 0 or mese2 > 12)):
    print("Formato mese non valido in una delle due date!")
    formatoDataValido = False
if((anno1 <= 1900 or anno1 > 2050) or (anno2 <= 1900 or anno2 > 2050)):
    print("Formato anno non valido in una delle due date!")
    formatoDataValido = False



if(formatoDataValido):
    print("Le date sono state inserite nel formato corretto")
    print("\nAdesso calcoliamo i secondi intercorrenti tra le date: ")
    giornoSec = 60 * 60 * 24
    meseSec = giornoSec * 30
    annoSec = meseSec * 12
    data1 = "Prima data inserita: {}/{}/{}".format(giorno1, mese1, anno1)
    data2 = "Seconda data inserita: {}/{}/{}".format(giorno2, mese2, anno2)
    print(data1)
    print(data2)
    data1 = date(anno1, mese1, giorno1)
    data2 = date(anno2, mese2, giorno2)
    giorniDiff = data2 - data1
    print("Giorni di differenza tra le due date: {}.".format(giorniDiff))
    secDiff = giorniDiff.days * giornoSec
    print("\nLa differenza espressa in secondi in riferimento alle date fornite è: {}.".format(secDiff))
else:
    print("\nSiccome una delle due date è stata inserita nel formato non corretto, risulta impossibile proseguire!")
