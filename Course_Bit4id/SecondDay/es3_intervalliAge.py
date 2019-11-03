num = int(input("Inserisci un numero: "))
if(num >= 0 and num <= 18):
    print("Il numero", num, " è compreso nell'intervallo 0-18")
elif(num >= 19 and num <= 30):
    print("Il numero", num, " è compreso nell'intervallo 19-30")
elif(num >= 31 and num <= 60):
    print("Il numero", num, " è compreso nell'intervallo 31-60")
elif(num >= 61 and num <= 90):
    print("Il numero", num, " è compreso nell'intervallo 61-90")
elif(num > 90):
    print("Il numero", num, " è maggiore di 90 !")
else:
    print("il numero", num, " non è compreso negli intervalli specificati !")
