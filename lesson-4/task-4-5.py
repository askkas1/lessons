# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка. Подсказка: использовать функцию reduce().

from random import randrange
from functools import reduce


def com(prev, curr):
    return prev * curr


print(reduce(com, [randrange(100, 1001) for _ in range(50)]))
