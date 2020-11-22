# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

n_profit = 0
n_lines = 0
n_avg_profit = 0
itog_list = []
dict_company = {}
with open("task-5-7.txt", 'r', encoding='utf-8') as ffile:
    for line in ffile:
        line_list = line.split()
        print(line_list)
        dict_company.update({line_list[0]: int(line_list[2]) - int(line_list[3])})
        if int(line_list[2]) > int(line_list[3]):
            n_profit += int(line_list[2])
            n_lines += 1
n_avg_profit = round(n_profit / n_lines, 2)
itog_list.append(dict_company)
itog_list.append({"average_profit": n_avg_profit})
print(n_avg_profit)
print(dict_company)
print(itog_list)

with open("task-5-7-result.json", 'w', encoding='utf-8') as ffile:
    json.dump(itog_list, ffile, ensure_ascii=False)
