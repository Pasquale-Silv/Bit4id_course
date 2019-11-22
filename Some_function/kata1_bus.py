def number(bus_stops):
    """
    You are provided with a list (or array) of integer arrays (or tuples).
    Each integer array has two items which represent number of people get into bus (The first item)
    and number of people get off the bus (The second item) in a bus stop.
    Your task is to return number of people who are still in the bus after the last bus station (after the last array).
    Even though it is the last bus stop,
    the bus is not empty and some people are still in the bus, and they are probably sleeping there :D
    """
    entranti = 0
    uscenti = 0
    res = 0

    for i in range(0, len(bus_stops)):
        entranti += bus_stops[i][0]
        uscenti += bus_stops[i][1]

    res = entranti - uscenti
    return res

n1 = number([[10,0],[3,5],[5,8]])
print(n1)
n2 = number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
print(n2)
n3 = number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])
print(n3)

print("\nOppure...\n")

def number2(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

m1 = number2([[10,0],[3,5],[5,8]])
print(m1)
m2 = number2([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
print(m2)
m3 = number2([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])
print(m3)
