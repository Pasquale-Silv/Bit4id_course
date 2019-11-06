names = ["Pasquale", "Bruno", "Lucia", "Antonio", "Giacomo"]


while(len(names) >= 3):
    print("La stanza è affollata, liberare!")
    print("Via", names.pop())

if(len(names) < 3):
    print("La stanza non è affollata!")

print("\nPersone in stanza:", names, ", ottimo!")
