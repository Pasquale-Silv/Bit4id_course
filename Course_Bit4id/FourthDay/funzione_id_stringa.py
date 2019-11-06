stringa1 = "Pasquale sta imparando Python"
stringa2 = "Python"
stringa3 = "java"

print("id stringa1:", id(stringa1))         # Il tipo stringa è immutabile!
print("id stringa2:", id(stringa2))         # La stringa è un immutabile !
print("id stringa3:", id(stringa3))         # stringaEs[2] = valoreDiverso <<<<--- Non è consentito poichè la stringa è un immutabile!


stringa1 = stringa2
print()
print("id stringa1:", id(stringa1))         # Il tipo stringa è immutabile!
print("id stringa2:", id(stringa2))         # La stringa è un immutabile !
print("id stringa3:", id(stringa3))         # stringaEs[2] = valoreDiverso <<<<--- Non è consentito poichè la stringa è un immutabile!
