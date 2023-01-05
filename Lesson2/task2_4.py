# 4. Напишите программу, которая принимает на вход 2 числа.
#    Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#    Найдите произведение элементов на указанных позициях(не индексах).

num = int(input('Enter a number N: '))
pos1 = int(input('Enter a position first: '))
pos2 = int(input('Enter a position second: '))
if pos1 > (abs(num) * 2 + 1) or pos2 > (abs(num) * 2 + 1):
     print('There are no values for these indexes!')
num_list = list(range(-num, num + 1))
res = num_list[pos1 - 1] * num_list[pos2 -1]
print(num_list)
print(res)