# class User:
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
#     def __len__(self):
#         return self.old
#
# user1 = User('Sergey', 45)
# user2 = User('Петр', 0)
#
# print(bool(user1))
# print(bool(user2))

# class User:
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
#     def __len__(self):
#         return self.old + 1
#
#     def __bool__(self):
#         return bool(self.old)
#
# user1 = User('Sergey', 45)
# user2 = User('Петр', 0)

# print(bool(user1))
# print(bool(user2))

# 4
# Объявите в программе класс Player (игрок),
# объекты которого создаются командой:
#
# player = Player(name, old, score)
#
# где
# name - имя игрока (строка);
# old - возраст игрока (целое число);
# score - набранные очки в игре (целое число).
# В каждом объекте класса Player должны
# создаваться аналогичные локальные атрибуты:
# name, old, score.
#
# С объектами класса Player должна работать функция:
#
# bool(player)
#
# которая возвращает True, если число очков
# больше нуля, и False - в противном случае.
#
# С помощью команды:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# считываются строки из входного потока в список строк lst_in. Каждая строка записана в формате:
#
# "имя; возраст; очки"
#
# Например:
#
# Балакирев; 34; 2048
# Mediel; 27; 0
# Влад; 18; 9012
# Nina P; 33; 0
#
# Каждую строку списка lst_in необходимо
# представить в виде объекта класса Player
# с соответствующими данными. И из этих
# объектов сформировать список players.
#
# Отфильтруйте этот список
# (создайте новый: players_filtered),
# оставив всех игроков с числом очков
# больше нуля. Используйте для этого
# стандартную функцию filter() совместно
# с функцией bool() языка Python.
#
# P.S. На экран ничего выводить не нужно.

# import sys
#
# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = old
#         self.score = score
#
#     def __bool__(self):
#         return self.score > 0
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# players = []
# for line in lst_in:
#     name, old, score = line.split("; ")
#     player = Player(name, int(old), int(score))
#     players.append(player)
#
# players_filtered = list(filter(bool, players))

# 5
# Объявите в программе класс MailBox
# (почтовый ящик), объекты которого
# создаются командой:
#
# mail = MailBox()
#
# Каждый объект этого класса должен
# содержать локальный публичный атрибут:
#
# inbox_list - список из принятых писем.
#
# Также в классе MailBox должен
# присутствовать метод:
#
# receive(self) - прием новых писем
#
# Этот метод должен читать данные
# из входного потока командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# В результате формируется список
# lst_in из строк. Каждая строка записана в формате:
#
# "от кого; заголовок; текст письма"
#
# Например:
#
# sc_lib@list.ru; От Балакирева; Успехов в IT!
# mail@list.ru; Выгодное предложение; Вам одобрен кредит.
# mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.
#
# Каждая строчка списка lst_in должна быть
# представлена объектом класса MailItem,
# объекты которого создаются командой:
#
# item = MailItem(mail_from, title, content)
#
# где
# mail_from - email отправителя (строка);
# title - заголовок письма (строка),
# content - содержимое письма (строка).
# В каждом объекте класса MailItem
# должны формироваться соответствующие
# локальные атрибуты
# (с именами: mail_from, title, content).
# И дополнительно атрибут is_read
# (прочитано ли) с начальным значением False.
#
# В классе MailItem должен
# быть реализован метод:
#
# set_read(self, fl_read) - для отметки,
#   что письмо прочитано (метод должен
#   устанавливать атрибут is_read = fl_read,
#   если True, то письмо прочитано,
#   если False, то не прочитано).
#
# С каждым объектом класса MailItem
# должна работать функция:
#
# bool(item)
#
# которая возвращает True для прочитанного
# письма и False для непрочитанного.
#
# Вызовите метод:
#
# mail.receive()
#
# Отметьте первое и последнее письмо
# в списке mail.inbox_list, как
# прочитанное (используйте для этого
# метод set_read). Затем, сформируйте
# в программе список (глобальный)
# с именем inbox_list_filtered из
# прочитанных писем, используя
# стандартную функцию filter()
# совместно с функцией bool() языка Python.
#
# P.S. На экран ничего выводить не нужно.

# import sys
#
# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False
#
#     def set_read(self, fl_read):
#         self.is_read = fl_read
#
#     def __bool__(self):
#         return self.is_read
#
# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
#
#     def receive(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         for line in lst_in:
#             mail_from, title, content = line.split("; ")
#             item = MailItem(mail_from, title, content)
#             self.inbox_list.append(item)
#
# mail = MailBox()
# mail.receive()
#
# if mail.inbox_list:
#     mail.inbox_list[0].set_read(True)
#     mail.inbox_list[-1].set_read(True)
#
# inbox_list_filtered = list(filter(bool, mail.inbox_list))

# 6
# Объявите класс Line, объекты
# которого создаются командой:
#
# line = Line(x1, y1, x2, y2)
#
# где x1, y1, x2, y2 - координаты
# начала линии (x1, y1) и координаты
# конца линии (x2, y2). Могут быть
# произвольными числами. В объектах
# класса Line должны создаваться
# соответствующие локальные атрибуты
# с именами x1, y1, x2, y2.
#
# В классе Line определить
# магический метод
# __len__() так, чтобы функция:
#
# bool(line)
#
# возвращала False, если
# длина линии меньше 1.
#
# P.S. На экран ничего выводить
# не нужно. Только объявить класс.

# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def __len__(self):
#         length = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
#         return int(length)
#
#     def __bool__(self):
#         return len(self) >= 1

# 7
# Объявите класс Ellipse (эллипс),
# объекты которого создаются командами:
#
# el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
# el2 = Ellipse(x1, y1, x2, y2)
#
# где
# x1, y1 - координаты (числа) левого верхнего угла;
# x2, y2 - координаты (числа) нижнего правого угла.
# Первая команда создает объект класса
# Ellipse без локальных атрибутов
# x1, y1, x2, y2. Вторая команда создает
# объект с локальными атрибутами
# x1, y1, x2, y2 и соответствующими
# переданными значениями.
#
# В классе Ellipse объявите магический
# метод __bool__(), который бы возвращал
# True, если все локальные атрибуты
# x1, y1, x2, y2 существуют и False -
# в противном случае.
#
# Также в классе Ellipse нужно
# реализовать метод:
#
# get_coords() - для получения кортежа
# текущих координат объекта.
#
# Если координаты отсутствуют (нет локальных
# атрибутов x1, y1, x2, y2), то метод
# get_coords() должен генерировать
# исключение командой:
#
# raise AttributeError('нет координат для извлечения')
#
# Сформируйте в программе список с именем
# lst_geom, содержащий четыре объекта
# класса Ellipse. Два объекта должны
# быть созданы командой
#
# Ellipse()
#
# и еще два - командой:
#
# Ellipse(x1, y1, x2, y2)
#
# Переберите список в цикле и вызовите
# метод get_coords() только для объектов,
# имеющих координаты x1, y1, x2, y2.
# (Помните, что для этого был определен
# магический метод __bool__()).
#
# P.S. На экран ничего выводить не нужно.

# class Ellipse:
#     def __init__(self, x1=None, y1=None, x2=None, y2=None):
#         if all(v is not None for v in [x1, y1, x2, y2]):
#             self.x1 = x1
#             self.y1 = y1
#             self.x2 = x2
#             self.y2 = y2
#
#     def __bool__(self):
#         return hasattr(self, 'x1') and hasattr(self, 'y1') and hasattr(self, 'x2') and hasattr(self, 'y2')
#
#     def get_coords(self):
#         if self.__bool__():
#             return (self.x1, self.y1, self.x2, self.y2)
#         else:
#             raise AttributeError('нет координат для извлечения')
#
#
# lst_geom = [Ellipse(), Ellipse(), Ellipse(x1=1, y1=2, x2=3, y2=4), Ellipse(x1=5, y1=6, x2=7, y2=8)]
#
# for ellipse in lst_geom:
#     if ellipse:
#         ellipse.get_coords()

# 8
# Вы начинаете разрабатывать игру
# "Сапер". Для этого вам нужно уметь
# представлять и управлять игровым полем.
# Будем полагать, что оно имеет размеры
# N x M клеток. Каждая клетка будет
# представлена объектом класса Cell и
# содержать либо число мин вокруг этой
# клетки, либо саму мину.
# ...pic...
# Для начала в программе объявите класс
# GamePole, который будет создавать и
# управлять игровым полем. Объект этого
# класса должен формироваться командой:
#
# pole = GamePole(N, M, total_mines)
#
# И, так как поле в игре одно, то нужно
# контролировать создание только одного
# объекта класса GamePole (используйте
# паттерн Singleton, о котором мы с вами
# говорили, когда рассматривали магический
# метод __new__()).
#
# Объект pole должен иметь локальный
# приватный атрибут:
#
# __pole_cells - двумерный (вложенный)
# кортеж, размерами N x M элементов
# (N строк и M столбцов), состоящий
# из объектов класса Cell.
#
# Для доступа к этой коллекции объявите
# в классе GamePole объект-свойство
# (property):
#
# pole - только для чтения (получения)
# ссылки на коллекцию __pole_cells.
#
# Далее, в самом классе GamePole
# объявите следующие методы:
#
# init_pole() - для инициализации начального
#   состояния игрового поля (расставляет
#   мины и делает все клетки закрытыми);
# open_cell(i, j) - открывает ячейку с
#   индексами (i, j); нумерация индексов
#   начинается с нуля; метод меняет значение
#   атрибута __is_open объекта Cell в
#   ячейке (i, j) на True;
# show_pole() - отображает игровое поле
#   в консоли (как именно сделать - на
#   ваше усмотрение, этот метод - домашнее
#   задание).
#
# Расстановку мин выполняйте случайным
# образом по игровому полю (для этого
# удобно воспользоваться функцией randint
# модуля random). После расстановки всех
# total_mines мин, вычислите их количество
# вокруг остальных клеток (где нет мин).
# Область охвата - соседние (прилегающие)
# клетки (8 штук).
#
# В методе open_cell() необходимо проверять
# корректность индексов (i, j). Если
# индексы указаны некорректно, то
# генерируется исключение командой:
#
# raise IndexError('некорректные индексы i, j клетки игрового поля')
#
# Следующий класс Cell описывает состояние
# одной ячейки игрового поля. Объекты
# этого класса создаются командой:
#
# cell = Cell()
#
# При этом в самом объекте создаются
# следующие локальные приватные свойства:
#
# __is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
# __number - число мин вокруг клетки (целое число от 0 до 8);
# __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
#
# Для работы с этими приватными атрибутами
# объявите в классе Cell следующие
# объекты-свойства с именами:
#
# is_mine - для записи и чтения информации из атрибута __is_mine;
# number - для записи и чтения информации из атрибута __number;
# is_open - для записи и чтения информации из атрибута __is_open.
#
# В этих свойствах необходимо выполнять
# проверку на корректность переданных
# значений (либо булево значение
# True/False, либо целое число от 0 до 8).
# Если передаваемое значение некорректно,
# то генерировать исключение командой:
#
# raise ValueError("недопустимое значение
# атрибута")
#
# С объектами класса Cell должна работать
# функция:
#
# bool(cell)
#
# которая возвращает True, если клетка
# закрыта и False - если открыта.
#
# Пример использования классов
# (эти строчки в программе писать не нужно):
#
# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()
#
# P.S. В программе на экран выводить
# ничего не нужно, только объявить классы.

# from random import randint
#
# class Singleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
# class Cell:
#     def __init__(self):
#         self.__is_mine = False
#         self.__number = 0
#         self.__is_open = False
#
#     @property
#     def is_mine(self):
#         return self.__is_mine
#
#     @is_mine.setter
#     def is_mine(self, value):
#         if not isinstance(value, bool):
#             raise ValueError("недопустимое значение атрибута")
#         self.__is_mine = value
#
#     @property
#     def number(self):
#         return self.__number
#
#     @number.setter
#     def number(self, value):
#         if not 0 <= value <= 8:
#             raise ValueError("недопустимое значение атрибута")
#         self.__number = value
#
#     @property
#     def is_open(self):
#         return self.__is_open
#
#     @is_open.setter
#     def is_open(self, value):
#         if not isinstance(value, bool):
#             raise ValueError("недопустимое значение атрибута")
#         self.__is_open = value
#
#     def __bool__(self):
#         return not self.__is_open
#
# class GamePole(metaclass=Singleton):
#     def __init__(self, N, M, total_mines):
#         self.N = N
#         self.M = M
#         self.total_mines = total_mines
#         self.__pole_cells = [[Cell() for _ in range(M)] for _ in range(N)]
#
#     @property
#     def pole(self):
#         return self.__pole_cells
#
#     def init_pole(self):
#         mine_count = 0
#         while mine_count < self.total_mines:
#             i, j = randint(0, self.N - 1), randint(0, self.M - 1)
#             if not self.__pole_cells[i][j].is_mine:
#                 self.__pole_cells[i][j].is_mine = True
#                 mine_count += 1
#         for i in range(self.N):
#             for j in range(self.M):
#                 if not self.__pole_cells[i][j].is_mine:
#                     self.__pole_cells[i][j].number = self.count_mines(i, j)
#
#     def open_cell(self, i, j):
#         if i < 0 or i >= self.N or j < 0 or j >= self.M:
#             raise IndexError('некорректные индексы i, j клетки игрового поля')
#         self.__pole_cells[i][j].is_open = True
#
#     def show_pole(self):
#         for i in range(self.N):
#             for j in range(self.M):
#                 cell = self.__pole_cells[i][j]
#                 if cell.is_open:
#                     if cell.is_mine:
#                         print("*", end=" ")
#                     else:
#                         print(cell.number, end=" ")
#                 else:
#                     print("#", end=" ")
#             print()
#
#     def count_mines(self, i, j):
#         count = 0
#         for k in range(max(0, i-1), min(self.N, i+2)):
#             for l in range(max(0, j-1), min(self.M, j+2)):
#                 if self.__pole_cells[k][l].is_mine:
#                     count += 1
#         return count
# # пример
# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# # pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()

# # Тесты
# p1 = GamePole(10, 20, 10)
# p2 = GamePole(10, 20, 10)
# assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
# p = p1
#
# cell = Cell()
# assert type(Cell.is_mine) == property and type(Cell.number) == property and type(Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"
#
# cell.is_mine = True
# cell.number = 5
# cell.is_open = True
# assert bool(cell) == False, "функция bool() вернула неверное значение"
#
# try:
#     cell.is_mine = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# try:
#     cell.number = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# p.init_pole()
# m = 0
# for row in p.pole:
#     for x in row:
#         assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
#         if x.is_mine:
#             m += 1
#
# assert m == 10, "на поле расставлено неверное количество мин"
# p.open_cell(0, 1)
# p.open_cell(9, 19)
#
# try:
#     p.open_cell(10, 20)
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
# def count_mines(pole, i, j):
#     n = 0
#     for k in range(-1, 2):
#         for l in range(-1, 2):
#             ii, jj = k+i, l+j
#             if ii < 0 or ii > 9 or jj < 0 or jj > 19:
#                 continue
#             if pole[ii][jj].is_mine:
#                 n += 1
#     return n
#
# for i, row in enumerate(p.pole):
#     for j, x in enumerate(row):
#         if not p.pole[i][j].is_mine:
#             m = count_mines(p.pole, i, j)
#             assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"

# 9
# Объявите в программе класс Vector,
# объекты которого создаются командой:
#
# v = Vector(x1, x2, x3,..., xN)
#
# где x1, x2, x3,..., xN - координаты
# вектора (числа: целые или вещественные).
#
# С каждым объектом класса Vector должны выполняться операторы:
#
# v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторов
# v1 * v2 # умножение соответствующих координат векторов
#
# v1 += 10 # прибавление ко всем координатам вектора числа 10
# v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1
#
# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
#
# При реализации бинарных операторов
# +, -, * следует создавать новые объекты
# класса Vector с новыми (вычисленными)
# координатами. При реализации операторов
# +=, -= координаты меняются в текущем
# объекте, не создавая новый.
#
# Если число координат (размерность)
# векторов v1 и v2 не совпадает, то при
# операторах +, -, * должно генерироваться
# исключение командой:
#
# raise ArithmeticError('размерности векторов не совпадают')
#
# P.S. В программе на экран выводить ничего не нужно,
# только объявить класс.

# class Vector:
#     def __init__(self, *args):
#         self.coordinates = list(args)
#
#     def __add__(self, other):
#         if len(self.coordinates) != len(other.coordinates):
#             raise ArithmeticError('размерности векторов не совпадают')
#         return Vector(*(x + y for x, y in zip(self.coordinates, other.coordinates)))
#     '''
# Инструкция Vector(*(x + y for x, y in zip(self.coordinates, other.coordinates)))
# выполняет сложение или другую операцию поэлементно
# для списков self.coordinates и other.coordinates,
# используя функцию zip для обхода элементов обоих
# списков одновременно.
# Чтобы объяснить это более подробно, рассмотрим пример:
# Предположим, что у нас есть два списка
# self.coordinates и other.coordinates:
#
# self.coordinates = [1, 2, 3]
# other.coordinates = [4, 5, 6]
#
# Тогда выражение zip(self.coordinates, other.coordinates)
# создаст объект zip, который будет содержать пары элементов списков:
#
# (1, 4), (2, 5), (3, 6)
#
# Затем, используя генератор списка
# (x + y for x, y in zip(self.coordinates, other.coordinates)),
# мы пройдемся по каждой паре элементов из zip и
# сложим их, создавая новый список с результатами сложения:
#
# [1 + 4, 2 + 5, 3 + 6] = [5, 7, 9]
#
# Наконец, оператор * распакует этот список,
# чтобы его элементы стали аргументами конструктора
# Vector, создавая новый объект Vector с результатами
# операции сложения (или другой операции,
# в зависимости от контекста).
#     '''
#
#     def __sub__(self, other):
#         if len(self.coordinates) != len(other.coordinates):
#             raise ArithmeticError('размерности векторов не совпадают')
#         return Vector(*(x - y for x, y in zip(self.coordinates, other.coordinates)))
#
#     def __mul__(self, other):
#         if len(self.coordinates) != len(other.coordinates):
#             raise ArithmeticError('размерности векторов не совпадают')
#         return Vector(*(x * y for x, y in zip(self.coordinates, other.coordinates)))
#
#     def __iadd__(self, other):
#         if isinstance(other, (int, float)):
#             self.coordinates = [x + other for x in self.coordinates]
#         else:
#             if len(self.coordinates) != len(other.coordinates):
#                 raise ArithmeticError('размерности векторов не совпадают')
#             self.coordinates = [x + y for x, y in zip(self.coordinates, other.coordinates)]
#         return self
#
#     def __isub__(self, other):
#         if isinstance(other, (int, float)):
#             self.coordinates = [x - other for x in self.coordinates]
#         else:
#             if len(self.coordinates) != len(other.coordinates):
#                 raise ArithmeticError('размерности векторов не совпадают')
#             self.coordinates = [x - y for x, y in zip(self.coordinates, other.coordinates)]
#         return self
#
#     def __eq__(self, other):
#         return self.coordinates == other.coordinates
#
#     def __ne__(self, other):
#         return self.coordinates != other.coordinates

