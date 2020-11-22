# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randrange
from functools import reduce


def f_sum(prev, current):
    return int(prev) + int(current)


with open("task-5-5.txt", "w", encoding="utf-8") as ffile:
    print(" ".join([str(randrange(1, 100)) for _ in range(50)]), file=ffile)

with open("task-5-5.txt", "r", encoding="utf-8") as ffile:
    try:
        print(f"Сумма чисел: {reduce(f_sum, ffile.readline().split())}")
    except:
        print("В файле встретились некорректные значения")
