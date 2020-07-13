# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def get_int(cls, date):
        day = int(date.split('-')[0])
        month = int(date.split('-')[1])
        year = int(date.split('-')[2])
        print(f'day: {day}, month: {month}, year: {year}')

    @staticmethod
    def validation(day, month, year):
        if day in range(1, 32):
            if month in range(1, 13):
                if year <= 2020:
                    print('Дата введена верно!')
                else:
                    print('Неверно указан год!')
            else:
                print('Неверно указан месяц!')
        else:
            print('Дата указан день!')


Date.get_int('10-12-2018')
Date.validation(10, 12, 2018)
Date.validation(10, 13, 2018)


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __init__(self, divisor):
        self.divisor = divisor

    def __str__(self):
        return f'На ноль делить нельзя!'


class Numbers:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def division(self):
        if self.divisor == 0:
            raise MyException(self.divisor)
        else:
            print(f'Результат деления: {self.dividend / self.divisor}')


user_dividend = int(input("Введите делимое >>>"))
user_divisor = int(input("Введите делитель >>>"))
a = Numbers(user_dividend, user_divisor)

try:
    a.division()
except MyException:
    print('Деление на ноль недопустимо!')


# a.division() - если ввести 0 как делитель, то вместо ZeroDivisionError будет MyException

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только
# чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не
# остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его
# в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст
# (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class MyExeption(Exception):
    def __str__(self):
        return f'Вы ввели не число'


class JustNumbers:
    def __init__(self, el):
        self.el = el

    def list_creating(self):
        if str(self.el).isdigit():
            return self.el
        else:
            raise MyExeption


result = []

while True:
    user_input = input('Введите значение или stop для выхода \n')
    if user_input == 'stop':
        print(f'Ваш список чисел: {result}')
        exit()
    try:
        a = JustNumbers(user_input)
        a.list_creating()
        result.append(user_input)
    except MyExeption:
        print('Вы ввели не число. Попробуйте еще раз')


# реализация без класса-исключения, выглядит лучше...
# class JustNumbers:
#     def __init__(self):
#         self.my_list = []
#
#     def list_creating(self):
#         while True:
#             user_input = input('Введите значение или stop для выхода \n')
#             if user_input == 'stop':
#                  print(self.my_list)
#                  exit()
#             elif str(user_input).isdigit():
#                 self.my_list.append(user_input)
#             else:
#                 print('Вы ввели не число. Попробуйте еще раз')
#
# a = JustNumbers()
# a.list_creating()

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Stock:
    max_count: int
    equipment: dict

    def __init__(self, count=0):
        self.max_count = count
        self.equipment = {}

    def store(self, equipment: dict):
        if sum(equipment.values()) > (self.max_count - sum(self.equipment.values())):
            raise CapacityException(self.max_count, sum(self.equipment.values()) + sum(equipment.values()))

        self.equipment.update(equipment)

    def transfer_to_division(self, name, division):
        self.name = name
        self.division = division
        self.equipment.pop(self.name)
        print(f'{self.name} передан в {division}')

    def __str__(self):
        return f'В данный момент на складе: {self.equipment}. Еще доступно мест: {self.max_count - sum(self.equipment.values())}'


class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f'Недостаточно места на складе, доступно = {self.current}, необходимо = {self.needle}'


class Equipment:
    name: str
    price: float
    qty: int

    def __init__(self, name, price, qty, *args):
        self.name = name
        self.price = price
        self.qty = qty

    def enter(self):
        user_name = input("Введите название оборудования")
        user_price = input("Введите цену")
        user_qty = input("Введите количество")
        user_arg = input("Введите кол-во страниц для принтера, тип для сканера или скорость для ксерокса")
        return user_name, user_price, user_qty, user_arg

    @staticmethod
    def validation(name, price, qty):
        if type(name) is str:
            if price > 0:
                if type(qty) is int:
                    print('Данные введены корректно!')
                else:
                    print('Введите количество оборудования в виде числа')
            else:
                print('Цена должны быть положительным числом')
        else:
            print('Неверно указано название оборудования!')

    @property
    def get_name_qty(self):
        return {self.name: self.qty}


class Printer(Equipment):
    def __init__(self, name, price, qty, qty_pages):
        super().__init__(name, price, qty)
        self.qty_pages = qty_pages

    def to_print(self):
        return f'{self.name} печатает {self.qty_pages} страниц'


class Scanner(Equipment):
    def __init__(self, name, price, qty, type):
        super().__init__(name, price, qty)
        self.type = type

    def to_scan(self):
        return f'тип {self.name}: {self.type}'


class Copier(Equipment):
    def __init__(self, name, price, qty, speed):
        super().__init__(name, price, qty)
        self.speed = speed

    def to_copier(self):
        return f'{self.name} копирует {self.speed} страниц в сутки'


stock = Stock(10)

printer_1 = Printer('принтер1', 10000.5, 1, 200000)
printer_2 = Printer('принтер2', 5000, 2, 100000)
scanner_1 = Scanner('сканер1', 6000, 3, 'планшетный')
copier_1 = Copier('ксерокс1', 4000, 3, 22000)

Equipment.validation('принтер1', -10000.5, 1)
Equipment.validation('принтер2', 5000, '2')
Equipment.validation(156, 5000, 2)
Equipment.validation('сканер1', 6000, 3)
print()

print(printer_1.to_print())
print(scanner_1.to_scan())
print(copier_1.to_copier())
print()

try:
    stock.store({'принтер 1': 1, 'принтер 2': 2, 'сканер 1': 3, 'ксерокс 1': 5})
except CapacityException as exeption:
    print(f'Необходимо еще {exeption.needle - exeption.current} место')

stock.store(printer_1.get_name_qty)
stock.store(printer_2.get_name_qty)
stock.store(scanner_1.get_name_qty)
stock.store(copier_1.get_name_qty)
print(stock)
print()
stock.transfer_to_division(printer_1.name, "Отдел продаж")
stock.transfer_to_division(copier_1.name, "Доставка")
print(stock)


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0 and self.a != 0:
            return f'{self.a}+{self.b}i'
        elif self.b < 0 and self.a != 0:
            return f'{self.a}{self.b}i'
        elif self.b == 0 and self.a != 0:
            return f'{self.a}'
        elif self.a == 0 and self.b != 0:
            return f'{self.b}i'
        elif self.a == 0 and self.b == 0:
            return "0"

    def __add__(self, other):
        if self.b + other.b > 0 and self.a + other.a != 0:
            return f'{self.a + other.a}+{self.b + other.b}i'
        elif self.b + other.b < 0 and self.a + other.a != 0:
            return f'{self.a + other.a}{self.b + other.b}i'
        elif self.b == 0 and self.a + other.a != 0:
            return f'{self.a + other.a}'
        elif self.a + other.a == 0 and self.b != 0:
            return f'{self.b + other.b}i'
        elif self.a + other.a == 0 and self.b + other.b == 0:
            return "0"

    def __mul__(self, other):
        if self.a * other.b + self.b * other.a > 0 and self.a * other.a - self.b * other.b != 0:
            return f'{self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}i'
        elif self.a * other.b + self.b * other.a < 0 and self.a * other.a - self.b * other.b != 0:
            return f'{self.a * other.a - self.b * other.b}{self.a * other.b + self.b * other.a}i'
        elif self.a * other.b + self.b * other.a == 0 and self.a * other.a - self.b * other.b != 0:
            return f'{self.a * other.a - self.b * other.b}'
        elif self.a * other.a - self.b * other.b == 0 and self.a * other.b + self.b * other.a != 0:
            return f'{self.a * other.b + self.b * other.a}i'
        elif self.a * other.a - self.b * other.b == 0 and self.a * other.b + self.b * other.a == 0:
            return "0"


z1 = Complex_number(2, 3)
z2 = Complex_number(-1, 1)
print(z1)
print(z2)
print()
print(z1 + z2)
print()
print(z1 * z2)
