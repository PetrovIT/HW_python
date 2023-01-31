# 1. Вычислить число c заданной точностью d

from decimal import Decimal
def round_num():
     number = Decimal(input('Enter a real number: '))
     dec = Decimal(input("Enter the required accuracy '0.0001': "))
     ost = dec % 1
     print(round(number / ost) * ost)

round_num()