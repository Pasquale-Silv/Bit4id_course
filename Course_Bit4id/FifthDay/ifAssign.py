# if ternario

età = int(input("Qual è la tua età?"))
stato = "maggiorenne" if (età >= 18) else "minorenne, vai dalla mammina"

print("Hai", età, "anni...", stato)


# ("no", "yes")[True]   ------>       (0, 1) nella tupla, quindi accedi al valore corrispondente a False(0) o True(1)

print("Ciao Pasquale" if(True) else "")
