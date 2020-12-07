"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

EMP_NAME = 'name'
GROSS_VALUE = 'gross'
GROSS_MIN = 20000.0

FILE_MODE = 'r'

f_name = 'task_3.txt'

employees = []
total_money = 0.0

with open(f_name, FILE_MODE) as f_obj:
    for line in f_obj:
        emp_name, emp_gross = line.split()

        employee = {EMP_NAME: emp_name, GROSS_VALUE: float(emp_gross)}
        employees.append(employee)

        total_money += employee[GROSS_VALUE]

for emp in employees:
    if emp[GROSS_VALUE] < GROSS_MIN:
        print(f'Сотрудник {emp[EMP_NAME]} имеет оклад {emp[GROSS_VALUE]}')

middle_gross = total_money / len(employees)

print('---')
print(f'Средняя величина дохода сотрудников {round(middle_gross, 2)}')
