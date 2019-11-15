def isPrimo(numInt):
    "Restituisce True se un numero è primo, altrimenti False."
    for i in range(2, numInt):
        if(numInt % i == 0):
            return False
    return True

def genNumPrimi2func(inizio, fine):
    "Raccoglie in un generatore tutti i numeri primi compresi nel range specificato."
    while(inizio <= fine):
        if(isPrimo(inizio)):
            yield inizio
        inizio += 1

gen1 = genNumPrimi2func(23, 43)
print(gen1)
print(type(gen1))

for i in gen1:
    print(i, end=" ")
print()

gen2 = genNumPrimi2func(100, 201)
for i in gen2:
    print(i, end=" ")
