def contoAllaRovescia(tettoMax):
    """Conta alla rovescia a partire dal numero passato come argomento."""
    if(tettoMax <= 0):
        print("Via!")
    else:
        print(tettoMax)
        contoAllaRovescia(tettoMax-1)

print("Conto alla rovescia da 3:")
contoAllaRovescia(3)

print("\nConto alla rovescia da 10:")
contoAllaRovescia(10)

print("\nConto alla rovescia da 7:")
contoAllaRovescia(7)
