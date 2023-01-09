# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample
def sum_odd_numbers (len_list):
     new_list = sample (range(1, len_list * 2), k=len_list)
     print(new_list)
     sum = 0
     for i in range(0, len_list, 2):
          sum += new_list[i]
     print(sum)

sum_odd_numbers (int(input()))