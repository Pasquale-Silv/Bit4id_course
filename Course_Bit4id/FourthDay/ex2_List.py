names = ["Pasquale", "Bruno", "Lucia", "Antonio", "Giacomo", "Barbara", "Giorgia"]
names2 = ["John"]

if(len(names) >= 3):

    while(len(names) > 5):
        print("C'è un casino nella stanza, VIA!")
        print("Via", names.pop())

    while (len(names) >= 3):
        print("La stanza è affollata, liberare!")
        print("Via", names.pop())

elif(len(names) >= 1):
    print("La stanza non è affollata")
elif(len(names) == 0):
    print("Non c'è nessuno in stanza.")
else:
    print("Non riconosco il parametro!")

print("\nPersone in stanza:", names, ", ottimo!")
