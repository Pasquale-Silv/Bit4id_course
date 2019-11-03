from datetime import datetime

data1 = datetime(1995, 12, 21)
data2 = datetime(1997, 6, 10)
print(data1)
print(data2)

giorniDiff = data1 - data2
print(giorniDiff)
print(giorniDiff * 60*60*24)
