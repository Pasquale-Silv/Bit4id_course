class Persona():

    civile= True                                 # Variabile di classe
    laurea = True                                # Altra variabile di classe

    def __init__(self, nome, cognome, anni):
        self.nome = nome                         # Variabili d'istanza
        self.cognome = cognome
        self.anni = anni


print(Persona.civile)

io = Persona("Pasquale", "Silvestre", 23)
print(io.civile)

print(isinstance(io, Persona))

tu = Persona("Lucas", "Cincinnati", 28)

print("\nProva su variabile di classe 'laurea':")
print(Persona.laurea)
print(io.laurea)
print(tu.laurea)

print("\nProva cambiando laurea usando la classe:")
Persona.laurea = False           # Chiamando la classe cambierai la variabile di classe, mutandola per tutte le istanze future e già presenti

print(Persona.laurea)
print(io.laurea)
print(tu.laurea)

print("\nProva cambiando laurea usando una sola istanza della classe:")
io.laurea = True                 # Cambiando il valore usando l'istanza, il valore muterà solo per quell'oggetto!

print(Persona.laurea)
print(io.laurea)
print(tu.laurea)

print()
ella = Persona('Anna', 'Palmierina', 21)
print(ella.laurea)

print("\nL'oggetto 'io' avrà una variabile 'cell' che le altre istanze della stessa classe non hanno:")
io.cell = "3889899829"
print("'cell' che SOLO UNA istanza della classe Persona ha:", io.cell)           # l'oggetto 'io' avrà una variabile 'cell' che le altre istanze della stessa classe non hanno!
