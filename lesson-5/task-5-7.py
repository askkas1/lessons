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
with open("task-5-7.txt", 'r', encoding='utf-8') as ffile:
    dict_company = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in ffile}
    itog_list = [dict_company, ({"average_profit": round(sum([s for s in dict_company.values() if s > 0]) /
                                                         len([s for s in dict_company.values() if s > 0]), 2)
                                 })
                 ]
print(itog_list)

with open("task-5-7-result.json", 'w', encoding='utf-8') as ffile:
    json.dump(itog_list, ffile, ensure_ascii=False, sort_keys=True, indent=4)
