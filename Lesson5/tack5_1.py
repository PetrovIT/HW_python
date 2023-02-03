#    1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
#    В тексте используется разделитель пробел.

from random import sample

def list_of_words(count: int, ltrs: str = 'abc'):
     words = []
     for i in range (count):
          letter = sample(ltrs, k=3)
          words.append("".join(letter))
     return " ".join(words)

def simple_sentense(words: str) -> str:
     return " ".join(i for i in words.split() if i != "abc")

full_list = list_of_words(int(input("Numbers of words: ")))
print (full_list)
print (simple_sentense(full_list))