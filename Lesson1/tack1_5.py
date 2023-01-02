# 5. Напишите программу, которая принимает на вход координаты двух точек 
#    и находит расстояние между ними в 2D пространстве.

ax = float(input("Enter coordinate X of point A: "))
ay = float(input("Enter coordinate Y of point A: "))
bx = float(input("Enter coordinate X of point B: "))
by = float(input("Enter coordinate Y of point B: "))
print(round(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5, 3))