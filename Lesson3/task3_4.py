# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь. 
#    Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
#    дробной части элементов.

import random

def create_float_list (len_list): # создаем список вещественных чисел
     any_list = []
     for i in range(0, len_list):
          any_list.append(round(random.uniform(1, 10), 2))
     print(any_list)
     return any_list

def find_diff_min_max (any_list): 
     new_list = [] 
     for i in range (len (any_list)): # создаем новый список только из дробных частей чисел
          new_list.append(round(any_list[i] % 1, 2))
     print(new_list)
     max = min = new_list[0]
     for i in range (1, len (any_list)): # ищем минимальное и максимальное значение
          if min > new_list[i]:
               min = new_list[i]
          if max < new_list[i]:
               max = new_list[i]
     print(max, min)
     different = round(max - min, 2)
     print(different)

number = int(input("Enter a nubmer: "))
find_diff_min_max(create_float_list(number))