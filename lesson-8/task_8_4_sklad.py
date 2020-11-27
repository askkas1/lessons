import json
import pickle
from task_8_4_tech import *

class Sklad:
    def __init__(self):
        self.reset_sklad()

    def __str__(self):
        return self.get_info()

    def reset_sklad(self):
        self.dwh = []
        self.cnt = 0
        self.mass = 0

    def save_to_file(self):
        with open("task-8-4.db", "wb") as ffile:
            try:
                pickle.dump(self.dwh, ffile)
            except:
                print("Ошибка записи в файл")

    def export_to_json(self):
        res = []
        for r in self.dwh:
            obj = r.pop("obj")
            r.update({"obj": obj.__dict__})
            res.append(r)
        with open("task-8-4.json", "w", encoding='utf-8') as ffile:
            json.dump(res, ffile, ensure_ascii=False, sort_keys=True, indent=4)

    def import_from_json(self):
        self.reset_sklad()

        with open("task-8-4.json", "r", encoding='utf-8') as ffile:
            res = json.load(ffile)
        for r in res:
            obj = r.get('obj')
            if r['category'] == "Printer":
                self.add_tech(
                    Printer(obj.get('code'), obj.get('price'), obj.get('mass'), obj.get('cartridge_resource')),
                    r.get('department'))
            elif r['category'] == "Scanner":
                self.add_tech(
                    Scanner(obj.get('code'), obj.get('price'), obj.get('mass'), obj.get('lamp_resource')),
                    r.get('department'))
            elif r['category'] == "Xerox":
                self.add_tech(
                    Xerox(obj.get('code'), obj.get('price'), obj.get('mass'), obj.get('count_lotkov')),
                    r.get('department'))


    def load_from_file(self):
        try:
            with open("task-8-4.db", "rb") as ffile:
                self.dwh = pickle.load(ffile)
        except:
            print("Ошибка открытия файла")

    def check_code(self, code):
        return [dict for dict in self.dwh if dict['code'] == code]

    def get_info(self, code=False):
        res = f'\nОбъектов на складе: {self.cnt}\nМасса объектов: {self.mass} кг.\n'
        for i, r in enumerate(self.dwh):
            if code:
                if r['code'] == code:
                    res = res + f"{i + 1}. Категория: {r['category']}\tИдентификатор: {r['code']}\tДепартамент: {r['department']}\n"
                    res = res + r['obj'].get_info
                    break
            else:
                res = res + f"{i + 1}. Категория: {r['category']}\tИдентификатор: {r['code']}\tДепартамент: {r['department']}\n"
                res = res + r['obj'].get_info
        return res

    def add_tech(self, obj, department):
        if not self.check_code(obj.code):
            self.cnt += 1
            self.mass += obj.mass
            dict = {}
            dict.update({"code": obj.code})
            dict.update({"category": obj.category})
            dict.update({"department": department})
            dict.update({"obj": obj})
            self.dwh.append(dict)
            print(self.get_info(obj.code))
        else:
            print(f"Ошибка, объект с идентификатором {obj.code} уже имеется на складе")

    def remove_tech(self,code):


    def change_department(self, code, new_department):
        for r in list(self.dwh):
            if r.get("code") == code:
                r["department"] = new_department
