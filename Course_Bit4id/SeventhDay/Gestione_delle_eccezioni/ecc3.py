try:
    print(3 / 0)
except Exception as e:
    print(e, "-------- >   è stata sollevata!")
finally:
    print("Questo viene eseguito in ogni occasione!")


print("hey")
print(10 * 100)
x = 80 if 10 == 10 else "ciao"
print(x)

y = 100 if 10 != 10 else "ciao"
print(y)
