#    3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
#    ключи — первые буквы имён, значения — списки, содержащие имена, 
#    начинающиеся с соответствующей буквы.

def first_letter_dict(*args):
     dict_of_names = {}
     for i in sorted(args):
          letter = i[0]
          if letter not in dict_of_names:
               dict_of_names[letter] = [i]
          else:
               dict_of_names[letter] += [i]

     return dict_of_names

print(first_letter_dict("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))