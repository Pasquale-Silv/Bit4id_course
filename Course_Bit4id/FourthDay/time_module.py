import time

start_time = time.time()
squares = []

for num in range(1, 10000000):
    squares.append(num ** 2)

print(time.time() - start_time)

new_start = time.time()

new_square = [num ** 2 for num in range(1, 10000000)]                         # LC is better!!!
print(time.time() - new_start)
