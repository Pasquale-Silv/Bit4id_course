def fattoriale(num):
    """Calcola il fattoriale del numero inserito in maniera ricorsiva."""
    if(num <= 1):
        return 1
    else:
        result = num * fattoriale(num - 1)
        return result

prova1 = fattoriale(5)
print(prova1)

prova2 = fattoriale(6)
print(prova2)

prova3 = fattoriale(3)
print(prova3)

prova4 = fattoriale(0)
print(prova4)
