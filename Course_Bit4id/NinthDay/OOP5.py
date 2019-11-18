class MyClass:         # Una classe eredita direttamente o indirettamente da 'object'
    pass

class MyClass2(object):                   # Preferita      'Object' è il supergenitore di tutti!
    pass

class MyClass3():
    pass

istanzaX = MyClass()   # Crea una istanza della classe MyClass.
print(istanzaX)