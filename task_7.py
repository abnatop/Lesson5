"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
Подсказка: использовать менеджер контекста.
"""

READ_MODE = 'r'
APPEND_MODE = 'a'

f_name = 'task_7.txt'
firms_data = {}

with open(f_name, READ_MODE) as f_obj:
    for line in f_obj:
        firm_name, firm_type, firm_gross, firm_total = line.split()
        firm_gross, firm_total = float(firm_gross), float(firm_total)
        firms_data[firm_name] = firm_gross - firm_total

total_profit = 0.0
for value in firms_data.values():
    if value > 0:
        total_profit += value
average_profit = total_profit / len(firms_data)

print(total_profit, average_profit)