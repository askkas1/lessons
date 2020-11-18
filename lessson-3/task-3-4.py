# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя
# способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора
# **, предусматривающая использование цикла.

def get_pov(a, b):
    if a.isdigit and b.isdigit:
        res = 1 / abs(int(a)) ** abs(int(b))
    else:
        print("Введены не корректные числа")
        res = 0
    return res


def get_pov_cycle(a, b):
    res = 0
    if a.isdigit and b.isdigit:
        i = 1
        res = int(a)
        while i < abs(int(b)):
            res = res * int(a)
            i += 1
        res = 1 / res
    else:
        print("Введены не корректные числа")

    return res


s_a = input("Введите первое число: ")
s_b = input("Введите второе число: ")
print(get_pov(s_a, s_b))
print(get_pov_cycle(s_a, s_b))
