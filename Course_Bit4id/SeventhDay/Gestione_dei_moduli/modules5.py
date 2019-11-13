# absolute path    ------->     import math         (Standard library)
# relative path    ------->     import .math        (Cerca prima nella home directory)

import math

print(dir(math))                                      # Cosi vedi tutto ciò che contiene al suo interno il modulo 'math'

print("\n\n\nCon funzione help():")

print(help(math.log))                                 # Cosi invece vedi l'aiuto riguardo una funzione specifica!

print("\n\nhelp() sul modulo math:")
print(help(math))

