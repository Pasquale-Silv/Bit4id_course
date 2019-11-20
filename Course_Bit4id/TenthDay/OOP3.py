# La printatura in una classe viene chiamata al momento della definizione della classe, non al momento delle istanze!

a = 80

class Libro():                # La print viene chiamata al momento della creazione/definizione della classe, non al momento della istanza!
    print(a)

l = Libro()                   # Questa istanza non chiamerà la print(a)
