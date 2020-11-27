class Tech:
    tech_types = ["Printer", "Scanner", "Xerox"]

    def __init__(self, code, price, mass):
        self.code = code
        self.price = int(price)
        self.mass = int(mass)

    @classmethod
    def add_manual(cls):
        resp_list = []
        for question, tp in cls.params.items():
            resp = input(f"Введите характеристику {question}: ")
            if tp == "int":
                try:
                    int(resp)
                except:
                    resp_list = []
                    input("Ошибка ввода...")
                    break
            resp_list.append(resp)
        return cls(*resp_list) if resp_list else None

class Printer(Tech):
    category = "Printer"
    params = {"Код": "str", "Цена": "int", "Масса": "int", "Ресурс картриджа": "int"}

    def __init__(self, code, price, mass, cartridge_resource):
        try:
            super().__init__(code, int(price), int(mass))
            self.cartridge_resource = int(cartridge_resource)
        except:
            print("Некорректно введены данные")



    @property
    def get_info(self):
        return f"\tЦена: {self.price} р.\n\tМасса: {self.mass} кг.\n\tРесурс картриджа: {self.cartridge_resource} стр.\n"

    # @classmethod
    # def make_from_json():


class Scanner(Tech):
    category = "Scanner"
    params = {"Код": "str", "Цена": "int", "Масса": "int", "Ресурс лампы": "int"}

    def __init__(self, code, price, mass, lamp_resource):
        try:
            super().__init__(code, int(price), int(mass))
            self.lamp_resource = int(lamp_resource)
        except:
            print("Некорректно введены данные")


    @property
    def get_info(self):
        return f"\tЦена: {self.price} р.\n\tМасса: {self.mass} кг.\n\tРесурс лампы: {self.lamp_resource} часов\n"


class Xerox(Tech):
    category = "Xerox"
    params = {"Код": "str", "Цена": "int", "Масса": "int", "Количество лотков": "int"}

    def __init__(self, code, price, mass, count_lotkov):
        try:
            super().__init__(code, int(price), int(mass))
            self.count_lotkov = int(count_lotkov)
        except:
            print("Некорректно введены данные")

    @property
    def get_info(self):
        return f"\tЦена: {self.price} р.\n\tМасса: {self.mass} кг.\n\tКоличество лотков: {self.count_lotkov} шт.\n"
