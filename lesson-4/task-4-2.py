# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from functools import reduce
from random import randint


def get_max(prev, current):
    return current if current > prev else False


n_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# n_list = [1,2,3]
# n_list = [randint(1,1000) for _ in range(20)]
# n_list = [531, 163, 370, 736, 730, 880, 739, 498, 433, 12, 888, 167, 975, 950, 774, 801, 316, 397, 891, 958]
i = 1
new_list = []
while i < len(n_list):
    new_item=get_max(n_list[i - 1], n_list[i])
    if new_item:
        new_list.append(new_item)
    i += 1
print(n_list)
print(new_list)
