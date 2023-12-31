# 4
# Объявите в программе класс Car, в
# котором реализуйте объект-свойство
# с именем model для записи и считывания
# информации о модели автомобиля из
# локальной приватной переменной __model.
#
# Объект-свойство объявите с помощью
# декоратора @property. Также в
# объекте-свойстве model должны
# быть реализованы проверки:
#
# - модель автомобиля - это строка;
# - длина строки модели должна быть
# в диапазоне [2; 100].
#
# Если проверка не проходит, то
# локальное свойство __model
# остается без изменений.
#
# Объекты класса Car предполагается
# создавать командой:
#
# car = Car()
#
# и далее работа с объектом-свойством,
# например:
#
# car.model = "Toyota"
#
# P.S. В программе объявить только класс.
# На экран ничего выводить не нужно.

# class Car:
#     def __init__(self):
#         self.__model = 'Car'
#
#     @property
#     def model(self):
#         return self.__model
#
#     @staticmethod
#     def data_is_valid(string):
#         if type(string) != str:
#             return False
#         if not 2 <= len(string) <= 100:
#             return False
#         return True
#
#     @model.setter
#     def model(self, name):
#         if self.data_is_valid(name):
#             self.__model = name

# 5
# Объявите в программе класс WindowDlg,
# объекты которого предполагается
# создавать командой:
#
# wnd = WindowDlg(заголовок окна,
# ширина, высота)
#
# В каждом объекте класса WindowDlg
# должны создаваться приватные
# локальные атрибуты:
#
# __title - заголовок окна (строка);
# __width, __height - ширина и
#   высота окна (числа).
#
# В классе WindowDlg необходимо
# реализовать метод:
#
# show() - для отображения окна на
# экране (выводит в консоль строку
# в формате:
# "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").
#
# Также в классе WindowDlg необходимо
# реализовать два объекта-свойства:
#
# width - для изменения и считывания
#         ширины окна;
# height - для изменения и считывания
#          высоты окна.
#
# При изменении размеров окна необходимо
# выполнять проверку:
#
# - переданное значение является целым
# числом в диапазоне [0; 10000].
#
# Если хотя бы один размер изменился
# (высота или ширина), то следует выполнить
# автоматическую перерисовку окна
# (вызвать метод show()). При начальной
# инициализации размеров width, height
# вызывать метод show() не нужно.
#
# P.S. В программе нужно объявить только
# класс с требуемой функциональностью.

# class WindowDlg:
#
#     def __init__(self, title, width, height):
#         self.__title = title
#         self.__width =width
#         self.__height = height
#
#     def show(self):
#         print(f"{self.__title}: {self.width}, {self.height}")
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         value_before = self.__width
#         if self.size_is_valid(w):
#             self.__width = w
#             if value_before != w:
#                 self.show()
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         value_before = self.__height
#         if self.size_is_valid(h):
#             self.__height = h
#             if value_before != h:
#                 self.show()
#
#     @staticmethod
#     def size_is_valid(size):
#         if type(size) != int:
#             return False
#         if not 0 <= size <= 10_000:
#             return False
#         return True

# 6
# Реализуйте односвязный список (не список
# Python, не использовать список Python
# для хранения объектов), когда один объект
# ссылается на следующий и так по цепочке
# до последнего:
# Для этого объявите в программе два класса:
#
# StackObj - для описания объектов
#   односвязного списка;
# Stack - для управления односвязным
#   списком.
#
# Объекты класса StackObj предполагается
# создавать командой:
#
# obj = StackObj(данные)
#
# Здесь данные - это строка с некоторым
# содержимым. Каждый объект класса StackObj
# должен иметь следующие локальные
# приватные атрибуты:
#
# __data - ссылка на строку с данными,
#   указанными при создании объекта;
# __next - ссылка на следующий объект
# класса StackObj (при создании объекта
#   принимает значение None).
#
# Также в классе StackObj должны быть
# объявлены объекты-свойства:
#
# next - для записи и считывания
#   информации из локального приватного
#   свойства __next;
# data - для записи и считывания
#   информации из локального
#   приватного свойства __data.
#
# При записи необходимо реализовать
# проверку, что __next будет ссылаться
# на объект класса StackObj или значение
# None. Если проверка не проходит,
# то __next остается без изменений.
#
# Класс Stack предполагается использовать
# следующим образом:
#
# st = Stack() # создание объекта односвязного списка
#
# В объектах класса Stack должен быть
# локальный публичный атрибут:
#
# top - ссылка на первый добавленный объект
# односвязного списка (если список
# пуст, то top = None).
#
# А в самом классе Stack следующие методы:
#
# push(self, obj) - добавление объекта
#   класса StackObj в конец
#   односвязного списка;
# pop(self) - извлечение последнего
#   объекта с его удалением из
#   односвязного списка;
# get_data(self) - получение списка
#   из объектов односвязного списка
#   (список из строк локального
#   атрибута __data каждого объекта
#   в порядке их добавления, или
#   пустой список, если объектов нет).
#
# Пример использования классов Stack
# и StackObj (эти строчки в программе
# писать не нужно):
#
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
#
# P.S. В программе требуется объявить
# только классы. На экран ничего выводить не нужно.

# class StackObj:
#
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, obj):
#         if isinstance(obj, StackObj) or obj is None:
#             self.__next = obj
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         self.__data = value
#
#
# class Stack:
#
#     def __init__(self):
#         self.top = None
#         self.last = None
#         self.prelast = None
#
#     def push(self, obj):
#         # Проверка, что объект - класса и,
#         # что он еще не в списке
#         if isinstance(obj, StackObj):
#             if obj.next:
#                 print(f'Невозможно добавить объект {obj}, который уже есть в связном списке')
#             else:
#                 # добавим первый объект
#                 if self.top is None:
#                     self.top = obj
#                     self.last = obj
#                 # если 1-й объект уже есть
#                 else:
#                     # установим в последнем объекте
#                     # ссылку на добавляемый
#                     self.last.next = obj
#                     # последним объектом теперь будет
#                     # добавляемый
#                     self.last = obj
#
#     def pop(self):
#         if self.top:
#             result = self.last
#             if not self.top.next:
#                 self.top, self.last = None, None
#                 return result
#             else:
#                 slider = self.top
#                 while slider.next:
#                     self.prelast = slider
#                     slider = slider.next
#                 self.prelast.next = None
#                 self.last = self.prelast
#                 return result
#
#     def get_data(self):
#         result = []
#         if self.top:
#             last = self.top
#             result.append(last.data)
#             while last.next:
#                 last = last.next
#                 result.append(last.data)
#         return result
#
# st = Stack()
# obj1 = StackObj("obj1")
# st.push(obj1)
# obj2 = StackObj("obj2")
# st.push(obj2)
# obj3 = StackObj("obj3")
# st.push(obj3)
# st.push(obj1)
#
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
# print(res)

# 7
# Объявите класс RadiusVector2D, объекты
# которого должны создаваться командами:
#
# v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
# v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
# v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
#
# В каждом объекте класса RadiusVector2D
# должны формироваться локальные приватные атрибуты:
#
# __x, __y - координаты конца вектора
# (изначально значения равны 0, если не
# передано какое-либо другое).
#
# В классе RadiusVector2D необходимо
# объявить два объекта-свойства:
#
# x - для изменения и считывания локального атрибута __x;
# y - для изменения и считывания локального атрибута __y.
#
# При инициализации и изменении локальных
# атрибутов, необходимо проверять
# корректность передаваемых значений:
#
# - значение должно быть числом (целым
# или вещественным) в диапазоне
# [MIN_COORD; MAX_COORD].
#
# Если проверка не проходит, то координаты
# не меняются (напомню, что при инициализации
# они изначально равны 0). Величины
# MIN_COORD = -100, MAX_COORD = 1024
# задаются как публичные атрибуты
# класса RadiusVector2D.
#
# Также в классе RadiusVector2D необходимо
# объявить статический метод:
#
# norm2(vector) - для вычисления
# квадратической нормы vector - переданного
# объекта класса RadiusVector2D
# (квадратическая норма вектора: x*x + y*y).
#
# P.S. В программе требуется объявить только класс.
# На экран ничего выводить не нужно.

# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024
#
#     def __init__(self, x = 0, y = 0):
#         self.__x = self.__y = 0
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def __coord_is_valid(cls, val):
#         if type(val) not in (int, float):
#             # print(f'Значение {val} не число')
#             return False
#         if not (cls.MIN_COORD <= val <= cls.MAX_COORD):
#             # print(f'Значение {val} не в диапазоне')
#             return False
#         return True
#
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x_val):
#         if self.__coord_is_valid(x_val):
#             if self.x != x_val:
#                 self.__x = x_val
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y_val):
#         if self.__coord_is_valid(y_val):
#             if self.y != y_val:
#                 self.__y = y_val
#
#
#     @staticmethod
#     def norm2(vector):
#         if not isinstance(vector, RadiusVector2D):
#             print(f"Аргумент {vector} не объект класса RadiusVector2D")
#             result = None
#         else:
#             result = vector.x*vector.x + vector.y*vector.y
#         return result
#
# r1 = RadiusVector2D()
# print(r1.x, r1.y)
# r2 = RadiusVector2D(1)
# print(r2.x, r2.y)
# r3 = RadiusVector2D(4, 5)
# print((r3.x, r3.y))
# r5 = RadiusVector2D(-102, 2000)
# assert r5.x == 0 and r5.y == 0, "присвоение значений, выходящих за диапазон [-100; 1024] не должно выполняться"

# 8
# Требуется реализовать программу по
# работе с решающими деревьями:
# /\-=|_ рисунок ...
# Здесь в каждом узле дерева делается
# проверка (задается вопрос). Если
# проверка проходит, то осуществляется
# переход к следующему объекту по левой
# стрелке (с единицей), а иначе - по
# правой стрелке (с нулем). И так до
# тех пор, пока не дойдем до одного из
# листа дерева (вершины без потомков).
#
# В качестве входных данных используется
# вектор (список) с бинарными значениями:
# 1 - да, 0 - нет. Каждый элемент этого
# списка соответствует своему вопросу
# (своей вершине дерева), например:
#
# Далее, этот вектор применяется к
# решающему дереву, следующим образом.
# Корневая вершина "Любит Python" с
# ней связан первый элемент вектора
# x и содержит значение 1, следовательно,
# мы переходим по левой ветви.
# Попадаем в вершину "Понимает ООП".
# С ней связан второй элемент вектора
# x со значением 0, следовательно,
# мы переходим по правой ветви и
# попадаем в вершину "будет кодером".
# Так как эта вершина конечная (листовая),
# то получаем результат в виде строки
# "будет кодером". По аналогии выполняется
# обработка вектора x с другими наборами
# значений 0 и 1.
#
# Для реализации решающих деревьев в
# программе следует объявить два класса:
#
# TreeObj - для описания вершин и листьев
# решающего дерева;
# DecisionTree - для работы с решающим
# деревом в целом.
#
# В классе DecisionTree должны быть
# реализованы (по крайне мере) два
# метода уровня класса (@classmethod):
#
# def predict(cls, root, x) - для
#       построения прогноза (прохода
#       по решающему дереву) для вектора
#       x из корневого узла дерева root.
# def add_obj(cls, obj, node=None, left=True) -
#       для добавления вершин в решающее
#       дерево (метод должен возвращать
#       добавленную вершину - объект
#       класса TreeObj);
#
# В методе add_obj параметры имеют,
# следующие значения:
#
# obj - ссылка на новый (добавляемый)
#       объект решающего дерева
#       (объект класса TreeObj);
# node - ссылка на объект дерева,
#        к которому присоединяется
#        вершина obj;
# left - флаг, определяющий ветвь
#        дерева (объекта node), к
#        которой присоединяется объект
#        obj (True - к левой ветви;
#        False - к правой).
#
# В классе TreeObj следует объявить
# инициализатор:
#
# def __init__(self, indx, value=None): ...
#
# где indx - проверяемый в вершине
#            дерева индекс вектора x;
# value - значение, хранящееся в вершине
#         (принимает значение None для
#         вершин, у которых есть потомки -
#         промежуточных вершин).
#
# При этом, в каждом создаваемом объекте
# класса TreeObj должны автоматически
# появляться следующие локальные атрибуты:
#
# indx - проверяемый индекс (целое число);
# value - значение с данными (строка);
# __left - ссылка на следующий объект
#          дерева по левой ветви
#          (изначально None);
# __right - ссылка на следующий объект
#           дерева по правой ветви
#           (изначально None).
#
# Для работы с локальными приватными
# атрибутами __left и __right необходимо
# объявить объекты-свойства с именами
# left и right.
#
# Эти классы в дальнейшем предполагается
# использовать следующим образом
# (эти строчки в программе не писать):
#
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
# x = [1, 1, 0]
# res = DecisionTree.predict(root, x) # будет программистом
#
# P.S. В программе требуется объявить
# только классы.
# На экран ничего выводить не нужно.

# class TreeObj:
#
#     def __init__(self, indx, value=None):
#         self.indx = indx
#         self.value = value
#         self.left = self.right = None
#
#     @property
#     def left(self):
#         return self.__left
#
#     @left.setter
#     def left(self, node):
#         self.__left = node
#
#     @property
#     def right(self):
#         return self.__right
#
#     @right.setter
#     def right(self, node):
#         self.__right = node
#
# class DecisionTree:
#
#     @classmethod
#     # obj - добавляемый объект класса TreeObj
#     # node - узел к которому добавляем
#     def add_obj(cls, obj, node=None, left=True):
#         if node:
#             if left: node.left  = obj
#             else:    node.right = obj
#         return obj
#
#     @classmethod
#     def predict(cls, root, x):
#         obj = root
#         while obj:
#             obj_next = cls.get_next(obj, x)
#             if obj_next is None: break
#             obj = obj_next
#
#         return obj.value
#
#     @classmethod
#     def get_next(cls, obj, x):
#         if x[obj.indx] == 1:
#             return  obj.left
#         return obj.right

# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
# x = [1, 1, 0]
# res = DecisionTree.predict(root, x)
# print(res)

# 9
# Вам требуется сформировать класс
# PathLines для описания маршрутов,
# состоящих из линейных сегментов.
# При этом каждый линейный сегмент
# предполагается задавать отдельным
# классом LineTo. Объекты этого
# класса будут формироваться командой:
#
# line = LineTo(x, y)
#
# где x, y - следующая координата
# линейного участка (начало маршрута
# из точки 0, 0).
#
# В каждом объекте класса LineTo
# должны формироваться локальные
# атрибуты:
#
# x, y - для хранения координат
# конца линии (начало определяется
# по координатам предыдущего объекта).
#
# Объекты класса PathLines должны
# создаваться командами:
#
# p = PathLines()                   # начало маршрута из точки 0, 0
# p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
#
# где line1, line2, ... - объекты класса LineTo.
#
# Сам же класс PathLines должен
# иметь следующие методы:
#
# get_path() - возвращает список
#       из объектов класса LineTo
#       (если объектов нет,то
#       пустой список);
# get_length() - возвращает суммарную
#       длину пути (сумма длин всех
#       линейных сегментов);
# add_line(self, line) - добавление
#       нового линейного сегмента
#       (объекта класса LineTo)
#       в конец маршрута.
#
# Пояснение: суммарный маршрут -
# это сумма длин всех линейных сегментов,
# а длина каждого линейного сегмента
# определяется как евклидовое расстояние
# по формуле:
#
# L = sqrt((x1-x0)^2 + (y1-y0)^2)
#
# где x0, y0 - предыдущая точка маршрута;
# x1, y1 - текущая точка маршрута.
#
# Пример использования классов
# (эти строчки в программе писать не нужно):
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
#
# P.S. В программе требуется объявить
# только классы. На экран ничего выводить не нужно.

# class LineTo:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class PathLines:
#     def __init__(self, *args):
#         # ******************* tuple_1 **** + tuple_2
#         self.coords = list((LineTo(0,0),)+args)
#
#     def get_path(self):
#         # все созданные объекты кроме нуля
#         return self.coords[1:]
#
#     def get_length(self):
#         # формируем генератор g который будет
#         # возвращать координаты точек с двух
#         # сторон итеририруемого отрезка в пути
#         # в виде кортежа из двух точек (точки-
#         # элементы списка self.coords, которые
#         # суть объекты LineTo)
#         g = ((self.coords[i-1],self.coords[i])
#              for i in range(1,len(self.coords)))
#         return sum(map(lambda t:
#             (((t[0].x-t[1].x)**2 + (t[0].y-t[1].y)**2))**0.5
#             , g))
#
#     def add_line(self, line):
#         self.coords.append(line)

# 10
# Вы создаете телефонную записную книжку.
# Она определяется классом PhoneBook.
# Объекты этого класса создаются командой:
#
# p = PhoneBook()
#
# А сам класс должен иметь следующий
# набор методов:
#
# add_phone(phone) - добавление нового
#   номера телефона (в список);
# remove_phone(indx) - удаление номера
#   телефона по индексу списка;
# get_phone_list() - получение списка из
#   объектов всех телефонных номеров.
#
# Каждый номер телефона должен быть
# представлен классом PhoneNumber.
# Объекты этого класса должны
# создаваться командой:
#
# note = PhoneNumber(number, fio)
#
# где number - номер телефона (число)
# в формате XXXXXXXXXXX (одиннадцати цифр,
# X - цифра); fio - Ф.И.О. владельца
# номера (строка).
#
# В каждом объекте класса PhoneNumber
# должны формироваться локальные атрибуты:
#
# number - номер телефона (число);
# fio - ФИО владельца номера телефона.
#
# Необходимо объявить два класса PhoneBook
# и PhoneNumber в соответствии с заданием.
#
# Пример использования классов (эти строчки
# в программе писать не нужно):
#
# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
# p.add_phone(PhoneNumber(21345678901, "Панда"))
# phones = p.get_phone_list()
#
# P.S. В программе требуется объявить только классы.
# На экран ничего выводить не нужно.

# class PhoneNumber:
#     def __init__(self, number, fio):
#         self.number = number
#         self.fio = fio
#
# class PhoneBook:
#     def __init__(self):
#         self.phones = []
#
#     def add_phone(self, phone):
#         self.phones.append(phone)
#
#     def remove_phone(self, indx):
#         self.phones.pop(indx)
#
#     def get_phone_list(self):
#         return  self.phones
