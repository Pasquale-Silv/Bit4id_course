# self è il riferimento all'istanza su cui il metodo è chiamato!

class Animale():
    tipo = 'Cigno'                                                                   # static ----> Variabile di classe.
    variabileDiClasse = "Sono una variabile di classe   -------->    STATIC in java!"

animale1 = Animale()

print(animale1.tipo)
print(Animale.tipo)                                                        # 'tipo' variabile di classe. (like 'static')
print(Animale.variabileDiClasse)

animale2 = Animale()

print(animale2.variabileDiClasse)

print("\nOra printiamo la classe e le sue istanze:")
print(Animale)
print(animale1)
print(animale2)
