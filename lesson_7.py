# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

# не задачка. а вынос мозга...
class Matrix:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(el)

    def __str__(self):
        result = '\n'.join(map(str, self.my_list))
        result = result.replace(',', '').replace('[', '').replace(']', '')
        return result
        # return '\n'.join(' '.join(map(str, line)) for line in self.my_list)

    def __add__(self, other):
        my_sum = []
        line_sum = []
        for x in range(len(self.my_list)):
            for y in range(len(self.my_list[x])):
                line_sum.append(self.my_list[x][y] + other.my_list[x][y])  # создаем список сумм элементов каждой строки
            my_sum.append(line_sum)  # вносим каждую строку в виде списка в результируюший список
            line_sum = []  # обнуляем список для внесения сум элементов следующей строки
        return Matrix('\n'.join(map(str, my_sum)))

a = Matrix([1, 2, 3], [6, 7, 8], [2, 3, 4])
print(a)
print()

b = Matrix([10, 11, 12], [13, 14, 15], [16, 17, 18])
print(b)
print()

print(f'Сумма матриц:\n{a + b}')

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора +@property.
#
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def calculation(self):
        pass

class Coat(Clothes):
    def __init__(self, size, height=None):
        super().__init__(size, height)

    def calculation(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height, size=None):
        super().__init__(size, height)

    def calculation(self):
        return 2 * self.height + 0.3


class Full_material(Clothes):
    @property
    def calculation(self):
        return f'Расход ткани на пошив пальто = {Coat.calculation(self)}\nРасход ткани на пошив костюма {Suit.calculation(self)}\nОбщий расход ткани = {round(Coat.calculation(self) + Suit.calculation(self), 2)}'

anna = Coat(50)
print(f'Расход ткани на пошив пальто anna = {anna.calculation()}')

sergei = Suit(17)
print(f'Расход ткани на пошив костюма sergei = {sergei.calculation()}\n')

kate = Full_material(50, 17)
print(kate.calculation)

# Вариант решения без абстрактных классов. Выглядит лаконичнее
# class Clothes:
#
#     def __init__(self, size, height):
#         self.size = size
#         self.height = height
#
#     def coat_material(self):
#         return round(self.size / 6.5 + 0.5, 2)
#
#     def suit_material(self):
#         return 2 * self.height + 0.3
#
#     @property
#     def full_material(self):
#         return round(self.size / 6.5 + 0.5 + 2 * self.height + 0.3, 2)
#
# kate = Clothes(50, 40)
#
# print(kate.coat_material())
# print(kate.suit_material())
# print(kate.full_material)

# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, count: int):
        self.count = count

    def __str__(self):
        return f'Результат = {self.count * "*"}'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count > 0:
            return Cell(self.count - other.count)
        else:
            return f'Вычитание клеток невозможно'

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        if self.count // other.count >= 1:
            return Cell(self.count // other.count)
        else:
            return f'Целочисленное деление клеток невозможно'

    def make_order(self, row):
        line = ''
        for i in range(self.count // row):
            line += ("*" * row) + '\n'
        if self.count % row != 0:
            line += "*" * (self.count % row)
        return line

a = Cell(10)
b = Cell(15)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(3))
print('\n' + b.make_order(5))

