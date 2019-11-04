myList = list(range(0,21, 2))

print(myList)

for x in range(len(myList)):
    print(myList.pop())
    print(myList)

print("\nVerifichiamo che la lista sia vuota:")
print(myList)
