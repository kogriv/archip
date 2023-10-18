# class PathLine:
#     def __init__(self, dist, angle):
#         self.dist = dist
#         self.angle = angle
#
#     def __eq__(self, other):
#         return abs(self.dist) == abs(other.dist)
#
# p1 = PathLine(10, 1.57)
# p2 = PathLine(-10, 0.49)
#
# h1, h2 = hash(p1), hash(p2)

# 4
# Объявите в программе класс с именем Rect
# (прямоугольник), объекты которого
# создаются командой:
#
# rect = Rect(x, y, width, height)
#
# где
# x, y - координата верхнего левого
#   угла (числа: целые или вещественные);
# width, height - ширина и высота прямоугольника
#   (числа: целые или вещественные).
#
# В этом классе определите магический метод,
# чтобы хэши объектов класса Rect с равными width,
# height были равны. Например:
#
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
#
# h1, h2 = hash(r1), hash(r2)   # h1 == h2
#
# P.S. На экран ничего выводить не нужно,
# только объявить класс.

# 6
# Объявите класс с именем ShopItem (товар),
# объекты которого создаются командой:
#
# item = ShopItem(name, weight, price)
#
# где
# name - название товара (строка);
# weight - вес товара (число: целое или вещественное);
# price - цена товара (число: целое или вещественное).
#
# Определите в этом классе магические методы:
#
# __hash__() - чтобы товары с одинаковым названием
#   (без учета регистра), весом и ценой имели бы равные хэши;
# __eq__() - чтобы объекты с одинаковыми хэшами были равны.
#
# Затем, из входного потока прочитайте строки командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Строки имеют следующий формат:
#
# название товара 1: вес_1 цена_1
# ...
# название товара N: вес_N цена_N
#
# Например:
#
# Системный блок: 1500 75890.56
# Монитор Samsung: 2000 34000
# Клавиатура: 200.44 545
# Монитор Samsung: 2000 34000
#
# Как видите, товары в этом списке могут совпадать.
#
# Необходимо для всех этих строчек сформировать
# соответствующие объекты класса ShopItem и
# добавить в словарь с именем shop_items.
# Ключами словаря должны выступать сами объекты,
# а значениями - список в формате:
#
# [item, total]
#
# где
# item - объект класса ShopItem;
# total - общее количество одинаковых объектов
#   (с одинаковыми хэшами).
#   Подумайте, как эффективно программно наполнять
#   такой словарь, проходя по списку lst_in один раз.
#
# P.S. На экран ничего выводить не нужно,
# только объявить класс и сформировать словарь.
#
# Sample Input:
#
# Системный блок: 1500 75890.56
# Монитор Samsung: 2000 34000
# Клавиатура: 200.44 545
# Монитор Samsung: 2000 34000
#
# Sample Output:

# import sys
#
# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.weight, self.price))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # lst_in = [
# # 'Системный блок: 1500 75890.56',
# # 'Монитор Samsung: 2000 34000',
# # 'Клавиатура: 200.44 545',
# # 'Монитор Samsung: 2000 34000'
# # ]
#
# shop_items = {}
#
# for line in lst_in:
#     parts = line.split(':')
#     name = parts[0].strip()
#     weight, price = map(float, parts[1].split())
#     item = ShopItem(name, weight, price)
#     if item in shop_items:
#         shop_items[item][1] += 1
#     else:
#         shop_items[item] = [item, 1]
#
# print(shop_items)

# it1 = ShopItem('name', 10, 11)
# it2 = ShopItem('name', 10, 11)
# assert hash(it1) == hash(it2), "разные хеши у равных объектов"
#
# it2 = ShopItem('name', 10, 12)
# assert hash(it1) != hash(it2), "равные хеши у разных объектов"
#
# it2 = ShopItem('name', 11, 11)
# assert hash(it1) != hash(it2), "равные хеши у разных объектов"
#
# it2 = ShopItem('NAME', 10, 11)
# assert hash(it1) == hash(it2), "разные хеши у равных объектов"
#
# name = lst_in[0].split(':')
# for sp in shop_items.values():
#     assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"
#
# v = list(shop_items.values())
# if v[0][0].name.strip() == "Системный блок":
#     assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"
#
# if v[0][0].name.strip() == "X-box":
#     assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"

# 7
# Объявите класс с именем DataBase (база
# данных - БД), объекты которого
# создаются командой:
#
# db = DataBase(path)
#
# где path - путь к файлу с данными БД (строка).
#
# Также в классе DataBase нужно объявить
# следующие методы:
#
# write(self, record) - для добавления
#   новой записи в БД, представленной
#   объектом record;
# read(self, pk) - чтение записи из БД
#   (возвращает объект Record) по ее
#   уникальному идентификатору pk (уникальное
#   целое положительное число); запись ищется
#   в значениях словаря (см. ниже)
#
# Каждая запись БД должна описываться классом
# Record, а объекты этого класса
# создаваться командой:
#
# record = Record(fio, descr, old)
#
# где fio - ФИО некоторого человека
# (строка); descr - характеристика человека
# (строка); old - возраст человека (целое число).
#
# В каждом объекте класса Record должны
# формироваться следующие локальные атрибуты:
#
# pk - уникальный идентификатор записи
# (число: целое, положительное);
# формируется автоматически при создании
# каждого нового объекта;
# fio - ФИО человека (строка);
# descr - характеристика человека (строка);
# old - возраст человека (целое число).
#
# Реализовать для объектов класса Record
# вычисление хэша по атрибутам:
# fio и old (без учета регистра).
# Если они одинаковы для разных записей,
# то и хэши должны получаться равными.
# Также для объектов класса Record  с
# одинаковыми хэшами оператор == должен
# выдавать значение True,
# а с разными хэшами - False.
#
# Хранить записи в БД следует в виде словаря
# dict_db (атрибут объекта db класса DataBase),
# ключами которого являются объекты класса
# Record, а значениями список из объектов с
# равными хэшами:
#
# dict_db[rec1] = [rec1, rec2, ..., recN]
#
# где rec1, rec2, ..., recN - объекты
# класса Record с одинаковыми хэшами.
#
# Для наполнения БД прочитайте строки из
# входного потока с помощью команды:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# где каждая строка представлена в формате:
#
# "ФИО; характеристика; возраст"
#
# Например:
#
# Балакирев С.М.; программист; 33
# Кузнецов А.В.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 37
#
# Каждая строка должна быть представлена
# объектом класса Record и записана в БД db
# (в словарь db.dict_db).
#
# P.S. На экран ничего выводить не нужно.

# import sys
#
# class Record:
#     def __init__(self, fio, descr, old):
#         self.fio = fio
#         self.descr = descr
#         self.old = old
#         self.pk = id(self)
#
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
# class DataBase:
#     def __init__(self, path):
#         self.path = path
#         self.dict_db = {}
#
#     def write(self, record):
#         if record in self.dict_db:
#             self.dict_db[record].append(record)
#         else:
#             self.dict_db[record] = [record]
#
#     def read(self, pk):
#         for records in self.dict_db.values():
#             for record in records:
#                 if record.pk == pk:
#                     return record
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# db = DataBase('example_path')
#
# for line in lst_in:
#     fio, descr, old = map(str.strip, line.split(';'))
#     record = Record(fio, descr, int(old))
#     db.write(record)

# 8
# Из входного потока необходимо прочитать
# список строк командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Каждая строка содержит информацию об
# учебном пособии в формате:
#
# "Название; автор; год издания"
#
# Например:
#
# Python; Балакирев С.М.; 2020
# Python ООП; Балакирев С.М.; 2021
# Python ООП; Балакирев С.М.; 2022
# Python; Балакирев С.М.; 2021
#
# Необходимо каждую из этих строк
# представить объектом класса BookStudy,
# которые создаются командой:
#
# bs = BookStudy(name, author, year)
#
# где
# name - название пособия (строка);
# author - автор пособия (строка);
# year - год издания (целое число).
# Такие же публичные локальные атрибуты
# должны быть в объектах класса BookStudy.
#
# Для каждого объекта реализовать
# вычисление хэша по двум атрибутам:
# name и author (без учета регистра).
#
# Сформировать список lst_bs из объектов
# класса BookStudy на основе прочитанных
# строк (списка lst_in). После этого
# определить число книг с уникальными
# хэшами. Это число сохранить через
# переменную unique_books (целое число).
#
# P.S. На экран ничего выводить не нужно.
#
# import sys
#
# class BookStudy:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.author.lower()))
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# lst_bs = []
# for line in lst_in:
#     name, author, year = map(str.strip, line.split(';'))
#     book = BookStudy(name, author, int(year))
#     lst_bs.append(book)
#
# unique_books = len(set(hash(book) for book in lst_bs))

# 9
# Объявите класс с именем Dimensions,
# объекты которого создаются командой:
#
# d = Dimensions(a, b, c)
#
# где a, b, c - положительные числа
# (целые или вещественные), описывающие габариты
# некоторого тела: высота, ширина и глубина.
#
# Каждый объект класса Dimensions должен
# иметь аналогичные публичные атрибуты a, b, c
# (с соответствующими числовыми значениями).
# Также для каждого объекта должен вычисляться
# хэш на основе всех трех габаритов: a, b, c.
#
# С помощью функции input() прочитайте из
# входного потока строку, записанную в формате:
#
# "a1 b1 c1; a2 b2 c2; ... ;aN bN cN"
#
# Например:
#
# "1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"
#
# Если какой-либо габарит оказывается отрицательным
# значением или равен нулю, то при создании объектов
# должна генерироваться ошибка командой:
#
# raise ValueError("габаритные размеры должны
# быть положительными числами")
#
# Сформируйте на основе прочитанной строки
# список lst_dims из объектов класса Dimensions.
# После этого отсортируйте этот список по
# возрастанию (неубыванию) хэшей этих объектов
# так, чтобы объекты с равными хэшами стояли
# друг за другом.
#
# P.S. На экран ничего выводить не нужно.

# s_inp = input()  # эту строку (переменную s_inp) в программе не менять
#
# class Dimensions:
#     def __init__(self, a, b, c):
#         if a <= 0 or b <= 0 or c <= 0:
#             raise ValueError("габаритные размеры должны быть положительными числами")
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
#
# lst_dims = []
#
# dimensions_list = s_inp.split(";")
# for dims in dimensions_list:
#     a, b, c = map(float, dims.strip().split())
#     dimension = Dimensions(a, b, c)
#     lst_dims.append(dimension)
#
# lst_dims.sort(key=lambda x: hash(x))

# 10
# Объявите класс с именем Triangle,
# объекты которого создаются командой:
#
# tr = Triangle(a, b, c)
#
# где a, b, c - длины сторон треугольника
# (числа: целые или вещественные). В классе
# Triangle объявите следующие дескрипторы данных:
#
# a, b, c - для записи и считывания
# длин сторон треугольника.
#
# При записи нового значения нужно проверять,
# что присваивается положительное число
# (целое или вещественное). Иначе,
# генерируется исключение командой:
#
# raise ValueError("длины сторон
# треугольника должны быть положительными числами")
#
# Также нужно проверять, что все три стороны
# a, b, c могут образовывать стороны треугольника.
# То есть, должны выполняться условия:
#
# a < b+c; b < a+c; c < a+b
#
# Иначе генерируется исключение командой:
#
# raise ValueError("с указанными длинами
# нельзя образовать треугольник")
#
# Наконец, с объектами класса Triangle
# должны выполняться функции:
#
# len(tr) - возвращает периметр треугольника,
#   приведенный к целому значению с
#   помощью функции int();
# tr() - возвращает площадь треугольника
#   (можно вычислить по формуле Герона:
#   s = sqrt(p * (p-a) * (p-b) * (p-c))
#   где p - полупериметр треугольника).
#
# P.S. На экран ничего выводить не нужно,
# только объявить класс Triangle.

# class PositiveValue:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name, None)
#
#     def __set__(self, instance, value):
#         if type(value) not in (int, float) or value <= 0:
#             raise ValueError("длины сторон треугольника должны быть положительными числами")
#         setattr(instance, self.name, value)
#
#
# class Triangle:
#     a = PositiveValue()
#     b = PositiveValue()
#     c = PositiveValue()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @staticmethod
#     def __is_triangle(a, b, c):
#         if a and b and c:
#             return a < b + c and b < a + c and c < a + b
#         return True
#
#     def __setattr__(self, key, value):
#         # попадем сюда, когда вызовется метод
#         # setattr(instance, self.name, value)
#         # в дескрипторе PositiveValue
#         if (key == 'a' and not self.__is_triangle(value, self.b, self.c)) or \
#                 (key == 'b' and not self.__is_triangle(self.a, value, self.c)) or \
#                 (key == 'c' and not self.__is_triangle(self.a, self.b, value)):
#             raise ValueError("с указанными длинами нельзя образовать треугольник")
#
#         super().__setattr__(key, value)
#
#     def __len__(self):
#         # так не пройдет..
#         # Функция len() в Python всегда возвращает
#         # целое число. Она предназначена для
#         # возвращения длины или числа элементов
#         # в структурах данных, таких как списки,
#         # кортежи, и т. д., и поэтому ожидается,
#         # что она вернет только целочисленное
#         # значение. Это часть внутренней реализации
#         # языка Python, и ее изменение может привести
#         # к непредсказуемым последствиям.
#         # if all((self.a, self.b, self.c)):
#         #     if all(isinstance(side, int) for side in (self.a, self.b, self.c)):
#         #         return int(self.a + self.b + self.c)
#         #     else:
#         #         return float(self.a + self.b + self.c)
#         # else:
#         #     return None
#         if all((self.a, self.b, self.c)):
#             return int(self.a + self.b + self.c)
#         else:
#             return None
#
#     def __call__(self):
#         a, b, c = self.a, self.b, self.c
#         if not (a and b and c):
#             return
#         p = 0.5 * (a + b + c)
#         return (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
#
# tr = Triangle(5, 4, 3)
# assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"
#
# try:
#     tr = Triangle(-5, 4, 3)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# try:
#     tr = Triangle(10, 1, 1)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# tr = Triangle(5, 4, 3)
# assert len(tr) == 12, "функция len вернула неверное значение"
# assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
#
# tr = Triangle(3.4, 4, 5)
# assert len(tr) == 12, "функция len вернула неверное значение"
# print(len(tr))  # output - 12
# print(tr())  # output - 6.769815359372811
# tr.a = 1  # raise ValueError: с указанными длинами нельзя образовать треугольник
