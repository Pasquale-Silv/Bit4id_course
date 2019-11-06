animal = "dog"
animals = ["dog", "cat", "mouse", "horse", "turtle"]

# Sono placeholder
# %s    s sta per string
# %d    d sta per digit(cifra)

print("I have a %s" % animal)

print("I have a %s, a %s and a %s." % (animals[0], animals[1], animals[-1]))  # Passi gli argomenti come tuple

number = 23
numbers = [23, 25, 26, 44, 33, 3.8]
print("My age is %d years old." % number)
print("My age is %d, my favourite number is %d and a float is like %f.Good luck by now." %(numbers[0], numbers[2], numbers[-1]))

# Puoi anche mischiare i vari placeholder %s, %d
