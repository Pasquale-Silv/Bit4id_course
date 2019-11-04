list1 = []

for num in range(1, 11):
    list1.append(num * 10)

print(list1)

list2 = []

for num in range(1, 11):
    list2.append(num ** 3)

print(list2)

namesList = ["Pasquale", "Giulio", "Alfonso", "Luca", "Bruno"]
namesList2 = []
i = 0
for name in namesList:
    namesList2.append(namesList[i] + " is awesome!")
    i +=1

print(namesList)
print(namesList2)
