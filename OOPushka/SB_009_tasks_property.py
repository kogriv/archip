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

