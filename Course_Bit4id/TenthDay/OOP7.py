class Gatto():

    tipo="felino"                         # Variabile/Attributo di classe

    def __init__(self, nome, anni, fidanzato=False, padrone=None):
        self.nome = nome
        self.anni = anni
        self.fidanzato = fidanzato
        self.padrone = padrone


g1 = Gatto("Fuffy", 3)
g2 = Gatto("Ciccy", 6, fidanzato=True)
g3 = Gatto("Annabelle", 2, False, "Giulio")

print(Gatto.tipo)
print(g1.tipo)
print(g2.tipo)
print(g3.tipo)

print("\nMutando la variabile di classe mediante istanza, essa muterà solo per l'oggetto in questione:")
g2.tipo = "tuccino"

print(Gatto.tipo)
print(g1.tipo)
print(g2.tipo)
print(g3.tipo)


print("\nMutando la variabile di classe utilizzando la classe stessa, "
      "cambierò anche tutte le variabili di tutte le istanze future e già presenti,"
      "tranne di quelle sovrascritte già, come nel precedente caso di g2:")

Gatto.tipo = "cluster"

print(Gatto.tipo)
print(g1.tipo)
print(g2.tipo)
print(g3.tipo)

print("\nAdesso vediamo se i gatti sono fidanzati:")
print(g1.fidanzato)
print(g2.fidanzato)
print(g3.fidanzato)

print("\nAdesso vediamo chi sono i padroni dei gatti:")
print(g1.padrone)
print(g2.padrone)
print(g3.padrone)
