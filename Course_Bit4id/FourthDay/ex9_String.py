sentence = "Pasquale sta imparando il linguaggio 'Python'."
lenSentence = len(sentence)
lenSentenceMeta = lenSentence / 2

print("Prime 5 lettere:", sentence[:5])
print("Prime 5 lettere dalla metà della lunghezza della stringa:", sentence[int(lenSentenceMeta):int(lenSentenceMeta+5)])
print("Ultime 5 lettere", sentence[-5:])

print(sentence + "\n")

sentence2 = "Pasquale sta imparando il linguaggio 'Python'. Tu preferisci Python o java?\n"
print(sentence2)

if ('Python' in sentence2):
    print("La parola 'Python' è presente nella lista!")
else:
    print("Parola non presente nella lista!")

print("La prima parola 'Python' inizia da", sentence2.find("Python"))
print("La seconda parola 'Python' inizia da", sentence2.rfind("Python"))
print("La parola 'Python' è presente per ben", sentence2.count("Python"), "nella stringa 'sentence2'")

sentence2Split = sentence2.split()
print(sentence2Split)

for parola in sentence2Split:
    print(parola)

print(sentence2.replace("Python", "Ruby"))
