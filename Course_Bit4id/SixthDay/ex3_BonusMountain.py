def metriToFeet(dictionary):
    """Data una lista espressa in metri, ritorna la lista equivalente espressa in feet."""
    list = []
    for k, v in dictionary.items():
        list.append(round(v * 3.28, 2))
    return list

def dictMetriFeet(dictionary):
    """
    Dato un dizionario contenente come valori solamente grandezze espresse in metri,
    restituisce un nuovo dizionario con una lista come valore contenente la grandezza espressa in metri e l'equivalente in feet.
    """
    return {key:[value, round(value * 3.28, 2)] for key, value in dictionary.items()}

mountainHeights = {
    "Kilimangiaro": 5895,
    "Camerun": 4040,
    "Elgon": 4321,
    "Sinai": 2285,
    "Everest": 8848,
}

listaFeet = metriToFeet(mountainHeights)
print(listaFeet)

new_dict_metri_feet = dictMetriFeet(mountainHeights)
print(new_dict_metri_feet)
