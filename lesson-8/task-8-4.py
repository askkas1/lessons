import os
import json
from task_8_4_sklad import *
from task_8_4_tech import *


def clear():
    os.system('cls')


def fill_default_sklad():
    sklad.add_tech(Xerox("Xerox-001", 13500, 6, 2), "IT")
    sklad.add_tech(Xerox("Xerox-002", 50000, 15, 4), "CEO")

    # sklad.add_tech(Scanner("Scan-001", 5000, 1, 1000), "IT")
    # sklad.add_tech(Scanner("Scan-002", 10000, 3, 5000), "CEO")
    #
    # sklad.add_tech(Printer("Printer-HP-001", 5000, 3, 3000), "IT")
    # sklad.add_tech(Printer("Printer-HP-004", 10000, 2, 6000), "CEO")
    # sklad.add_tech(Printer("Printer-HP-005", 10000, 2, 6000), "BUHGALTERY")
    #

def menu():
    clear()
    while True:
        print("Меню: ")
        print(" 1. Посмотреть оборудование на складе")
        print(" 2. Добавить новое оборудование")
        print(" 3. Перенести оборудование")
        print(" 4. Загрузить из файла")
        print(" 5. Сохранить в файл")
        print(" 6. Экспорт в JSON")
        print(" 7. Импорт из JSON")
        print(" 8. Продать оборудование")
        print(" 9. Очистить склад")
        print(" 0. Выход")
        n_menu = input("Выберите действие: ")
        clear()
        if n_menu.isdigit() and n_menu in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if n_menu == "1":
                print(sklad)
                input("Нажмите Enter для продолжения...")
            elif n_menu == "2":
                clear()
                print("Выберите тип устройства: ")
                for i, v in enumerate(Tech.tech_types):
                    print(f"\t{str(i + 1)}. {v}")
                n_menu = int(input("Ваш выбор:"))
                if n_menu < len(Tech.tech_types) + 1:
                    ask = Tech.tech_types[n_menu - 1]
                    # --------------
                    if ask=="Printer":
                        new = Printer.add_manual()
                    elif ask == "Scanner":
                        new = Scanner.add_manual()
                    # ---------------
                    elif ask == "Xerox":
                        new = Xerox.add_manual()
                    if hasattr(new, 'mass'):
                        dep = input("Введите департамент: ")
                        sklad.add_tech(new, dep)
                    print()
                    input("Нажмите Enter для продолжения...")
            elif n_menu == "3":
                clear()
                print(sklad)
                num = input("Введите номер оборудования для перемещения: ")
                to_dep = input("Введите наименование нового департамента: ")
                try:
                    sklad.change_department(sklad.dwh[int(num) - 1]['code'], to_dep)
                    clear()
                    print(sklad.get_info(sklad.dwh[int(num) - 1]['code']))
                except:
                    print("Некорректный выбор")
                finally:
                    print()
                    input("Нажмите Enter для продолжения...")
            elif n_menu == "4":
                sklad.load_from_file()
            elif n_menu == "5":
                sklad.save_to_file()
            elif n_menu == "6":
                sklad.export_to_json()
            elif n_menu == "7":
                sklad.import_from_json()
            elif n_menu == "8":
                pass
            elif n_menu == "9":
                sklad.reset_sklad()

            clear()
        else:
            break


sklad = Sklad()
fill_default_sklad()
# p = Printer("PPP", 123, 123, 123)
# print(p.__class__)
# print(p.__dict__)
# print(p.__annotations__)
# print(PrinterEncoder().default(p))
clear()
menu()
