x = lambda a : a + 5           # Funzione anonima
print(x(30))

print((lambda x: x % 2 and 'odd' or 'even')(7))
print((lambda x: x % 2 and 'odd' or 'even')(8))
print((lambda x: x % 2 and 'odd' or 'even')(2))
print((lambda x: x % 2 and 'odd' or 'even')(3))

uno = (lambda x, y: x + y)(5, 6)
print("\n", uno)
