def greeting(person):
    """Prende come argomento un nome di persona e lo ringrazia per un consiglio."""
    print("Hi my dear %s," % person)
    print("Greetings for your advice, dear %s" % person)
    print("I really hope you are fine, my dear %s, enjoy your day!\n" % person)

greeting("Pasquale")
greeting("Giulio")
greeting("Mario")

print("\nAdesso con la funzione che prende una lista come argomento:\n")

def greetingList(individui):
    """Prende come argomento una lista di individui e li ringrazia individualmente per un consiglio."""
    for individuo in individui:
        print("Hi my dear %s," % individuo)
        print("Greetings for your advice, dear %s" % individuo)
        print("I really hope you are fine, my dear %s, enjoy your day!\n" % individuo)


listaIndividui = ["Giacobbe", "Armando", "Genoveffa", "Carmine"]

greetingList(listaIndividui)
