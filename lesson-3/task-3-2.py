# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

user_list = {}
user_list_structure = ["Фамилия", "Имя", "Отчество", "Дата рождения", "Город", "Почта", "Телефон"]


def set_user_data(fam, im, ot, dr, city, email, phone):
    private_user_dict = {}
    private_user_dict.update({"Фамилия": fam})
    private_user_dict.update({"Имя": im})
    private_user_dict.update({"Отчество": ot})
    private_user_dict.update({"Дата рождения": dr})
    private_user_dict.update({"Город": city})
    private_user_dict.update({"Почта": email})
    private_user_dict.update({"Телефон": phone})
    ret = ""
    for par,val in private_user_dict.items():
        ret = ret+par+": "+val+"; "
    return ret


print(
    set_user_data(fam=input("Фамилия: "),
                  im=input("Имя: "),
                  ot=input("Отчество: "),
                  dr=input("Дата рождения: "),
                  city=input("Город: "),
                  email=input("Почта: "),
                  phone=input("Телефон: "),
                  )
)
