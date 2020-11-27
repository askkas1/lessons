class ZeroErr(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(txt)


x = input("Введите  делимое: ")
y = input("Введите делитель: ")

try:
    if y == "0":
        raise ZeroErr("Некорректный делитель")
    z = int(x) / int(y)
except ZeroErr:
    pass
except:
    print("Ошибка в строке")
