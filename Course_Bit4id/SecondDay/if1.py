if (not(0)):     # Qualsiasi numero != da 0 è valutato come True(sia numeri positivi che negativi)
    print('This is the first condition!')
else:            # False is None, 0, stringa vuota(""), (not 0)
    print('This is the second condition!')

stringa = ""
if (stringa):
    print("stringa non vuota")
else:
    print('Stringa vuota - False, ossia (' + stringa + ' )')

if None:   # None è un oggetto! In Python tutto è un oggetto!
    print('True')
else:
    print('None is False')

if not(None):
    print('not(None) is True')
else:
    print('None is False')

x = 9 ** 9
y = 10 * 10
z = -70
if(x >= y + z):
    print(x, '>=', y + z)
    if(x >= y + z):
        print("Anche solo x è maggiore o uguale di (y + z)")
else:
    print(y + z, '>', x)

print("---------------------------------------")

if None:
    print('This is True')
else:
    print("This is False, first indentation level")
    if(1):
        print("Second indentation level")
    else:
        print("not True")

print("---------------------------------------")
a = 3
if(a > 0):
    print('Numero positivo')
elif(a == 0):
    print('Numero uguale a 0')
else:
    print('Numero negativo')
