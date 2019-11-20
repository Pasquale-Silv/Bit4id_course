# Attributi di classe e di istanza
# Le variabili di classe sono variabili condivise da tutte le istanze di una medesima classe

class Rocket():
    # Rocket simulates a rocket ship for a game,
    # or a physics simulation.

    type = "razzo"                        # Variabile di classe, condivisa tra tutte le istanze di una medesima classe.
    def __init__(self, nome):
        self.nome = nome                      # Variabile di istanza, ogni istanza ha la sua copia privata
        self.x = 0
        self.y = 0

    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

