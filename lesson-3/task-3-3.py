# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def get_max_arg(x, y, z):
    arg_list = [x, y, z]
    arg_min = min(arg_list)
    arg_list.remove(arg_min)
    return sum(arg_list)


print(get_max_arg(3, 1, 2)) #5
