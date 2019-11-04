ages = [70, 82, 30, 1, 0, 103, 40, 22]
print(ages)

youngest = min(ages)
print(youngest)

oldest = max(ages)
print(oldest)

sumAges = sum(ages)
print(sumAges)

meanAges = sumAges / len(ages)
print("media dei valori:", meanAges)

ages.append(23)
ages.insert(2, 44)
ages.insert(0, 33)
print(ages)

new_meanAges = sum(ages) / len(ages)
print("Nuova media dei valori:", round(new_meanAges, 2))

del(ages[-1])            # Potevi usare anche ages.pop()
print(ages)              # del(index) e lista.pop(index=-1) rimuovono per indice
ages.remove(22)          # lista.remove(contenuto) rimuove per contenuto nella lista, ma solo la prima occurence.
print(ages)

nuova_media = sum(ages) / len(ages)
print("Nuova media dei valori: ", round(nuova_media, 2))

# altro esempio con .pop()
print("Elemento poppato al default index -1(last element pop):", ages.pop())           # poppa l'ultimo elemento
print(ages)
numPop = ages.pop(1)
print("Elemento poppato at index 1:", numPop)
print(ages)

nuova_media = sum(ages) / len(ages)
print("Nuova media dei valori: ", round(nuova_media, 2))
