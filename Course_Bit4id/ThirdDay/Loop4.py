myNumericList = [3, 5, 10, 24]

x = 0
somma = 0
media = 0

while(x < len(myNumericList)):
    somma += myNumericList[x]
    print(myNumericList[x])
    x += 1
else:                      # else viene printato se il while non viene bruscamente interrotto, stessa cosa per il for
    print("Somma dei valori ciclati:", somma)
    media = round((somma / len(myNumericList)), 2)
    print("Media dei valori ciclati:", media)

