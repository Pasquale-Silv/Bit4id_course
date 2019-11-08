Individui = {
    "Pasquale": {"Mestiere": "Data Scientist", "Automunito": True, "Titolo di studio": "Laurea triennale", "Peso": 85},
    "Giulio": {"Mestiere": "Matematico", "Automunito": True, "Titolo di studio": "Laurea magistrale", "Peso": 77},
    "Alfonso": {"Mestiere": "Chirurgo", "Automunito": True, "Titolo di studio": "Laurea magistrale", "Peso": 88},
    "Bryan": {"Mestiere": "Meccanico", "Automunito": True, "Titolo di studio": "Diploma", "Peso": 64},
    "Giacomo": {"Mestiere": "Agricoltore", "Automunito": False, "Titolo di studio": "Diploma", "Peso": 93}
}

for key in Individui.keys():
    print("KEY:", key)
    print("Rispettivo dizionario value:", Individui[key])
print()

for k in Individui.keys():
    print("Chiave del dizionario esterno: %s" %(k))
    for k2 in Individui[k].keys():
        print("\t\tChiavi del dizionario interno %s:" % (k2))
print()


for k, v in Individui.items():
    print("KEY:", k, ", VALUE:", v)
print()

for k, v in Individui.items():
    yesOrNO = v['Automunito']
    if(yesOrNO):
        yesOrNO = "yes"
    else:
        yesOrNO = 'no'
    print("KEY:", k.title(), ", VALUE['Automunito'](YES or NO) :", yesOrNO)
print("\n")



for individuo, infoIndividuo in Individui.items():
    print("Ecco le informazioni su %s:" % (individuo.upper()))
    for key in infoIndividuo.keys():
        if key == 'Mestiere':
            print("\t%s" % infoIndividuo[key].upper())
        elif key == 'Automunito':
            if(infoIndividuo[key]):
                infoIndividuo[key] = "yes"
            else:
                infoIndividuo[key] = "no"
            print("\tIl soggetto è automunito: %s" % (infoIndividuo[key]))
        else:
            print("\tValore senza condizioni speciali che lo modificano: %s" % (infoIndividuo[key]))

