colors = ['red', 'green', 'blue', 'black']
color = colors[0]
print(color)

green_color = colors[1]
print(green_color)

black_color = colors[-1]
print(black_color)

green_color_again = colors[-3]
print(green_color_again)

print()

for color in colors:
    print(color)

# Riassegna il primo colore
colors[0] = 'orange'
print(colors)

# Metdodo per controllare l'indice di un dato elemento
print("Index of 'black' in list colors:", colors.index('black'))

# print(colors.index('violet'))     =======>   Genererà un ValueError poichè 'violet' non è presente nella lista colors

print()
print('orange' in colors)
print('violet' in colors)
print('black' not in colors)
print('black' in colors)

colors.append('violet')         # Viene aggiunto alla fine
print(colors)
print(colors.index('violet'))

colors.insert(1, 'yellow')    # Inserisci un dato valore in uno specifico indice
print(colors)
colors.insert(0, 'brown')
print(colors)

colors.insert(100, 'pink')      # Trasforma in .append() se l'indice è outOfBound !
print(colors)
print(colors.index('pink'))
del(colors[1])                  # Elimina per indice
print(colors)
colors.remove('violet')         # Elimina per 'contenuto' , ricorda che rimuove solo la prima occurence!
print(colors)

colore_pop = colors.pop(3)      # poppare = tornare il valore e poi rimuoverlo dalla lista! In this case index is 3
print(colore_pop)
print(colors)
colore_pop_default = colors.pop()    # Se non gli passi nessun indice poppa l'ultimo elemento!
print(colore_pop_default)
print(colors)

lunghezzaLista = len(colors)
print("Lunghezza della lista colors:", lunghezzaLista)
