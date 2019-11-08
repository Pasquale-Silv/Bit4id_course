def fullNamePrintedRet(firstname, lastname):
    str = "Il tuo nome è %s %s, ricordalo!" % (firstname, lastname)
    return str

primo = fullNamePrintedRet("Pasquale", "Silvestre")
secondo = fullNamePrintedRet("John", "Barbera")
print(primo)
print(secondo)
print(fullNamePrintedRet("Alex", "Alexander"))

print()

def retAdd2num(num1, num2):
    sum = num1 + num2
    str = "La somma dei due numeri è %f" % sum
    return str

terzo = retAdd2num(8, 8)
print(terzo)
quarto = retAdd2num(10, 9)
print(quarto)
print(retAdd2num(100, 1000))
