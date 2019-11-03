num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
print("Che operazione aritmetica vuoi effettuare sugli operandi specificati?")
operazione = input("Possibili alternative: +, -, *, /, **/^\nScegli:\n")
if(operazione == "+"):
    risultato = num1 + num2
    print("Somma, risultato: ", risultato)
elif(operazione == "*"):
    risultato = num1 * num2
    print("Moltiplicazione, risultato: ", risultato)
elif(operazione == "/"):
    risultato = num1 / num2
    print("Divisione, risultato: ", risultato)
elif(operazione == "-"):
    risultato = num1 - num2
    print("Sottrazione, risultato: ", risultato)
elif(operazione == "**" or operazione == "^"):
    risultato = num1 ** num2
    print("Potenza, risultato: ", risultato)
else:
    print("La scelta da lei effettuata non corrisponde a nessuna delle alternative disponibili")

scelta = input("Desideri salvare questo valore in memoria per possibili riutilizzi?  S/N:\n").upper()
if (scelta == "S"):
    print("Il numero ", risultato, "è stato salvato in memoria")
else:
    risultato = 0

print("Vuoi effettuare un nuovo calcolo?")
redo = input("S/N: \n").upper()
if (redo == "S"):
    print("Ricorda che il risultato precedente era", risultato)
    riutilizzo = input("Desideri riutilizzarlo? S/N: \n").upper()
    if(riutilizzo == "S"):
        num1 = risultato
    else:
        num1 = float(input("Inserisci primo numero: "))
    num2 = float(input("Inserisci secondo numero: "))
    print("Che operazione aritmetica vuoi effettuare sugli operandi specificati?")
    operazione = input("Possibili alternative: +, -, *, /, **/^\nScegli:\n")
    if(operazione == "+"):
        risultato = num1 + num2
        print("Somma, risultato: ", risultato)
    elif(operazione == "*"):
        risultato = num1 * num2
        print("Moltiplicazione, risultato: ", risultato)
    elif(operazione == "/"):
        risultato = num1 / num2
        print("Divisione, risultato: ", risultato)
    elif(operazione == "-"):
        risultato = num1 - num2
        print("Sottrazione, risultato: ", risultato)
    elif(operazione == "**" or operazione == "^"):
        risultato = num1 ** num2
        print("Potenza, risultato: ", risultato)
    else:
        print("La scelta da lei effettuata non corrisponde a nessuna delle alternative disponibili")