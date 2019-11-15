file = 'C:/Users/Student-004/Documents/fileUno.txt'

con = open(file, 'r')

data_fuori = con.read()
print(type(data_fuori))
print(data_fuori)

con.close()
