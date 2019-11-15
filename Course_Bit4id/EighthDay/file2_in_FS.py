file = 'C:/Users/Student-004/Documents/fileUno.txt'    # \ diventa / del normale percorso su cmd

conFile = open(file, 'r')                # Connessione al file
print(type(conFile))

for line in conFile:
    print(line)
conFile.close()

print("-------------------------------")

conFile = open(file, 'r')
print(conFile.readline())
print(conFile.readline())
print(conFile.readline())
print(conFile.readline())
conFile.close()
