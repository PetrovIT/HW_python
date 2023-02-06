#    * 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», 
#    возвращает словарь, ключи — первые буквы фамилий, значения — словари, 
#    реализованные по схеме предыдущего задания.

from collections import OrderedDict

def first_letters_surnames_names(*args):
     s_n_sort = {}
     for s_n in args:
          s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
     return dict(OrderedDict(sorted(s_n_sort.items(), key = lambda x: x[0])))


s_n_names = first_letters_surnames_names("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                                         "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
                                         "Борис Аркадьев", "Антон Серов", "Павел Анисимов")

print(s_n_names)