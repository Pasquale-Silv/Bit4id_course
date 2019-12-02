def digital_root(n):
    """
    A digital root is the recursive sum of all the digits in a number.
    Given n, take the sum of the digits of n.
    If that value has more than one digit,
    continue reducing in this way until a single-digit number is produced.
    This is only applicable to the natural numbers.
    """
    nStr = str(n)
    somma = 0
    for letter in nStr:
        somma += int(letter)
    print("Se due o più numeri continua:", somma)
    nStr = str(somma)
    if (len(nStr) != 1):
        somma = 0
        for letter in nStr:
            somma += int(letter)
    return somma

# oppure....

def digital_root(n):
    nStr = str(n)
    somma = 0
    while(len(nStr) != 1):
        somma = 0
        for letter in nStr:
            somma += int(letter)
        nStr = str(somma)
    return somma

print(digital_root(456))
print(digital_root(8754677))

print("\nCon efficienza:")

def digital_root(n):
    return n%9 or n and 9

print(digital_root(456))
print(digital_root(8754677))
