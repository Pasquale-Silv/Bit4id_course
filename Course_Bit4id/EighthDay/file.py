import datetime

file_loc = 'filenamePrimo.csv'

f_hand = open(file_loc, 'w')

f_hand.write("Ciao Pasquale,\ncome stai oggi?")

f_hand.closed

f_hand.close()

f_hand.closed

print("-------------------------------------------------------")

f_hand = open(file_loc, 'r')
lines = f_hand.read().splitlines()  # lines to a list
print(lines[0])   # header

for line in lines:
    if line.startswith('M'):
        print(line)

print(f_hand.read())

f_hand.close()
