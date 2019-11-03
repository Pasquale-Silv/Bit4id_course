from math import pi
import datetime

baseT = 10
altT = 15
areaT = 10 * 15
print('Area del triangolo:', areaT)
print()

radius = 5
print("Area del cerchio:")
print((radius**2) * pi)
print("Circonferenza: " + str(2*pi*radius))

print()

date1 = datetime.datetime(2019, 2, 28)
date2 = datetime.datetime(2019, 4, 20)
print(date1)
print(date2)
print("Counting days...")
print("Giorni restanti: ", date2 - date1)
