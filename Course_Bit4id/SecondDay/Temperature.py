risp = input("Scegli tra C e F: ").upper()
if (risp == "C"):
    c = int(input("Digita la C:"))
    conv_C_in_F = ((9 * c + (32 * 5))/5)
    k = c + 273.15
    print("C:", c)
    print("C convertito in F: ", conv_C_in_F)
    print("K:", k)
elif(risp == "F"):
    f = int(input("Digita la F:"))
    conv_F_in_C = (5 * (f - 32)) / 9
    k = conv_F_in_C + 273.15
    print("F:", f)
    print("F convertito in C: ", conv_F_in_C)
    print("K:", k)
else:
    print("La scelta non è valida!")
