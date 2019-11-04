import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
ordered_list = sorted(example_list)

print(example_list)
print("Ordiniamo:")
print(ordered_list)

print("Lunghezza della lista:", len(ordered_list))
print()

x = statistics.mean(example_list)
print("Media della distribuzione:", x)

y = statistics.median(example_list)
print("Mediana della distribuzione:", y)

z = statistics.mode(example_list)
print("Moda della distribuzione:", z)

a = statistics.stdev(example_list)
print("Standard deviation della distribuzione:", a)

b = statistics.variance(example_list)
print("Varianza della distribuzione:", b, "\n")

print(statistics.variance([1, 2, 2, 2, 2, 4, 3]))
print(statistics.variance([2, 2, 2, 2, 2, 2]))
