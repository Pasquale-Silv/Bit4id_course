# Incapsulamento e information hidding
# Ereditarietà, gerarchia
# Polimorfismo, specializzazione
# Modularità e scomposizione del problema

class Persona():

    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età

class Lavoratore(Persona):

    def __init__(self, nome, cognome, età, professione):
        super(Lavoratore, self).__init__(nome, cognome, età)
        self.professione = professione

worker1 = Lavoratore("Pasquale", "Silvestre", 23, "Data Scientist")
print(worker1)
print(worker1.professione)
