# try
# except
# else                     This executes ONLY if no exception is raised
# finally                  Viene eseguito sempre

print("Devi dividere due numeri")
num1 = int(input("Scegli il primo numero:\n"))
num2 = int(input("Scegli il secondo numero:\n"))

try:
    res = num1 / num2
    print(res)
except (ZeroDivisionError):
    print("Eccezione:", ZeroDivisionError, ", completamente gestita! Bravo!")
else:
    print("else: Solo se va tutto bene")
finally:
    print("finally sempre presente !")

print("poichè hai gestito l'eccezione il programma continua la sua esecuzione fin qui!")
print("Complimenti!")
