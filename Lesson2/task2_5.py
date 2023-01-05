# 5. Реализуйте алгоритм перемешивания списка.
#    Без функции shuffle из модуля random.

n = int(input('Enter a size of list: '))
my_list = list(range(n))
print(my_list)
from random import randrange
for i in range(n):
     temp1 = randrange(n)
     temp2 = my_list[i]
     my_list[i] = my_list[temp1]
     my_list[temp1] = temp2
print(my_list)