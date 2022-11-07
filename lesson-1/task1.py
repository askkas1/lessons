# Задачи первого урока

n_menu: int = 0


##################################################################
def p_task_1():
    n_radius: int = -1
    c_pi: int = 3.14159
    print("Посчитаем площадь круга")
    s_radius = input("Введите радиус:")
    if not s_radius.isdigit():
        print("Некорректная площадь")
        return
    n_radius=int(s_radius)
    print("Площадь круга= {S}".format(S=2 * c_pi * int(n_radius)))


##################################################################

def p_task_2():
    n_days: int = 0
    n_hours: int = 0
    n_minutes: int = 0
    n_seconds: int = 0
    n_user_time_seconds: int = 0

    s_user_time_seconds = input("Введите время в секундах: ")
    if not s_user_time_seconds.isdigit():
        print("Некорректный ввод")
        return
    n_user_time_seconds = int(s_user_time_seconds)

    n_hours = int(n_user_time_seconds / 60 / 60)
    n_minutes = int(n_user_time_seconds / 60 - n_hours * 60)
    n_seconds = int(n_user_time_seconds - n_hours * 60 * 60 - n_minutes * 60)
    print(f"{n_hours:02d}:{n_minutes:02d}:{n_seconds:02d}")


##################################################################


def p_task_3():
    x = input("Введите целое число : ")
    if not x.isdigit():
        print("Некорректный ввод")
        return
    y = int(x) + int(x + x) + int(x + x + x)
    print(f"Ваша сумма чисел - {x} + {x}{x} + {x}{x}{x} = {y}")


##################################################################


def p_task_4():
    index: int = 0
    n_max: int = 0
    user_string = input("Введите целочисленное число: ")
    if not user_string.isdigit():
        print("Некорректный ввод")
    while index < len(user_string):
        if int(user_string[index]) > n_max:
            n_max = int(user_string[index])
        index += 1
    print("Максимальное число в строке: {}".format(n_max))


##################################################################

def p_task_5():
    n_debit: int = 0
    n_credit: int = 0
    n_people_cnt: int = 0
    s_debit = input("Введите значение выручки фирмы: ")
    s_credit = input("Введите значение издержек фирмы: ")
    if not s_debit.isdigit() or not s_credit.isdigit():
        print("Введено некорректное значение")
    n_debit = int(s_debit)
    n_credit = int(s_credit)
    if n_debit > n_credit:
        print(f"Прибыль составляет: {n_debit - n_credit}")
        s_people_cnt = input("Введите численность сотрудников фирмы: ")
        if not s_people_cnt.isdigit():
            print("Введенные данные некорректны")
        n_people_cnt = int(s_people_cnt)
        print(f"Прибыль на одного сотрудника составляет: {(n_debit - n_credit) / n_people_cnt}")
    else:
        print(f"Убытки составляют: {n_credit - n_debit}")


##################################################################

def p_task_6():
    n_start_km: int = 0
    n_target_km: int = 0
    n_prev_day_km: int = 0
    n_day_of_target: int = 1
    s_start_km = input("Сколько километров спортсмен пробежал в первый день?: ")
    s_target_km = input("Сколько километров требуется пробежать спортсмену?: ")
    if not s_start_km.isdigit() or not s_target_km.isdigit():
        print("Введены некорректные значения")
    n_start_km=int(s_start_km)
    n_target_km=int(s_target_km)
    n_prev_day_km=n_start_km
    while n_prev_day_km < n_target_km:
        n_day_of_target += 1
        n_prev_day_km=n_prev_day_km+n_prev_day_km*0.1
        print(f"День: {n_day_of_target}, расстояние: {round(n_prev_day_km,2)} км")

        if n_day_of_target > 365 * 10:
            print("Цель недостижима :(")
            return
    if n_target_km<n_start_km:
        print("Хорошая попытка :)")
    else:
        print(f"Спортсмен пробежит указанное расстояние на {n_day_of_target} день")


##################################################################

while True:
    print("")
    print("!!! Программа по первому уроку!!!")
    print("-------------------------------------")
    print("Выберите номер задания")
    print(" 1.Работа с переменными")
    print(" 2.Форматирование времени в секундах hh24:mi:ss")
    print(" 3.Сумма чисел n+nn+nnn")
    print(" 4.Максимальное число в строке")
    print(" 5.Выручка и издержки фирмы")
    print(" 6.Задача со спортсменом")
    print(" 7.Выход")
    print("-------------------------------------")

    n_menu = input("Ваш выбор: ")

    if n_menu.isdigit() == True:
        if int(n_menu) == 1:
            p_task_1()
        if int(n_menu) == 2:
            p_task_2()
        if int(n_menu) == 3:
            p_task_3()
        if int(n_menu) == 4:
            p_task_4()
        if int(n_menu) == 5:
            p_task_5()
        if int(n_menu) == 6:
            p_task_6()
        if int(n_menu) == 7:
           break

    else:
        print("Некорректный выбор")
    print("")
    input("Нажмите Enter для продолжения ...")