# Attributi magici o speciali
# __name__     attributo che contiene il nome della classe
# __module__   attributo che contiene il modulo in cui è contenuta la classe
# __class__    attributo che permette di ottenere la classe di un oggetto

class Rocket():
    # Rocket simulates a rocket ship for a game,
    # or a physics simulation.
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0

    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


print("Attributo magico __name__:\n", Rocket.__name__)
print("Attributo speciale __module__:\n", Rocket.__module__)
print(Rocket.__class__)
rocket1 = Rocket()
print(rocket1.__class__)

print("\nCon lista:")
lista1 = [3, 6]

print(lista1.__class__)

print(isinstance(lista1, list))
print(isinstance(lista1, int))
print(isinstance(3.54, float))
print(isinstance(rocket1, Rocket))
print(isinstance({4:5,7:9}, Rocket))
print(isinstance((2, 4), tuple))
print(isinstance({4:5,7:9}, dict))
print(isinstance("Pasquale", str))
