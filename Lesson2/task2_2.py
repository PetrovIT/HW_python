# 2. Напишите программу, которая принимает на вход число N 
#    и выдает набор произведений чисел от 1 до N в виде списка.

num = int(input('Enter e number N: '))
sum = 1
list = []
for i in range(num):
     sum *= i + 1
     list.append(sum)
print(list)