def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

def calculator(a, b, operator):
    calculator = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    return calculator[operator](a, b)

add1 = calculator(2, 5, "add")
print(add1)

sub1 = calculator(10, 8, "subtract")
print(sub1)
