# Prova su un file che non esiste

import csv

try:
    with open("filename.tsv", 'a') as file, open('altro_file.csv', 'r') as f_hand:        # 'a' for append
        reader = csv.reader(f_hand, delimiter='\t')                                   # 'tsv' is for tab separated value
        male_data = [line for line in reader if line[0] == 'M']                       # LC
        for line in male_data:
            file.write('\t'.join(line) + '\n')
except FileNotFoundError:
    print('The file does not exist.')
