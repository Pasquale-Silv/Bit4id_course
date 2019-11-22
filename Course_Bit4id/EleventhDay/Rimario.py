def rimario(elenco):
    rime = []
    parola = input("Inserisci la parola di cui desideri cercare le rime:\n").lower()
    for elemento in elenco:
        if elemento[-3:] == parola[-3:]:
            rime.append(elemento)
    if (not rime):
        print("Non sono state trovate rimecorrispondenti alla parola trovata!")
    else:
        print(f"Le rime corrispondenti alla parola '{parola}' sono le seguenti: {rime}")

lista_parola = ['fare', "dormire", "giocare", "cespuglio", "anatra", "fittizio"]
rimario(lista_parola)
