def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)

print("---------------------------------------")

def fibo(n):
    a = 0
    b = 1
    while(a < n):
        print(a, end=' ')
        c = a
        a = b
        b = c + b
    print()
fibo(1000)
