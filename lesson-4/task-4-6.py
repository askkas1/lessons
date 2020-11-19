# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть
# условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет
# прекращено.

from itertools import count, cycle
from random import randint


def iterator_a(n_start):
    for counter in count(n_start):
        yield counter
        if counter >= 10:
            break


def iterator_b():
    counter = 0
    list = [randint(1, 50) for _ in range(100)]
    for res in cycle(list):
        yield res
        counter += 1
        if counter > 10:
            break


for r in iterator_a(3):
    print(r)

for r in iterator_b():
    print(r)
