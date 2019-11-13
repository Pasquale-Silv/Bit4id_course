def fibo(n, num1=0, num2=1):
    if(n == 0):
        return 1
    somma = num1 + fibo(n-1, num1=num2, num2=(num1 + num2))
    return somma

fibo10 = fibo(10)
print(fibo10)
