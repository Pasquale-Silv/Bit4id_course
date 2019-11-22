# Complete the function that accepts a string parameter,
# and reverses each word in the string. All spaces in the string should be retained.
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
def reverse_words(text):
    listaSplit = text.split(" ")
    nuovaLista = []
    for parola in listaSplit:
        nuovaLista.append(parola[::-1])
    print(" ".join(nuovaLista))

reverse_words("stringa cosi bella")

reverse_words('The quick brown fox jumps over the lazy dog.') # 'ehT kciuq nworb xof spmuj revo eht yzal .god'
reverse_words('apple')          #, 'elppa')
reverse_words('a b c d')                #, 'a b c d')
reverse_words('double  spaced  words')              #, 'elbuod  decaps  sdrow')


print([letter for letter in "ciao"[::-1]])
