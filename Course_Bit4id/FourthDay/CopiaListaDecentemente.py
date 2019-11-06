usernames = ["Pasquale", "Gino", "Giulio", "Nando", "Teodoro"]

copied_usernames = usernames

del(copied_usernames[3])
del(copied_usernames[0])

print("Lista copiata:", copied_usernames)
print("Lista originale", usernames)
print("Se copi una lista per riferimento essa seguirà le sorti della lista copiata")

copied_usernames.append("Antonio")
copied_usernames.append("Laura")

print("Lista copiata:", copied_usernames)
print("Lista originale", usernames)

copied_usernames_decente = usernames[:]          # Oppure ' copyList = list(usernames) ' o ' copyList.copy(listToCopy) '
copied_usernames_decente2 = list(usernames)

print("\nLista copiata con usernames[:]:", copied_usernames_decente)
print("Lista copiata con list(usernames):", copied_usernames_decente2)

copyList = usernames.copy()
print("Lista copiata con metodo .copy():", copyList)

print("Queste ultime tre sono copiate dalla lista usernames, ma indipendenti da essa, non seguiranno le sue sorti!")
