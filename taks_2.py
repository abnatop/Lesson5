"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""

FILE_MODE = 'r'
f_name = 'task_2.txt'
line_count = 1

with open(f_name, FILE_MODE) as f_obj:
    for line in f_obj:
        words_in_line = len(line.split())
        print(f'Строка {line_count} содержит слов - {words_in_line}.')
        line_count += 1

print('---')
print(f'Файл {f_name} содержит {line_count - 1} строк.')
