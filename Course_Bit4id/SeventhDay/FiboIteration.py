def fibo(num):
    num1 = 0
    num2 = 1
    temp = 0
    while(num > 0):
        print(num1, end=" ")
        temp = num1
        num1 = num2 + num1
        num2 = temp

        num -= 1
    print()

fibo(10)  # 89

def fiboSommaUltimo(num):
    num1 = 0
    num2 = 1
    temp = 0
    somma = 1
    while(num > 0):
        temp = num1
        somma += num1
        num1 = num2 + num1
        num2 = temp

        num -= 1
    return somma

sommaFibo = fiboSommaUltimo(10)
print(sommaFibo)
