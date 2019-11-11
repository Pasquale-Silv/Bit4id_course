# Positional Argument = Fondamentale la posizione mediante la quale vengono passati alla funzione!
# Keyword argument = Ma puoi passarli assegnando esplicitamente il valore al momento della chiamata di funzione, tipo stampa(keyword=valore)
# Puoi usare sia mixing positional and keyword arguments, tipo describe_person('Pasquale', età=23)
# Se hai dei parametri senza un default devi metterli sempre prima

def sommaTutto(*args):                                                             # args viene passato come una tupla!
    print(args)
    print(type(args))
    print("Somma dei valori:", sum(args))
    print()

sommaTutto(3,3,8,2)
sommaTutto()
sommaTutto(0)
sommaTutto(1)
sommaTutto(1,11,22)

print("-------------------------------------------")

def printaTutto(*args):
    print(args)
