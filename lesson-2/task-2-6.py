# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

list_param = ["название", "цена", "количество", "ед"]
global_list_product = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
                       (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
                       (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]

list_param = []  ## REMOVE THIS FOR AUTOCOMPLETE
global_list_product = []  ## REMOVE THIS FOR AUTOCOMPLETE


# 1 - Создание структуры товаров
def make_structure():
    i = 1
    print()
    print("Формирование структуры списка товаров (пустая строка = окончание ввода)")
    while 1 == 1:
        new_param = input("Введите название новой характеристики списка товаров: ")
        if not new_param:
            break
        list_param.append(new_param)
    print()
    print("Список введеных характеристик: ")
    print()
    for r in list_param:
        print(f"{i}. {r}")
        i += 1


# 2 - Добавление новых товаров в кортеж

def add_product():
    dict_product = {}
    if len(list_param) == 0:
        print("Для начала введите структуру товаров!")
        return
    print()
    print("Добавление нового продукта в БД товаров")
    print("Желаете добавить новый товар?")
    print(" 1. Да")
    print(" 2. Нет")
    try:
        n_menu = int(input("Выберите пункт меню: "))
    except:
        print()
        print("Некорректный выбор пункта меню")
        print()
    if not n_menu == 1:
        return
    dict_product.clear()
    for r in list_param:
        s_value = input(f"Введите значение параметра {r}: ")
        try:
            user_value = int(s_value)
        except:
            try:
                user_value = float(s_value)
            except:
                user_value = s_value

        dict_product.update({r: user_value})
    print()
    print("Словарь характеристик продукта: ")
    print(dict_product)
    print()
    product_counter = len(global_list_product) + 1
    tuple_product = product_counter, dict_product
    print()
    print("Кортеж продуктов:")
    print(tuple_product)
    global_list_product.append(tuple_product)
    print("Глобальный список продуктов:")
    print(global_list_product)


def print_products():
    index = 0
    while index < len(global_list_product):
        print(f"Номер товара: {global_list_product[index][0]}")
        for par, val in global_list_product[index][1].items():
            print(f"    {par} : {val}")
        index += 1


def get_analytic():
    dict_of_analytic = {}

    if len(global_list_product) == 0:
        print("Список товаров пуст")
        return

    for r in global_list_product[0][1].keys():
        index = 0
        list_of_values = []
        while index < len(global_list_product):
            if list_of_values.count(global_list_product[index][1].get(r)) == 0:
                list_of_values.append(global_list_product[index][1].get(r))
            index += 1
        dict_of_analytic.update({r: list_of_values})
    print(dict_of_analytic)


# MAIN MENU

while 1 == 1:
    print("---- База данных товаров ----")
    print(" 1.Формирование новой структуры товаров")
    print(" 2.Добавление нового товара в БД")
    print(" 3.Просмотр товаров в БД")
    print(" 4.Просмотр аналитики по товарам")
    print(" 0.Выход из программы")
    print("-----------------------------")
    print()
    n_menu = -1
    try:
        n_menu = int(input("Выберите пункт меню: "))
    except:
        print()
        print("Некорректный выбор пункта меню")
        print()
    if n_menu == 1:
        make_structure()
    elif n_menu == 2:
        add_product()
    elif n_menu == 3:
        print_products()
    elif n_menu == 4:
        get_analytic()
    elif n_menu == 0:
        exit()
    else:
        print("Данного пункта меню нет")
    print()
    input("Нажмите Enter для продолжения")
    print()
