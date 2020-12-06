"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
FILE_MODE = 'w'

f_name = 'task_1.txt'
f_list = []
f_string = ' '

while f_string:
    f_string = input('Введите текст: ')
    if f_string:
        f_list.append(f_string)

with open(f_name, FILE_MODE) as f_obj:
    for line in f_list:
        f_obj.write(line)

print(f'Текст сохранен в файле {f_name}')
