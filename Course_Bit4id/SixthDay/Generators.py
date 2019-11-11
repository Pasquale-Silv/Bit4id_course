# A generator is a function used to create a sequence of objects.
# Generators, tipically are used in iterators as source of data
# A generator keeps track of where it was last time it was called and returns the next value.

def my_range(first, last):
    number = first
    while number < last:
        yield number
        number += 1

print(type(my_range(1, 5)))

gen1 = my_range(1, 10)
print(my_range)
print(type(gen1))
print(gen1)

for i in gen1:
    print(i)

for i in gen1:
    print(i)
