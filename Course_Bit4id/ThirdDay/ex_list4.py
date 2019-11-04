squareList = [x ** 2 for x in range(11)]

print(squareList)

list1 = squareList[3:]
print(list1)

print(squareList[-5:])
print(squareList[:-7])
print(squareList[:])
print(squareList[4:-1])

list2= []
print(list2)
list2.extend(squareList[5:10])
print(list2)

print("-------------------------------------------")

emptyList = []
print(emptyList)
for num in range(1, 11):
    emptyList.append(num ** 2)

print(emptyList)
