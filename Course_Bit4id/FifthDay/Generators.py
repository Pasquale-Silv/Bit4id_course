# In Python there are no tuple comprehensions... But you can have generators!
# Generator Comprehensions - GC

gen1 = (number for number in range(1, 6))

print(gen1)
print(type(gen1))

for x in gen1:
    print(x)

# Il generatore non va a occupare la memoria! Si esaurisce a runtime!
# Quindi utilissimo per scorrere e acquisire file di enorme dimensione

genToList = list(gen1)
print(genToList)            # Poichè il generatore si esaurisce non vengono aggiunti elementi alla lista, si è esaurito e bisogna ricrearlo!

gen1 = (number for number in range(1, 6))
genToList = list(gen1)
print(genToList)
