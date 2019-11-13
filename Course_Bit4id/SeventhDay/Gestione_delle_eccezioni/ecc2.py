list_of_numbers = [0, 1, 2]

dictionary_of_numbers = {}

for number in list_of_numbers:
     dictionary_of_numbers[number ** 2] = number

print(dictionary_of_numbers)

try:
    index = list_of_numbers.index(2)
    value = dictionary_of_numbers[index]                   # There is no key 2 in the dictionary that you created.
except (ValueError, KeyError):                             # KeyError beccato!
    print("Error raised, but controlled!")
else:
    # This executes ONLY if no exception is raised
    print("Getting number at position %d : %d" % (index, value))
finally:
    # Do cleanup operations
    print('Cleaning up!')


risp = input("Vuoi beccare la KeyError arbitraria? s/n:\n").lower()
if(risp == 's'):
    raise KeyError("\nHai beccato la KeyError per mia volontà, non ti faccio proseguire!\n")


print("\nPoichè hai gestito l'eccezione il programma continua la sua esecuzione fin qui!")
print("Complimenti!")
