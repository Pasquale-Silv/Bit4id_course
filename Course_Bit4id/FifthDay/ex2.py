dictWeightLifting = {
    "Bench press": 3,
    "Shoulder press": 4,
    "Chest press": 5
}

for key, value in dictWeightLifting.items():
    print("I did", value, "times the exercise named", key)

dictWeightLifting['Bench press'] = 11
print()

for key, value in dictWeightLifting.items():
    print("I did", value, "times the exercise named", key)

dictWeightLifting['Push-ups'] = 60
print()

for key, value in dictWeightLifting.items():
    print("I did", value, "times the exercise named", key)

del(dictWeightLifting['Shoulder press'])
print("\nDopo l'eliminazione dell'esercizio 'Shoulder press':\n")
for key, value in dictWeightLifting.items():
    print("I did", value, "times the exercise named", key)
