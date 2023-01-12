# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_nums(n):
     my_list = []
     d = 2
     while d * d <= n:
          if n % d == 0:
               my_list.append(d)
               n //= d
          else:
               d += 1
     if n > 1:
          my_list.append(n)
     return my_list
print(simple_nums(int(input('Number: '))))
