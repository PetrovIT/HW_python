#    2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path

def rle_coder(text="text_words.txt", code_txt = "text_code_words.txt"):
     if path.exists(text):
          with open(text) as my_f_1, \
               open(code_txt, 'a') as my_f_2:
               for i in my_f_1:
                    my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
     else:
          print("Files do not exist in the system!")

def rle_decoder(name):
     if path.exists(name):
          with open(name) as my_f:
               n = ""
               for k in my_f:
                    word_nums = []
                    for i in k.strip():
                         if i.isdigit():
                              n += i
                         else:
                              word_nums.append([int(n), i])
                              n = ""
                    print ("".join(starmap(lambda x, y: x*y, word_nums)))
     else:
          print("Files do not exist in the system!")
rle_coder(input("Enter a name of file with text: "), input("Enter file name for record: "))
rle_decoder(input("Enter a name of file to decode: "))