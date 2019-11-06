parola = input("Passami una parola: \n").lower()
isPalindroma = True
for i in range(0, int(len(parola) / 2)):
    if(parola[i] != parola[-i - 1]):
        isPalindroma = False
        break
if(isPalindroma):
    print("La parola", parola, "è palindroma!")
else:
    print("La parola", parola, "non è palindroma!")

print(parola)
print(parola[::-1])
