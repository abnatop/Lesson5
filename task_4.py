"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""

READ_MODE = 'r'
APPEND_MODE = 'a'

file_in = 'task_4.txt'
file_out = 'task_4.out'

digits = {
    '1': 'Один',
    '2': 'Два',
    '3': 'Три',
    '4': 'Четыре',
    '5': 'Пять',
    '6': 'Шесть',
    '7': 'Семь',
    '8': 'Восемь',
    '9': 'Девять',
    '0': 'Ноль'
}

with open(file_out, APPEND_MODE) as f_out_obj:

    with open(file_in, READ_MODE) as f_in_obj:
        for line in f_in_obj:
            eng_digit, separator, digit = line.split()
            out_line = f'{digits[digit]} {separator} {digit}'

            f_out_obj.write(out_line + '\n')
