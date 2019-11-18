import datetime

today = datetime.datetime.now()
print(today)

print(today == datetime.datetime.now())
print(today > datetime.datetime.now())
print(today < datetime.datetime.now())

dataPrec = datetime.datetime(1995, 12, 21)
print(dataPrec)

print(dataPrec < today)
print(dataPrec > today)
print(today > dataPrec)