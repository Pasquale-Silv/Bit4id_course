items = ["Python", 23, "Napoli", "Pasquale"]

for item in items:
    print(item)

print()

for item in items:
    print("Mi chiamo {}, vivo a {}, ho {} anni e sto imparando il linguaggio di programmazione '{}'.".format(items[-1],
                                                                                                             items[-2],
                                                                                                             items[-3],
                                                                                                             items[0]))

print()

for item in items:
    print("Vediamo ciclicamente cosa abbiamo nella nostra lista:", item)

