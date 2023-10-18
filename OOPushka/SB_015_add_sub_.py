# class Way:
#     def __init__(self, length):
#         self.length = length
#
#     def __add__(self, other):
#         return Way(self.length + other.length)
#
# w1 = Way(5)
# w2 = Way(10)
#
# w = 15 + w2
#
# метод __iadd__() используется для оператора += (пример: w1 += w2) и не может быть использован для оператора + (пример: w1 + w2)
# метод __add__() используется для оператора += (пример: w1 += w2), если отсутствует метод __iadd__()
# метод __radd__() используется для реализации оператора +, относительно правого операнда (объекта класса Way); пример: w = 10 + w1
# метод __add__() служит для реализации бинарного оператора сложения (пример: w1 + w2)

# 4
# Известно, что в Python мы можем соединять
# два списка между собой с помощью оператора +:
#
# lst = [1, 2, 3] + [4.5, -3.6, 0.78]
#
# Но нет реализации оператора -, который бы
# убирал из списка соответствующие значения
# вычитаемого списка, как это показано в примере:
#
# lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1]
#   # [2, 3, 4] (порядок следования оставшихся
#   элементов списка должен сохраняться)
#
# Давайте это поправим и создадим такой
# функционал. Для этого нужно объявить
# класс с именем NewList, объекты которого
# создаются командами:
#
# lst = NewList() # пустой список
# lst = NewList([-1, 0, 7.56, True])
#   # список с начальными значениями
#
# Реализуйте для этого класса работу
# с оператором вычитания, чтобы над
# объектами класса NewList можно было
# выполнять следующие действия:
#
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
#
# Также в классе NewList необходимо объявить метод:
#
# get_list() - для возвращения результирующего
# списка объекта класса NewList
#
# Например:
#
# lst = res_2.get_list() # [1, 2, 3]
#
# P.S. В программе требуется только объявить класс.
# На экран ничего выводить не нужно.

# class NewList:
#     '''
#     При использовании изменяемых объектов,
#     таких как списки или словари, в качестве
#     значений по умолчанию для аргументов
#     функции возникает потенциальный нежелательный
#     побочный эффект. Это происходит потому,
#     что объект, используемый по умолчанию,
#     сохраняется между вызовами функции.
#     Если изменения делаются в этом объекте
#     в ходе выполнения функции, они остаются
#     после ее завершения.
#     Поэтому - лучше использовать None
#     '''
#
#     def __init__(self, lst: list = None):
#         self._lst = lst[:] if lst and type(lst) == list else []
#
#     def get_list(self):
#         return self._lst
#
#     def __sub__(self, other):
#         if type(other) not in (list, NewList):
#             raise ArithmeticError('Правый операнд должен иметь тип list или NewList')
#
#         other_list = other if type(other) == list else other.get_list()
#         return NewList(self.__diff_list(self._lst, other_list))
#
#     def __rsub__(self, other):
#         if type(other) != list:
#             raise ArithmeticError('Правый операнд должен иметь тип list')
#         return NewList(self.__diff_list(other, self._lst))
#
#     # операцию -= не переопределяем, поскольку операции list1-list2 достаточно
#
#     @staticmethod
#     def __diff_list(lst_subtrahend, lst_minuend):
#         '''
#         "уменьшаемое" - subtrahend
#         "вычитаемое" - minuend
#         "разность" - difference
#         '''
#         if len(lst_minuend) == 0:
#             return lst_subtrahend
#
#         lst_minuend_temp = lst_minuend[:]
#         return [
#             x for x in lst_subtrahend \
#             if not NewList.__contains_element(x, lst_minuend_temp)
#         ]
#
#     @staticmethod
#     def __contains_element(element, lst_checked: list):
#         res = any(map(lambda xx: \
#                       type(element) == type(xx) and element == xx, \
#                       lst_checked))
#         # type(element) == type(xx) - надо для сравнения True и 1
#         if res:
#             # вычитаем 1-й совпавший элемент
#             lst_checked.remove(element)
#         return res

# 5
# Объявите класс с именем ListMath,
# объекты которого можно создавать командами:
#
# lst1 = ListMath() # пустой список
# lst2 = ListMath([1, 2, -5, 7.68])
#   # список с начальными значениями
#
# В качестве значений элементов списка
# объекты класса ListMath должны отбирать
# только целые и вещественные числа,
# остальные игнорировать (если указываются
# в списке). Например:
#
# lst = ListMath([1, "abc", -5, 7.68, True])
#   # ListMath: [1, -5, 7.68]
#
# В каждом объекте класса ListMath должен
# быть публичный атрибут:
#
# lst_math - ссылка на текущий список объекта
# (для каждого объекта создается свой список).
#
# Также с объектами класса ListMath должны
# работать следующие операторы:
#
# lst = lst + 76  # сложение каждого числа
#                 # списка с определенным числом
# lst = 6.5 + lst # сложение каждого числа
#                 # списка с определенным числом
# lst += 76.7     # сложение каждого числа
#                 # списка с определенным числом
# lst = lst - 76  # вычитание из каждого числа
#                 # списка определенного числа
# lst = 7.0 - lst # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5 # умножение каждого числа списка на
#               # указанное число (в данном случае на 5)
# lst = 5 * lst # умножение каждого числа списка на
#               # указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13 # деление каждого числа списка
#                # на указанное число
#                # (в данном случае на 13)
# lst = 3 / lst  # деление числа на каждый элемент списка
# lst /= 13.0
#
# При использовании бинарных операторов
# +, -, *, / должны формироваться новые
# объекты класса ListMath с новыми списками,
# прежние списки не меняются.
#
# При использовании операторов +=, -=, *=, /=
# значения должны меняться внутри списка
# текущего объекта (новый объект не создается).
#
# P.S. В программе достаточно только объявить класс.
# На экран ничего выводить не нужно.

# class ListMath:
#     def __init__(self, lst: list = None):
#         self.lst_math = lst if lst and type(lst) == list else []
#         self.lst_math = list(filter(lambda x: \
#                                     type(x) in (int, float), \
#                                     self.lst_math))
#
#     @staticmethod
#     def __verify_value(value):
#         if type(value) not in (int, float):
#             raise ArithmeticError('Операнд должен быть числом')
#
#
#     def __add__(self, other):
#         self.__verify_value(other)
#         return ListMath([x + other for x in self.lst_math])
#
#     def __radd__(self, other):
#         # перейдем на __add__
#         return self + other
#
#     def __sub__(self, other):
#         self.__verify_value(other)
#         return ListMath([x - other for x in self.lst_math])
#
#     def __rsub__(self, other):
#         return ListMath([other - x for x in self.lst_math])
#
#     def __mul__(self, other):
#         self.__verify_value(other)
#         return ListMath([x * other for x in self.lst_math])
#
#     def __rmul__(self, other):
#         return self * other
#
#     def __truediv__(self, other):
#         self.__verify_value(other)
#         if other == 0:
#             raise ArithmeticError('Деление на ноль запрещено')
#         return ListMath([x / other for x in self.lst_math])
#
#     def __rtruediv__(self, other):
#         res = any(map(lambda x: \
#                       x == 0, \
#                       self.lst_math))
#         if res:
#             raise ArithmeticError('В списке делителей присутствует ноль')
#         return ListMath([other / x for x in self.lst_math])
#
#     def __iadd__(self, other):
#         self.__verify_value(other)
#         self.lst_math = [x + other for x in self.lst_math]
#         return self
#
#     def __isub__(self, other):
#         self.__verify_value(other)
#         self.lst_math = [x - other for x in self.lst_math]
#         return self
#
#     def __imul__(self, other):
#         self.__verify_value(other)
#         self.lst_math = [x * other for x in self.lst_math]
#         return self
#
#     def __itruediv__(self, other):
#         self.__verify_value(other)
#         if other == 0:
#             raise ArithmeticError('Деление на ноль запрещено')
#         self.lst_math = [x / other for x in self.lst_math]
#         return self

# 6
# Ранее, в одном из подвигов мы с вами
# создавали односвязный список с объектами
# класса StackObj (когда один объект
# ссылается на следующий и так далее):
# ... pic ...
#
# Давайте снова создадим такую структуру
# данных. Для этого объявим два класса:
#
# Stack - для управления односвязным
#         списком в целом;
# StackObj - для представления
#            отдельных объектов в
#            односвязным списком.
#
# Объекты класса StackObj должны
# создаваться командой:
#
# obj = StackObj(data)
#
# где data - строка с некоторыми данными.
#
# Каждый объект класса StackObj должен
# иметь локальные приватные атрибуты:
#
# __data - ссылка на строку с
#       переданными данными;
# __next - ссылка на следующий объект
#       односвязного списка (если следующего
#       нет, то __next = None).
#
# Объекты класса Stack создаются командой:
#
# st = Stack()
#
# и каждый из них должен содержать
# локальный атрибут:
#
# top - ссылка на первый объект
# односвязного списка (если объектов
# нет, то top = None).
#
# Также в классе Stack следует
# объявить следующие методы:
#
# push_back(self, obj) - добавление
#   объекта класса StackObj в конец
#   односвязного списка;
# pop_back(self) - удаление последнего
#   объекта из односвязного списка.
#
# Дополнительно нужно реализовать следующий
# функционал (в этих операциях копии
# односвязного списка создавать не нужно):
#
# # добавление нового объекта класса
# # StackObj в конец односвязного списка st
# st = st + obj
# st += obj
#
# # добавление нескольких объектов
# в конец односвязного списка
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']
#
# В последних двух строчках должны
# автоматически создаваться N объектов
# класса StackObj с данными, взятыми из
# списка (каждый элемент списка для
# очередного добавляемого объекта).
#
# P.S. В программе достаточно только
# объявить классы. На экран ничего
# выводить не нужно.

# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def data(self):
#         return self.__data
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
#
# class Stack:
#     def __init__(self):
#         self.__top = None
#
#     @property
#     def top(self):
#         return self.__top
#
#     def push_back(self, obj):
#         if not self.__top:
#             self.__top = obj
#         else:
#             current = self.__top
#             while current.next:
#                 current = current.next
#             current.next = obj
#
#     def pop_back(self):
#         if not self.__top:
#             return
#         elif not self.__top.next:
#             self.__top = None
#         else:
#             current = self.__top
#             while current.next.next:
#                 current = current.next
#             current.next = None
#
#     def __add__(self, obj):
#         self.push_back(obj)
#         return self
#
#     def __iadd__(self, obj):
#         self.push_back(obj)
#         return self
#
#     def __mul__(self, data_list):
#         for data in data_list:
#             self.push_back(StackObj(data))
#         return self
#
#     def __imul__(self, data_list):
#         for data in data_list:
#             self.push_back(StackObj(data))
#         return self

# 7
# Вам поручается создать программу по
# учету книг (библиотеку). Для этого
# необходимо в программе объявить два класса:
#
# Lib - для представления библиотеки в целом;
# Book - для описания отдельной книги.
#
# Объекты класса Book должны создаваться командой:
#
# book = Book(title, author, year)
#
# где
# title - заголовок книги (строка);
# author - автор книги (строка);
# year - год издания (целое число).
#
# Объекты класса Lib создаются командой:
#
# lib = Lib()
#
# Каждый объект должен содержать локальный публичный атрибут:
#
# book_list - ссылка на список из книг
# (объектов класса Book). Изначально список пустой.
#
# Также объекты класса Lib должны
# работать со следующими операторами:
#
# lib = lib + book # добавление новой книги в библиотеку
# lib += book
#
# lib = lib - book # удаление книги book из
#                  # библиотеки (удаление происходит
#                  # по ранее созданному объекту
#                  # book класса Book)
# lib -= book
#
# lib = lib - indx # удаление книги по ее
#                  # порядковому номеру (индексу:
#                  # отсчет начинается с нуля)
# lib -= indx
#
# При реализации бинарных операторов + и -
# создавать копии библиотек (объекты класса
# Lib) не нужно.
#
# Также с объектами класса Lib должна
# работать функция:
#
# n = len(lib) # n - число книг
#
# которая возвращает число книг в библиотеке.
#
# P.S. В программе достаточно только
# объявить классы. На экран ничего выводить не нужно.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


# class Lib:
#     def __init__(self):
#         self.book_list = []
#
#     def __add__(self, book):
#         self.book_list.append(book)
#         return self
#
#     def __iadd__(self, book):
#         self.book_list.append(book)
#         return self
#
#     def __sub__(self, item):
#         if isinstance(item, Book):
#             self.book_list = [b for b in self.book_list if b != item]
#         elif isinstance(item, int) and 0 <= item < len(self.book_list):
#             del self.book_list[item]
#         return self
#
#     def __isub__(self, item):
#         if isinstance(item, Book):
#             self.book_list = [b for b in self.book_list if b != item]
#         elif isinstance(item, int) and 0 <= item < len(self.book_list):
#             del self.book_list[item]
#         return self
#
#     def __len__(self):
#         return len(self.book_list)

# 8
# Вам необходимо создать простую программу
# по учету семейного бюджета. Для этого в
# программе объявите два класса с именами:
#
# Budget - для управления семейным бюджетом;
# Item - пункт расходов бюджета.
#
# Объекты класса Item должны создаваться командой:
#
# it = Item(name, money)
#
# где
# name - название статьи расхода;
# money - сумма расходов (вещественное или целое число).
#
# Соответственно, в каждом объекте класса
# Item должны формироваться локальные
# атрибуты name и money с переданными
# значениями. Также с объектами класса Item
# должны выполняться следующие операторы:
#
# s = it1 + it2 # сумма для двух статей расходов
#
# и в общем случае:
#
# s = it1 + it2 + ... + itN # сумма N статей расходов
#
# При суммировании оператор + должен возвращать
# число - вычисленную сумму по атрибутам
# money соответствующих объектов класса Item.
#
# Объекты класса Budget создаются командой:
#
# my_budget = Budget()
#
# А сам класс Budget должен иметь
# следующие методы:
#
# add_item(self, it) - добавление статьи
#   расхода в бюджет (it - объект класса Item);
# remove_item(self, indx) - удаление статьи
#   расхода из бюджета по его порядковому
#   номеру indx (индексу: отсчитывается с нуля);
# get_items(self) - возвращает список всех
#   статей расходов (список из объектов класса Item).
#
# Пример использования классов
# (эти строчки в программе писать не нужно):
#
# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
#
# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x
#
# P.S. В программе требуется только
# объявить класс. На экран
# ничего выводить не нужно.

# в функции __radd__ other это self.money
# с add и следующий объект будет
# Item.money(self.money) и тогда
# всё ровно будет.

# class Budget:
#     lst_it = []
#
#     def add_item(self, it):
#         self.lst_it.append(it.money)
#
#     def remove_item(self, indx):
#         del self.lst_it[indx]
#
#     def get_items(self):
#         return self.lst_it
#
#
# class Item:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
#     def __add__(self, other):
#         if not isinstance(other, Item) and not isinstance(other.money, (int, float)):
#             raise AttributeError("Неправильный тип данных")
#         self.money += other.money
#         return self.money
#
#     def __radd__(self, other):
#         return other + self.money

# 9
# Объявите класс Box3D для представления
# прямоугольного параллелепипеда (бруска),
# объекты которого создаются командой:
#
# box = Box3D(width, height, depth)
#
# где width, height, depth - ширина,
# высота и глубина соответственно
# (числа: целые или вещественные)
#
# В каждом объекте класса Box3D должны
# создаваться публичные атрибуты:
#
# width, height, depth - ширина,
# высота и глубина соответственно.
#
# С объектами класса Box3D должны
# выполняться следующие операторы:
#
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
#
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
#
# При каждой арифметической операции
# следует создавать новый объект класса
# Box3D с соответствующими значениями
# локальных атрибутов.
#
# P.S. В программе достаточно только
# объявить класс Box3D.
# На экран ничего выводить не нужно.

# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)
#
#     def __mul__(self, factor):
#         return Box3D(self.width * factor, self.height * factor, self.depth * factor)
#
#     def __rmul__(self, factor):
#         return self * factor
#
#     def __sub__(self, other):
#         return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)
#
#     def __floordiv__(self, divisor):
#         return Box3D(self.width // divisor, self.height // divisor, self.depth // divisor)
#
#     def __mod__(self, mod):
#         return Box3D(self.width % mod, self.height % mod, self.depth % mod)
#
# 10
# В нейронных сетях использую операцию
# под названием Max Pooling. Суть ее
# состоит в сканировании прямоугольной
# таблицы чисел (матрицы) окном определенного
# размера (обычно, 2x2 элемента) и выбора
# наибольшего значения в пределах этого окна:
# Или, если окна выходят за пределы матрицы,
# то они пропускаются (игнорируются):
# Мы повторим эту процедуру. Для этого
# в программе нужно объявить класс с именем
# MaxPooling, объекты которого создаются командой:
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
#
# где step - шаг смещения окна по горизонтали
# и вертикали; size - размер окна по
# горизонтали и вертикали.
#
# Параметры step и size по умолчанию должны
# принимать кортеж со значениями (2, 2).
#
# Для выполнения операции Max Pooling
# используется команда:
#
# res = mp(matrix)
#
# где
# matrix - прямоугольная таблица чисел;
# res - ссылка на результат обработки
#   таблицы matrix (должна создаваться
#   новая таблица чисел.
#
# Прямоугольную таблицу чисел следует
# описывать вложенными списками.
# Если при сканировании таблицы часть
# окна выходит за ее пределы, то эти
# данные отбрасывать (не учитывать
# все окно).
#
# Если matrix не является прямоугольной
# таблицей или содержит хотя бы одно
# не числовое значение, то должно
# генерироваться исключение командой:
#
# raise ValueError("Неверный формат для первого параметра matrix.")
#
# Пример использования класса
# (эти строчки в программе писать не нужно):
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
#
# Результатом будет таблица чисел:
#
# 6 8
# 9 7
#
# P.S. В программе достаточно объявить
# только класс. Выводить на экран ничего не нужно.
# variant 1
# class MaxPooling:
#     def __init__(self, step=(2, 2), size=(2, 2)):
#         # Инициализация класса с заданными параметрами
#         # step (шаг) и size (размер окна)
#         self.step = step
#         self.size = size
#
#     def __is_numeric_matrix(self, matrix):
#         # Проверка, является ли матрица числовой и прямоугольной
#         if not all(isinstance(row, list) for row in matrix):
#             return False
#         if not all(len(row) == len(matrix[0]) for row in matrix):
#             return False
#         if not all(isinstance(item, (int, float)) for row in matrix for item in row):
#             return False
#         return True
#
#     def __get_window(self, matrix, x, y):
#         # Получение окна размера self.size с началом в координатах x, y
#         window = []
#         for i in range(self.size[0]):
#             if x + i >= len(matrix):  # Проверка, чтобы окно не выходило за пределы матрицы по вертикали
#                 return None
#             row = []
#             for j in range(self.size[1]):
#                 if y + j >= len(matrix[0]):  # Проверка, чтобы окно не выходило за пределы матрицы по горизонтали
#                     return None
#                 row.append(matrix[x + i][y + j])
#             window.append(row)
#         return window
#
#     def __max_pooling(self, matrix):
#         # Процедура выполнения операции Max Pooling на матрице
#         result = []
#         for i in range(0, len(matrix), self.step[0]):  # Цикл с шагом self.step[0] по вертикали
#             row = []
#             for j in range(0, len(matrix[0]), self.step[1]):  # Цикл с шагом self.step[1] по горизонтали
#                 window = self.__get_window(matrix, i, j)  # Получение окна с координатами i, j
#                 if window is not None:  # Проверка, что окно не выходит за пределы матрицы
#                     row.append(max(map(max, window)))  # Добавление максимального значения окна в результирующую строку
#             if row:
#                 result.append(row)  # Добавление строки в результирующую матрицу, если она не пустая
#         return result
#
#     def __call__(self, matrix):
#         # Вызов операции Max Pooling на матрице,
#         # проверка на числовую и прямоугольную матрицу
#         if not self.__is_numeric_matrix(matrix):
#             raise ValueError("Неверный формат для первого параметра matrix.")
#         return self.__max_pooling(matrix)
#
# variant 2
class MaxPooling:
    def __init__(self, step=(2,2), size=(2,2)):
        self.__step = step
        self.__size = size

    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows >0 else 0
        if rows == 0:
            return [[]]
        # проверка матрицы
        if not all(map(
            lambda x: len(x) == cols,
            matrix
        )) or \
           not all(map(
               lambda row: all(map(
                   lambda x: type(x) in (int, float),
                   row
               )),
               matrix
           )):
            raise ValueError("Неверный формат для первого параметра matrix.")
        h, w = self.__size[0], self.__size[1]
        sh, sw = self.__step[0], self.__step[1]

        # посчитаем количество окон, которое будет
        # при сканировании матрицы по строкам и по столбцам
        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        # выходная матрица изначально - нулевая
        res = [[0]*cols_range for _ in range(rows_range)]
        for i in range(rows_range):
            for j in range(cols_range):
                # опираясь на i,j спозиционируем
                # окно на матрице, потом выберем
                # все элементы в пределах этого окна
                # и найдем среди них максимальное значение
                # matrix[i*sh: i*sh+h] - строки в пределах окна
                # создадим генератор
                s = (x for r in matrix[i*sh: i*sh+h] \
                     for x in r[j*sw:j*sw+w])
                res[i][j] = max(s)

        return res

mp = MaxPooling(step=(2, 2), size=(2, 2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])  # [[6, 8], [9, 7]]
print(res)


