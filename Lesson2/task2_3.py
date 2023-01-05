# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

num = int(input('Enter e number N: '))
list = []
sum = 0
for i in range(1, num + 1):
     res = round((1 + 1 / i) ** i, 3)
     list.append(res)
     sum += res
print(list)
print(sum)