def a(a):
    id(a)

print("Per vedere cosa sta accadendo in memoria:")
import dis                                             # disassemble
dis.dis(a)

print("\nVariabili locali:")
print(locals())                       # Per vedere tutte le variabili con scope local presenti nell'applicativo

print("\nVariabili globali:")
print(globals())                      # Per vedere tutte le variabili con scope global presenti nell'applicativo
