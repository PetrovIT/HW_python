#    1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
#       значения которых больше предыдущего элемента. Use comprehension.

from random import sample

def if_next_number_more(num):
    my_list = sample(range(num * 3), num)
    print(my_list)
    return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]

print(if_next_number_more(int(input("Enter a lenght of number's list: "))))