careers = ["Programmer", "Economist", "Architect", "Accountant"]

print("Lista sulla quale effettueremo le operazioni:", careers)

print("\nOrdine originale:")
for career in careers:
    print(career)

print("\nOrdine alfabetico:")
for career in sorted(careers):
    print(career)

print("\nOrdine originale:")
for career in careers:
    print(career)

print("\nOrdine reverse-alfabetico:")
for career in sorted(careers, reverse=True):
    print(career)

print("\nOrdine originale:")
for career in careers:
    print(career)

print("\nOrdine reverse-posizionale:")
careers.reverse()                                # Non assegnarlo ad altra variabile, altrimenti None (.reverse() x2)
for career in careers:
    print(career)

careers.reverse()

print("\nOrdine originale:")
for career in careers:
    print(career)

print("\nLista ordinata permanentemente in ordine alfabetico:")
careers.sort(reverse=False)
for career in careers:
    print(career)

print("\nLista ordinata permanentemente in ordine alfabetico inverso:")
careers.sort(reverse=True)
for career in careers:
    print(career)
