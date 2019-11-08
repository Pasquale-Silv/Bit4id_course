def int_in_str(num):
    if(num == 0):
        return "zero"
    elif(num == 1):
        return "one"
    elif(num == 2):
        return "two"
    elif(num == 3):
        return "three"
    else:
        return "number greater than three..."

prova1 = int_in_str(2)
print(prova1)