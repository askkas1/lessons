# TASK 2-3 Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (
# зима, весна, лето, осень). Напишите решения через list и через dict.

print("---Используем словарь---")
seasons_dict = {12: "Зима", 1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
                9: "Осень", 10: "Осень", 11: "Осень"}
print(seasons_dict)
s_user_month = input("Введите номер месяца: ")
try:
    n_user_month = int(s_user_month)
except:
    print("Введено некорректное число")
    exit()
print("Время года для данного месяца: ", seasons_dict.get(n_user_month))

print("---Используем список---")
seasons_list = [12, "Зима", 1, "Зима", 2, "Зима", 3, "Весна", 4, "Весна", 5, "Весна", 6, "Лето", 7, "Лето", 8, "Лето",
                9, "Осень", 10, "Осень", 11, "Осень"]
print(seasons_list)

s_user_month = input("Введите номер месяца: ")
try:
    n_user_month = int(s_user_month)
except:
    print("Введено некорректное число")
    exit()
try:
    c_user_month=seasons_list[seasons_list.index(n_user_month) + 1]
    print("Время года для данного месяца: ",seasons_list[seasons_list.index(n_user_month) + 1])
except:
    print("Данного месяца нет в списке")
