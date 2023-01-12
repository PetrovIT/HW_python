# 5. Даны два файла, в каждом из которых находится запись многочленов. 
#    Задача - сформировать файл, содержащий сумму многочленов.

path1 = 'poly1.txt'
data1 = open (path1, 'r')
for line in data1:
     print(line)
data1.close()

path2 = 'poly2.txt'
data2 = open (path2, 'r')
for line in data2:
     print(line)
data2.close()
