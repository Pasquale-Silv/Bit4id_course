stringa1 = "Pasquale"

# Inverti con LC:
lc1 = [letter for letter in stringa1]
print(lc1)

lc2 = [letter for letter in stringa1[::-1]]
print(lc2)

lc3 = [stringa1[i] for i in range(len(stringa1)-1, 0, -1)]
print(lc3)
