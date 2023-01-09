# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample
def multiplication_couple_numbers (len_list):
     first_list = sample (range(1, len_list + 1), k=len_list)
     new_list =[]
     print(first_list)
     index_l = 0
     index_r = len_list - 1
     while index_l < index_r:
          new_list.append(first_list[index_l] * first_list[index_r])
          index_l += 1
          index_r -= 1
     if len_list % 2:
          new_list.append(first_list[len_list // 2])
     print(new_list)
multiplication_couple_numbers (int(input()))