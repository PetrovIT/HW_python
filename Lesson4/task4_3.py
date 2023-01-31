# 3. Задайте последовательность чисел. Напишите программу, 
#    которая выведет список неповторяющихся элементов исходной 
#    последовательности в том же порядке.

import random
from itertools import groupby

def random_list(n):
     if n < 1:
          print("Negative value of the number of numbers!")
          exit()
     else:
          my_list = []
          for i in range(n):
               my_list.append(random.choice(range(1, 11)))
     return my_list

num = int(input("Enter a number N: "))
numbers_list = random_list(num)
print(numbers_list)

new_list = sorted(set(numbers_list), key=lambda d: numbers_list.index(d))
print(new_list)