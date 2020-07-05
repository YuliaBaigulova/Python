# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
# (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

from time import sleep

class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def running(self):
        for i in range(3):
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(2)
            elif i == 1:
                sleep(7)
            elif i == 2:
                sleep(1)

a = TrafficLight()
a.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _lenght: int
    _width: int

    def __init__(self, lenght, width, mass, thickness):
        self._lenght = lenght
        self._width = width
        self.mass = mass  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1, кг
        self.thickness = thickness  # толщина полотна, см

    def calculation(self):
        return self._lenght * self._width * self.mass * self.thickness

a = Road(20, 5000, 25, 5)
print(f"Масса асфальта, необходимого для покрытия всего дорожного полотнаa = {a.calculation()} кг")

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход = {self._income["wage"] + self._income["bonus"]} руб.')

a = Position("Сергей", "Иванов", "мастер", 75000, 5000)
a.get_full_name()
print(f"Должность: {a.position}")
a.get_total_income()

b = Position("Оксана", "Григорьева", "бухгалтер", 55000, 10000)
b.get_full_name()
print(f"Должность: {b.position}")
b.get_total_income()

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} = {self.speed}')


class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} = {self.speed}')
        if self.speed > 60:
            print(f'Автомобиль {self.name} превысил допустимую скорость. Максимальная скорость = 60 км/ч')


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} = {self.speed}')
        if self.speed > 40:
            print(f'Автомобиль {self.name} превысил допустимую скорость. Максимальная скорость = 40 км/ч')


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool = True):
        super().__init__(speed, color, name, is_police)


mazda = TownCar(0, "черный", "mazda")
mazda.show_speed()
mazda.go()
mazda.turn_left()
mazda = TownCar(70, "черный", "mazda")
mazda.show_speed()
mazda.stop()

opel = WorkCar(45, "красный", "опель")
nissan = PoliceCar(55, "белый", "ниссан")
opel.show_speed()
nissan.show_speed()
print(nissan.is_police)
print(opel.is_police)

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка ручкой - {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка карандашом - {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка маркером - {self.title}")

a = Pen("Ручка 1")
b = Pencil("Карандаш 1")
c = Handle("Маркер 1")
a.draw()
b.draw()
c.draw()
