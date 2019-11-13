def binary_contains(sorted_iterable, key):
    low = 0
    high = len(sorted_iterable) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_iterable[mid] < key:
            low = mid + 1
        elif(sorted_iterable[mid]) > key:
            high = mid - 1
        else:
            return True
    return False

lista1 = [100, 9, 80, 102, 305, 4, 5, 19, 0, 10]
lista1.sort()
print(lista1)

risp = binary_contains(lista1, 304)
print(risp)
