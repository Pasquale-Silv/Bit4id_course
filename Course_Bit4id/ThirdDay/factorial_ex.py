num = int(input("Scegli un numero: \n"))
app = num
factorial = 1
list = [num]

for i in range(num):
    if num == 1:
        break
    list.append(num - 1)
    num -= 1

print(list)

for i in list:
    factorial *= i

print("Il fattoriale del numero", app,"è:", factorial)