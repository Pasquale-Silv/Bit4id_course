sentence = "Pasquale sta imparando il linguaggio 'Python'"

for letter in sentence:
    print(letter)

listSentence = list(sentence)

print(listSentence)

print("Ora estrapola la parola 'Python' dalla lista:")
listaSplit = sentence.split()
print(listaSplit)                   # Traforma la sentence in una lista di parole!