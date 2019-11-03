first_name = input("Insert your name:")          # input(...) trasforma qualsiasi cosa nel tipo 'stringa'
last_name = input("Insert your lastname:")
age = input("Insert your age:")
print("Welcome", first_name, last_name, ", your age is", age)

if (int(age) >= 18):
    print("Sei maggiorenne, signor", first_name, last_name)
else:
    print("Sei minorenne, signor", first_name, last_name)

print("Vuoi rispondere ad altre domande?")
risposta = input("Rispondi s/n")
if(risposta == "s"):
    numCell = input("Qual è il tuo numero di cellulare?")
    spos = input("Sei sposato?")
    print("Scheda personale:", first_name, last_name, ",hai", age, "anni", ",il tuo numero di cellulare è:", numCell)
else:
    print("Ok, grazie per l'attenzione!")
