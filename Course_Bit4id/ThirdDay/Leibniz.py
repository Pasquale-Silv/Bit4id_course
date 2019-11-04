denom = float(input("Scegli il denominatore:"))

i = 1
bool = True
num = (4 / i)

while(i < denom):
    if(bool):
        num -= (4 / (i + 2))
        bool = False
    else:
        num += (4 / (i + 2))
        bool = True
    i += 2

print(num)