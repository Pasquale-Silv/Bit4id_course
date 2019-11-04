num = int(input("Scegli un numero: \n"))
factorial = num

while(num > 1):
    factorial *= (num-1)
    num -= 1

print(factorial)