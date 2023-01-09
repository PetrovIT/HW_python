# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
#    Без использования встроенной функции преобразования, без строк. Без использования 
#    встроенной функции преобразования, без строк.

def conv_to_bin (num):
     num_list = []
     while num:
          num_list.insert(0, num % 2)
          num //= 2
     return num_list

num = int(input('Enter a number: '))
print(*conv_to_bin(num), sep='')