def first_non_repeated(s):
    diz = {}
    for carattere in s:
        if carattere in diz:
            diz[carattere] += 1
        else:
            diz[carattere] = 1
    for carattere in s:
        for k, v in diz.items():
            if diz[carattere] == 1:
                return carattere

primo = first_non_repeated("pasquale")
print(primo)

primo = first_non_repeated("alfonso")
print(primo)

primo = first_non_repeated("alberoa")
print(primo)
