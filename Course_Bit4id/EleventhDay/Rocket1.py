class Rocket():

    tipo = "razzo"
    # Rocket simulates a rocket ship for a game,
    # or a physics simulation.
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y

    def setTipo(cls, nuovoTipo):                                           # Metodo di classe 'cls' = Rocket
        cls.tipo = nuovoTipo
    setTipo = classmethod(setTipo)

    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        # Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment


# Create three rockets.
rockets = [Rocket() for x in range(0,3)]
# Move each rocket a different amount.
rockets[0].move_rocket()
rockets[1].move_rocket(10,10)
rockets[2].move_rocket(-10,0)
# Show where each rocket is.
for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
    print("Variabile di classe:", rocket.tipo)

Rocket.setTipo("razzino")

for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
    print("Variabile di classe:", rocket.tipo)

rockets[0].setTipo("MEGARAZZO, stavolta d'istanza.")

for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
    print("Variabile di classe:", rocket.tipo)

print("\nPoichè hai dichiarato il metodo di classe 'cls', anche se cambi tipo su una singola istanza, "
      "esso sarà cambiato per tutte le istanze della classe in quanto è stato dichiarato come metodo di classe.")
