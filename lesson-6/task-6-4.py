# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
from random import randrange


class Car:
    speed = 0
    __directions = {1: "Налево", 2: "Направо", 3: "Прямо", 4: "Разворот"}
    __direction = 3

    def go(self):
        self.speed = randrange(10, 150)
        print(f"Машина {self.name} поехала")

    def stop(self):
        self.speed = 0
        print(f"Машина {self.name} остановилась")

    def turn(self, direction=False):
        self.__direction = randrange(1, 5) if not direction else direction
        print(f"Машина {self.name} едет {self.__directions.get(self.__direction)}")


    def show_speed(self):
        print(f"Скорость машины составляет: {self.speed}")

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Внимание! Превышение скорости: {self.speed}")
        else:
            print(f"Скорость в норме: {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Внимание! Превышение скорости: {self.speed}")
        else:
            print(f"Скорость в норме: {self.speed}")


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, True)


town_car_1 = TownCar("Городская 1","Черная")
town_car_2 = TownCar("Городская 2","Белая")
work_car_1 = WorkCar("Рабочая 1","Синяя")
sport_car = SportCar("Спортивная","Красная")
police_car= PoliceCar("Полицейская","Красная")

town_car_1.go()
town_car_1.show_speed()
town_car_1.turn()
town_car_1.turn()
town_car_1.stop()
print()
town_car_2.go()
town_car_2.show_speed()
town_car_2.turn()
town_car_2.turn()
town_car_2.stop()
print()
work_car_1.go()
work_car_1.show_speed()
work_car_1.turn()
work_car_1.turn()
work_car_1.stop()
print()
sport_car.go()
sport_car.show_speed()
sport_car.turn()
sport_car.turn()
sport_car.stop()
print()
police_car.go()
police_car.show_speed()
police_car.turn()
police_car.turn()
police_car.stop()