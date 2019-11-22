def reverse_words(str):
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)

primo = reverse_words("La vita è bella!  vero?")
print(primo)

secondo = reverse_words('double  spaced  words')              #, 'elbuod  decaps  sdrow')
print(secondo)
