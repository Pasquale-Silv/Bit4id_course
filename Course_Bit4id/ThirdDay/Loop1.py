colors = ['black', 'blue', 'red', 'green']

for index in range(len(colors)):
    print(colors[index])

print()

for color in colors:
    print(color)

print()

for i in range(0, 11, 2):
    print(i)

# If you want to enumerate a list, you need to add an index variable to hold the current index
# enumerate()    ---------------------..-> enumerate torna una tupla con indice e valore (index, color)
print("\nProviamo enumerate():")
for index, color in enumerate(colors):
    print("Indice:", index, ", color:", color)

# In for loops Python allows 'break' and 'continue', like Java does.