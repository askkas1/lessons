# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def make_divide(x, y):
    """Функция деления двух чисел"""
    x = int(x) if x.isdigit() else x
    y = int(y) if y.isdigit() else y
    try:
        res = x / y
    except ZeroDivisionError:
        print("Ошибка - деление на 0")
        res="ОШИБКА"
    return res


s_user_x = input("Введите первое число: ")
s_user_y = input("Введите второе число: ")

print("Результат: ", make_divide(s_user_x, s_user_y))
