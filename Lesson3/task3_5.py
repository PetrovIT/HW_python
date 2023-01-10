# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def negafibonachi (number):
     fib1 = fib2 = 1
     fib_1 = 1
     fib_2 = -1
     fib_list = [-1, 1, 0, 1, 1]
     for i in range(n-2):
          fib1, fib2 = fib2, fib1 + fib2
          fib_1, fib_2 = fib_2, fib_1 - fib_2
          fib_list.append(fib2)
          fib_list.insert(0, fib_2)
     return fib_list

n = int(input("Enter number N of Fibonachi: "))
print(*negafibonachi(n))