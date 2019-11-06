num = int(input("Scegli l'intero:\n"))

listDiv = []

for x in range(2, int(num / 2) + 2):
    if(num % x == 0):
        listDiv.append(x)

print(listDiv)

if(not(listDiv)):
    print("Il numero inserito è un numero primo!")
