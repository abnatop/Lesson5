"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
"""
from random import randint

READ_MODE = 'r'
APPEND_MODE = 'a'

RAND_FROM = 0
RAND_TO = 100
DIGIT_COUNT = 10

f_name = 'task_5.txt'

with open(f_name, APPEND_MODE) as f_obj:
    for i in range(DIGIT_COUNT):
        digit = randint(RAND_FROM, RAND_TO)
        f_obj.write(f'{digit} ')
