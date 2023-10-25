# class Money:
#     __slots__ = '_money',
#
#     def __init__(self, value):
#         self._money = value
#
#
# class MoneyR(Money):
#     pass
#
# m = MoneyR(10)
# m.s = 100

# class Money:
#     # __slots__ = '_money',
#
#     def __init__(self, value):
#         self._money = value
#
#
# class MoneyR(Money):
#     __slots__ = '_value', '_money'
#
# m = MoneyR(10)
# m._money = 100
# m._value = 20

# 4
# Объявите класс Person, в объектах которого
# разрешены только локальные атрибуты с именами
# (ограничение задается через коллекцию __slots__):
#
# _fio - ФИО сотрудника (строка);
# _old - возраст сотрудника (целое положительное число);
# _job - занимаемая должность (строка).
#
# Сами объекты должны создаваться командой:
#
# p = Person(fio, old, job)
#
# Создайте несколько следующих объектов
# этого класса с информацией:
#
# Суворов, 52, полководец
# Рахманинов, 50, пианист, композитор
# Балакирев, 34, программист и преподаватель
# Пушкин, 32, поэт и писатель
#
# Сохраните все эти объекты в виде списка с именем persons.
#
# P.S. В программе следует объявить только
# класс и создать список. На экран выводить
# ничего не нужно.

# class Person:
#     __slots__ = ('_fio', '_old', '_job')
#
#     def __init__(self, fio, old, job):
#         self._fio = fio
#         self._old = old
#         self._job = job
#
# # Создание объектов класса Person
# persons = [
#     Person('Суворов', 52, 'полководец'),
#     Person('Рахманинов', 50, 'пианист, композитор'),
#     Person('Балакирев', 34, 'программист и преподаватель'),
#     Person('Пушкин', 32, 'поэт и писатель')
# ]

# 5
# Объявите класс Planet (планета),
# объекты которого создаются командой:
#
# p = Planet(name, diametr, period_solar, period)
#
# где
# name - наименование планеты;
# diametr - диаметр планеты (любое положительное число);
# period_solar - период (время) обращения планеты
#   вокруг Солнца (любое положительное число);
# period - период обращения планеты вокруг своей оси
#   (любое положительное число).
#
# В каждом объекте класса Planet должны
# формироваться локальные атрибуты с именами:
# _name, _diametr, _period_solar, _period
# и соответствующими значениями
#
# Затем, объявите класс с именем SolarSystem (солнечная система). В объектах этого класса должны быть допустимы, следующие локальные атрибуты (ограничение задается через коллекцию __slots__):
#
# _mercury - ссылка на планету Меркурий (объект класса Planet);
# _venus - ссылка на планету Венера (объект класса Planet);
# _earth - ссылка на планету Земля (объект класса Planet);
# _mars - ссылка на планету Марс (объект класса Planet);
# _jupiter - ссылка на планету Юпитер (объект класса Planet);
# _saturn - ссылка на планету Сатурн (объект класса Planet);
# _uranus - ссылка на планету Уран (объект класса Planet);
# _neptune - ссылка на планету Нептун (объект класса Planet).
#
# Объект класса SolarSystem должен создаваться командой:
#
# s_system = SolarSystem()
#
# и быть только один (одновременно в программе
# два и более объектов класса SolarSystem недопустимо).
# Используйте для этого паттерн Singleton.
#
# В момент создания объекта SolarSystem
# должны автоматически создаваться перечисленные
# локальные атрибуты и ссылаться на
# соответствующие объекты класса Planet
# со следующими данными по планетам
#
# self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
# self._venus =   Planet('Венера',  12104, 224.7, 5832.45)
# self._earth =   Planet('Земля',   12756, 365.3, 23.93)
# self._mars =    Planet('Марс',     6794,   687, 24.62)
# self._jupiter = Planet('Юпитер', 142800,  4330,  9.9)
# self._saturn =  Planet('Сатурн', 120660, 10753, 10.63)
# self._uranus =  Planet('Уран',    51118, 30665, 17.2)
# self._neptune = Planet('Нептун',  49528, 60150, 16.1)
#
# Создайте в программе объект s_system класса SolarSystem.
#
# P.S. В программе следует объявить
# только классы и создать объект s_system.
# На экран выводить ничего не нужно.

# class Planet:
#     def __init__(self, name, diametr, period_solar, period):
#         self._name = name
#         self._diametr = diametr
#         self._period_solar = period_solar
#         self._period = period
#
#
# class SolarSystem:
#     _instance = None
#     __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')
#
#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super(SolarSystem, cls).__new__(cls)
#             cls._instance._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
#             cls._instance._venus = Planet('Венера', 12104, 224.7, 5832.45)
#             cls._instance._earth = Planet('Земля', 12756, 365.3, 23.93)
#             cls._instance._mars = Planet('Марс', 6794, 687, 24.62)
#             cls._instance._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
#             cls._instance._saturn = Planet('Сатурн', 120660, 10753, 10.63)
#             cls._instance._uranus = Planet('Уран', 51118, 30665, 17.2)
#             cls._instance._neptune = Planet('Нептун', 49528, 60150, 16.1)
#         return cls._instance
#
#
# # Создание объекта s_system класса SolarSystem
# s_system = SolarSystem()

# 6
# Объявите класс с именем Star (звезда),
# в объектах которого разрешены только
# локальные атрибуты с именами (ограничение
# задается через коллекцию __slots__):
#
# _name - название звезды (строка);
# _massa - масса звезды (любое положительное число);
#          часто измеряется в массах Солнца;
# _temp - температура поверхности звезды в Кельвинах
#         (любое положительное число).
#
# Объекты этого класса должны создаваться командой:
#
# star = Star(name, massa, temp)
#
# На основе класса Star объявите следующие дочерние классы:
#
# WhiteDwarf - белый карлик;
# YellowDwarf - желтый карлик;
# RedGiant - красный гигант;
# Pulsar - пульсар.
#
# В каждом объекте этих классов должны
# быть разрешены (дополнительно к атрибутам
# базового класса Star) только следующие
# локальные атрибуты:
#
# _type_star - название типа звезды (строка);
# _radius - радиус звезды (любое положительное число);
#           часто измеряется в радиусах Солнца.
#
# Соответственно, объекты этих классов должны
# создаваться командой:
#
# star = Имя_дочернего_класса(name, massa, temp, type_star, radius)
#
# Создайте в программе следующие объекты звезд:
#
# RedGiant: Альдебаран; 5; 3600; красный гигант; 45
# WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
# WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
# YellowDwarf: Солнце; 1; 6000; желтый карлик; 1
#
# Все эти объекты сохраните в виде
# списка stars. Затем, с помощью функций
# isinstance() и filter() сформируйте новый
# список с именем white_dwarfs, состоящий
# только из белых карликов (WhiteDwarf).
#
# P.S. В программе следует объявить
# только классы и создать списки.
# На экран выводить ничего не нужно.

# class Star:
#     __slots__ = ('_name', '_massa', '_temp')
#
#     def __init__(self, name, massa, temp):
#         self._name = name
#         self._massa = massa
#         self._temp = temp
#
#
# class WhiteDwarf(Star):
#     __slots__ = ('_type_star', '_radius')
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class YellowDwarf(Star):
#     __slots__ = ('_type_star', '_radius')
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class RedGiant(Star):
#     __slots__ = ('_type_star', '_radius')
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class Pulsar(Star):
#     __slots__ = ('_type_star', '_radius')
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# # Создание объектов звезд
# stars = [
#     RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
#     WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
#     WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
#     YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)
# ]
#
# # Фильтрация белых карликов
# white_dwarfs = list(filter(lambda star: isinstance(star, WhiteDwarf), stars))

# 7
# Объявите класс Note (нота), объекты
# которого создаются командой:
#
# note = Note(name, ton)
#
# где
# name - название ноты (допустимые значения:
#   до, ре, ми, фа, соль, ля, си);
# ton - тональность ноты (целое число).
# Тональность (ton) принимает следующие целые значения:
#
# -1 - бемоль (flat);
# 0 - обычная нота (normal);
# 1 - диез (sharp).
#
# Если в названии (name) или тональности
# (ton) передаются недопустимые значения,
# то генерируется исключение командой:
#
# raise ValueError('недопустимое значение аргумента')
#
# В каждом объекте класса Note должны
# формироваться локальные атрибуты с именами
# _name и _ton с соответствующими значениями.
#
# Объявите класс с именем Notes,
# в объектах которого разрешены только
# локальные атрибуты с именами
# (ограничение задается через коллекцию __slots__):
#
# _do - ссылка на ноту до (объект класса Note);
# _re - ссылка на ноту ре (объект класса Note);
# _mi - ссылка на ноту ми (объект класса Note);
# _fa - ссылка на ноту фа (объект класса Note);
# _solt - ссылка на ноту соль (объект класса Note);
# _la - ссылка на ноту ля (объект класса Note);
# _si - ссылка на ноту си (объект класса Note).
#
# Объект класса Notes должен создаваться командой:
#
# notes = Notes()
#
# и быть только один (одновременно в
# программе два и более объектов класса
# Notes недопустимо). Используйте для
# этого паттерн Singleton.
#
# В момент создания объекта Notes должны
# автоматически создаваться перечисленные
# локальные атрибуты и ссылаться на
# соответствующие объекты класса Note
# (тональность (ton) у всех нот изначально равна 0).
#
# Обеспечить возможность обращения к
# нотам по индексам:
# 0 - до; 1 - ре; ... ; 6 - си. Например:
#
# nota = notes[2]  # ссылка на ноту ми
# notes[3]._ton = -1 # изменение тональности ноты фа
#
# Если указывается недопустимый
# индекс (не целое число, или число,
# выходящее за интервал [0; 6]),
# то генерируется исключение командой:
#
# raise IndexError('недопустимый индекс')
#
# Создайте в программе объект notes класса Notes.
#
# P.S. В программе следует объявить
# только классы и создать объект notes.
# На экран выводить ничего не нужно.
# class Note:
#     _available_values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
#
#     def __init__(self, name, ton):
#         self._name = name
#         self._ton = ton
#
#     def __setattr__(self, key, value):
#         if key == "_name" and value not in self._available_values:
#             raise ValueError('недопустимое значение аргумента')
#         if key == "_ton" and value not in (-1, 0, 1):
#             raise ValueError('недопустимое значение аргумента')
#         object.__setattr__(self, key, value)
#
#
# class Notes:
#     __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
#     _available_values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __del__(self):
#         Notes._instance = None
#
#     def __init__(self):
#         for k, v in zip(self.__slots__, self._available_values):
#             setattr(self, k, Note(v, 0))
#
#     def __getitem__(self, item):
#         if not (0 <= item < 7):
#             raise IndexError('недопустимый индекс')
#         return getattr(self, self.__slots__[item])
# notes = Notes()

# 8
# В программе объявлен базовый класс
# Function (функция) следующим образом:
#
# class Function:
#     def __init__(self):
#         self._amplitude = 1.0     # амплитуда функции
#         self._bias = 0.0          # смещение функции по оси Oy
#
#     def __call__(self, x, *args, **kwargs):
#         return self._amplitude * self._get_function(x) + self._bias
#
#     def _get_function(self, x):
#         raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')
#
#     def __add__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError('смещение должно быть числом')
#
#         obj = self.__class__(self)
#         obj._bias = self._bias + other
#         return obj
#
# Здесь в инициализаторе создаются два локальных атрибута:
#
# _amplitude - амплитуда функции;
# _bias - смещение функции по оси ординат (Oy).
#
# Далее, в методе __call__() берется значение
# функции в точке x через метод _get_function(),
# который должен быть определен в дочерних
# классах, умножается на амплитуду функции и
# добавляется ее смещение. Следующий метод
# __add__() позволяет менять смещение функции,
# изменяя атрибут _bias на указанное значение other.
#
# Обратите внимание, в методе __add__()
# происходит создание нового объекта командой:
#
# obj = self.__class__(self)
#
# Здесь __class__ - это ссылка на класс,
# к которому относится объект self.
# Благодаря этому в базовом классе можно
# создавать объекты соответствующих дочерних
# классов. В момент создания объекта ему
# передается параметр self как аргумент.
# Так будет создаваться копия объекта,
# т.е. новый объект с тем же набором и
# значениями локальных атрибутов.
#
# Чтобы обеспечить этот функционал, объявите
# дочерний класс с именем Linear
# (линейная функция y = k*x + b), объекты
# которого должны создаваться командами:
#
# obj = Linear(k, b)
# linear = Linear(obj)  # этот вариант используется
#                       # в базовом классе в методе __add__()
#
# В первом случае происходит создание объекта
# линейной функции с параметрами k и b.
# Во втором - создание объекта со значениями
# параметров k и b, взятыми из объекта obj.
#
# В каждом объекте класса Linear должны
# создаваться локальные атрибуты с именами
# _k и _b с соответствующими значениями.
# В результате будет создан универсальный
# базовый класс Function для работы с
# произвольными функциями от одного аргумента.
#
# Применять эти классы можно следующим образом
# (эти строчки в программе писать не нужно):
#
# f = Linear(1, 0.5)
# f2 = f + 10   # изменение смещения (атрибут _bias)
# y1 = f(0)     # 0.5
# y2 = f2(0)    # 10.5
#
# Пропишите в базовом классе Function еще
# один магический метод для изменения
# масштаба (амплитуды) функции, чтобы
# был доступен оператор умножения:
#
# f = Linear(1, 0.5)
# f2 = f * 5    # изменение амплитуды (атрибут _amplitude)
# y1 = f(0)     # 0.5
# y2 = f2(0)    # 2.5
#
# P.S. В программе следует объявить только
# классы. На экран выводить ничего не нужно.

# class Function:
#     def __init__(self):
#         self._amplitude = 1.0     # амплитуда функции
#         self._bias = 0.0          # смещение функции по оси Oy
#
#     def __call__(self, x, *args, **kwargs):
#         return self._amplitude * self._get_function(x) + self._bias
#
#     def _get_function(self, x):
#         raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')
#
#     def __add__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError('смещение должно быть числом')
#
#         obj = self.__class__(self)
#         obj._bias = self._bias + other
#         return obj
#
#     # здесь добавляйте еще один магический метод для умножения
#     def __mul__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError('амплитуда должна быть числом')
#
#         obj = self.__class__(self)
#         obj._amplitude = self._amplitude * other
#         return obj
#
#
# # здесь объявляйте класс Linear
# class Linear(Function):
#     def __init__(self, k=None, b=None):
#         super().__init__()
#         if type(k) == Linear:
#             self._k, self._b = k._k, k._b
#         else:
#             self._k = k
#             self._b = b
#
#     def _get_function(self, x):
#         return self._k * x + self._b

# class Shop:
#     ID_SHOP_ITEM = 0
#
#
# sp = Shop()
# sp.ID_SHOP_ITEM += 1
# print(Shop.ID_SHOP_ITEM)
# print(sp.__dict__)

# Бремя наследия
# Необходимо написать универсальную основу
# для представления ненаправленных связных
# графов и поиска в них кратчайших маршрутов.
# Далее, этот алгоритм предполагается применять
# для прокладки маршрутов: на картах,
# в метро и так далее.
#
# Для универсального описания графов,
# вам требуется объявить в программе
# следующие классы:
#
# Vertex - для представления вершин графа
#          (на карте это могут быть: здания,
#          остановки, достопримечательности и т.п.);
# Link - для описания связи между двумя
#        произвольными вершинами графа (на карте:
#        маршруты, время в пути и т.п.);
# LinkedGraph - для представления связного
#               графа в целом (карта целиком).
#
# Объекты класса Vertex должны создаваться командой:
#
# v = Vertex()
#
# и содержать локальный атрибут:
#
# _links - список связей с другими вершинами
# графа (список объектов класса Link).
#
# Также в этом классе должно быть
# объект-свойство (property):
#
# links - для получения ссылки на список _links.
#
# Объекты следующего класса Link должны
# создаваться командой:
#
# link = Link(v1, v2)
#
# где
# v1, v2 - объекты класса Vertex (вершины графа).
# Внутри каждого объекта класса Link должны
# формироваться следующие локальные атрибуты:
#
# _v1, _v2 - ссылки на объекты класса Vertex,
#            которые соединяются данной связью;
# _dist - длина связи (по умолчанию 1);
#         это может быть длина пути,
#         время в пути и др.
#
# В классе Link должны быть объявлены
# следующие объекты-свойства:
#
# v1 - для получения ссылки на вершину v1;
# v2 - для получения ссылки на вершину v2;
# dist - для изменения и считывания значения атрибута _dist.
#
# Наконец, объекты третьего класса
# LinkedGraph должны создаваться командой:
#
# map_graph = LinkedGraph()
#
# В каждом объекте класса LinkedGraph должны
# формироваться локальные атрибуты:
#
# _links - список из всех связей графа (из объектов класса Link);
# _vertex - список из всех вершин графа (из объектов класса Vertex).
#
# В самом классе LinkedGraph необходимо
# объявить (как минимум) следующие методы:
#
# def add_vertex(self, v): ... - для
#   добавления новой вершины v в список _vertex
#   (если она там отсутствует);
# def add_link(self, link): ... - для
#   добавления новой связи link в список _links
#   (если объект link с указанными вершинами в
#   списке отсутствует);
# def find_path(self, start_v, stop_v): ... -
#   для поиска кратчайшего маршрута из вершины
#   start_v в вершину stop_v.
#
# Метод find_path() должен возвращать список
# из вершин кратчайшего маршрута и список
# из связей этого же маршрута в виде кортежа:
#
# ([вершины кратчайшего пути], [связи между вершинами])
#
# Поиск кратчайшего маршрута допустимо делать
# полным перебором с помощью рекурсивной функции
# (будем полагать, что общее число вершин в
# графе не превышает 100). Для тех, кто желает
# испытать себя в полной мере, можно реализовать
# алгоритм Дейкстры поиска кратчайшего пути
# в связном взвешенном графе.
#
# В методе add_link() при добавлении новой связи
# следует автоматически добавлять вершины этой
# связи в список _vertex, если они там отсутствуют.
#
# Проверку наличия связи в списке _links следует
# определять по вершинам этой связи. Например,
# если в списке имеется объект:
#
# _links = [Link(v1, v2)]
#
# то добавлять в него новые объекты Link(v2, v1)
# или Link(v1, v2) нельзя (обратите внимание
# у всех трех объектов будут разные id,
# т.е. по id определять вхождение в список нельзя).
#
# Подсказка: проверку на наличие существующей
# связи можно выполнить с использованием
# функции filter() и указанием нужного
# условия для отбора объектов.
#
# Пример использования классов, применительно
# к схеме метро (эти строчки в программе
# писать не нужно):
#
# map_graph = LinkedGraph()
#
# v1 = Vertex()
# v2 = Vertex()
# v3 = Vertex()
# v4 = Vertex()
# v5 = Vertex()
# v6 = Vertex()
# v7 = Vertex()
#
# map_graph.add_link(Link(v1, v2))
# map_graph.add_link(Link(v2, v3))
# map_graph.add_link(Link(v1, v3))
#
# map_graph.add_link(Link(v4, v5))
# map_graph.add_link(Link(v6, v7))
#
# map_graph.add_link(Link(v2, v7))
# map_graph.add_link(Link(v3, v4))
# map_graph.add_link(Link(v5, v6))
#
# print(len(map_graph._links))   # 8 связей
# print(len(map_graph._vertex))  # 7 вершин
# path = map_graph.find_path(v1, v6)
#
# Однако, в таком виде применять классы
# для схемы карты метро не очень удобно.
# Например, здесь нет указаний названий
# станций, а также длина каждого сегмента
# равна 1, что не соответствует действительности.
#
# Чтобы поправить этот момент и реализовать
# программу поиска кратчайшего пути в
# метро между двумя произвольными станциями,
# объявите еще два дочерних класса:
#
# class Station(Vertex): ... - для описания станций метро;
# class LinkMetro(Link): ... - для описания связей между станциями метро.
#
# Объекты класса Station должны создаваться командой:
#
# st = Station(name)
#
# где name - название станции (строка).
# В каждом объекте класса Station должен
# дополнительно формироваться локальный атрибут:
#
# name - название станции метро.
#
# (Не забудьте в инициализаторе дочернего
# класса вызывать инициализатор базового класса).
#
# В самом классе Station переопределите
# магические методы __str__() и __repr__(),
# чтобы они возвращали название станции
# метро (локальный атрибут name).
#
# Объекты второго класса LinkMetro должны
# создаваться командой:
#
# link = LinkMetro(v1, v2, dist)
#
# где
# v1, v2 - вершины (станции метро);
# dist - расстояние между станциями (любое положительное число).
#
# (Также не забывайте в инициализаторе
# этого дочернего класса вызывать
# инициализатор базового класса).
#
# В результате, эти классы должны
# совместно работать следующим образом
# (эти строчки в программе писать не нужно):
#
# map_metro = LinkedGraph()
# v1 = Station("Сретенский бульвар")
# v2 = Station("Тургеневская")
# v3 = Station("Чистые пруды")
# v4 = Station("Лубянка")
# v5 = Station("Кузнецкий мост")
# v6 = Station("Китай-город 1")
# v7 = Station("Китай-город 2")
#
# map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 1))
# map_metro.add_link(LinkMetro(v1, v3, 1))
#
# map_metro.add_link(LinkMetro(v4, v5, 1))
# map_metro.add_link(LinkMetro(v6, v7, 1))
#
# map_metro.add_link(LinkMetro(v2, v7, 5))
# map_metro.add_link(LinkMetro(v3, v4, 3))
# map_metro.add_link(LinkMetro(v5, v6, 3))
#
# print(len(map_metro._links))
# print(len(map_metro._vertex))
# path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
# print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# print(sum([x.dist for x in path[1]]))  # 7
#
# P.S. В программе нужно объявить
# только классы
# Vertex, Link, LinkedGraph, Station, LinkMetro.
# На экран ничего выводить не нужно.

class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links

class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        # составим кортеж из связей, которые уже есть
        t = tuple(filter(lambda x:
                         (id(x.v1)==id(link.v1) and id(x.v2)==id(link.v2)) or \
                         (id(x.v2)==id(link.v1) and id(x.v1)==id(link.v2)),
                         self._links
                         ))
        if len(t) == 0:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            # добавим связи к вершинам
            link.v1.links.append(link)
            link.v2.links.append(link)


    def find_path(self, start_v, stop_v, path=None):
        # воспользуемся рекурсивной ф-ей
        self._start_v = start_v
        self._stop_v = stop_v
        return self._next(self._start_v, None, [], [])

    def _dist_path(self, links):
        return sum([x.dist for x in links if x  is not None])


    def _next(self, current, link_prev, current_path, current_links):
        '''
        Рекурсивная функция поиска кратчайшего пути

        :param current:         текущая вершина - объект класса Vertex
        :param link_prev:       предыдущая связь - объект класса Link
        :param current_path:    список вершин Vertex
        :param current_links:   список связей Link
        :return: best_path, best_links - списки вершин и связей
        '''

        current_path.append(current)
        if link_prev:
            current_links.append(link_prev)

        if current == self._stop_v:
            return current_path, current_links

        len_path = -1
        best_path = []
        best_links = []

        # Проход по всем связям в графе
        for link in self._links:
            # рекурсивно проходим по всей связанной цепочке, до _stop_v
            # остановка поиска на _stop_v гарантирована проверкой выше:
            # if current == self._stop_v: return current_path, current_links
            # рекурсия:
            # если одна вершина связи является
            # последней (current) на пути,
            # а другая - еще не внесена в путь,
            # то последней точкой станет не внесенная
            # и "проваливаемся" в саму себя- в _next (по рекурсии)
            if link.v1 == current and link.v2 not in current_path:
                path, links = self._next(link.v2, link, current_path[:], current_links[:])
            elif link.v2 == current and link.v1 not in current_path:
                path, links = self._next(link.v1, link, current_path[:], current_links[:])
            # иначе дошли до разрыва цеочки
            # т.е. обе вершины связи - не связаны с
            # построеным путем path
            else:
                # выходим из рекурсии
                continue

            # если конечная точка попала в путь
            # и длина полученного по рекурсии
            # пути меньше, чем ранее полученная длина
            # Обновляем лучший путь и длину
            if self._stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]
            # print('path:',path)
            # print('len_path:',len_path)

            # если конечная точка не попала в построенный путь,
            # это значит, что вся цепочка которая началась
            # с первого link в цикле for, и была построена по рекурсии
            # на этой итерации цикла - отбрасывается
            # и мы переходим к другой связи link
            # (к другой итерации цикла for)
            # т.е. на каждой итерации цикла мы строим всю
            # возможную цепочку связей

        return best_path, best_links

class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name

class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist

map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
