class MyClass():
    def cmethod(cls):
        print("Metodo di classe")
    cmethod = classmethod(cmethod)                     # Metodo di classe

    def smethod():
        print("Metodo statico")
    smethod = staticmethod(smethod)                    # Metodo statico

MyClass.cmethod()               # Metodo di classe

# I metodo di classe possono essere chiamati sia dalla classe stessa che dalle sue istanze.

MyClass.smethod()
