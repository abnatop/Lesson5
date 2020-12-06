"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""

FILE_MODE = 'r'
f_name = 'task_2.txt'

with open(f_name, FILE_MODE) as f_obj:
    for line in f_obj:
        print(line)
