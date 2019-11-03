num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
print("Che operazione aritmetica vuoi effettuare sugli operandi specificati?")
operazione = input("Possibili alternative: +, -, *, / o :, **/^\nScegli:\n")
if(operazione == "+"):
    print("Somma, risultato: ", num1 + num2)
elif(operazione == "*"):
    print("Moltiplicazione, risultato: ", num1 * num2)
elif(operazione == "/" or operazione == ':'):
    if(num2 == 0):
        print("Divisione impossibile, non puoi dividere un numero per", num2)
    else:
        print("Divisione, risultato: ", num1 / num2)
elif(operazione == "-"):
    print("Sottrazione, risultato: ", num1 - num2)
elif(operazione == "**" or operazione == "^"):
    print("Potenza, risultato: ", num1 ** num2)
else:
    print("La scelta da lei effettuata non corrisponde a nessuna delle alternative disponibili")