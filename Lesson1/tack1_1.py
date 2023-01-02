# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

a = int(input("Enter a day number of week: "))
if 5 < a < 8:
     print("Weekand")
elif 0 < a < 6:
     print("Workday")
else:
     print("It's not a day of the week!")