def genNumPrimi(inizio, fine):
    "Raccoglie in un generatore tutti i numeri primi compresi nel range specificato."
    while(inizio <= fine):
        isPrimo = True
        for i in range(2, int(inizio/2 + 1)):
            if (inizio % i == 0):
                isPrimo = False
        if(isPrimo):
            yield inizio
        inizio += 1

print("Primo generatore:")
gen1 = genNumPrimi(3, 9)
for i in gen1:
    print(i)

print("\nSecondo generatore:")
gen2 = genNumPrimi(3, 23)
for i in gen2:
    print(i)

print("\nTerzo generatore:")
gen3 = genNumPrimi(100, 1000)
for i in gen3:
    print(i)
