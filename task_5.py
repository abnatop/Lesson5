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

f_name = 'task_5.txt'

for i in range(10):
    print(randint(0,2))

# with open(f_name, APPEND_MODE) as f_obj:
#     for line in f_list:
#         f_obj.write(line + '\n')
