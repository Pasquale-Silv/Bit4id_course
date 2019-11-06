mulOfTen = [num * 10 for num in range(1, 11)]
print("Multipli di dieci:", mulOfTen)

cubeLC = [(x ** 3) for x in range(1, 11)]
print("\nCubo dei primi dieci numeri:", cubeLC)

names = ["Giordano", "Genoveffa", "Lucas", "Markov", "Lino"]
namesLC = [name + " is awesome!" for name in names]

print("\nLC su lista di stringhe di nomi:")
for name in namesLC:
    print(name)

plus_thirteen = []

for x in range(1, 11):
    plus_thirteen.append(x + 13)

print(plus_thirteen)
