#    2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def uniq_numbers(num):
     return [el for el in range(20, num + 1) if el % 20 == 0 or el % 21 == 0]

print(uniq_numbers(int(input('Enter a number more than 20: '))))