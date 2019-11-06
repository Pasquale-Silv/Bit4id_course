careers = ["Programmer", "Economist", "Architect", "Accountant"]

print(careers.index("Accountant"))

print(careers[careers.index("Accountant")])
if (careers[careers.index("Accountant")] in careers):
    print(careers[careers.index("Accountant")], "è presente nella lista 'careers'.")

careers.append("Constructor")

careers.insert(0, "Teacher")

print()

for career in careers:
    print(career)

print("-------------------------------------")

careers2 = []

for career in careers:
    careers2.append(career)

print("Nuova lista:", careers2)
print("Prima carriera:", careers2[0])
print("Ultima carriera:", careers2[-1])
