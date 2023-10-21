# from collections.abc import Iterable
#
# my_list = [1, 2, 3, 4, 5]
#
# # Проверка, является ли объект итерируемым
# if hasattr(my_list, '__iter__'):
#     print("Этот объект итерируемый")
#
# if isinstance(my_list, Iterable):
#     print("Этот объект является эземпляром Iterable")

# r = range(1, 3000)
# res1 = 2022 in r   # res1 = True
# res2 = 2022 in r   # res2 = True
# print(res1)
# print(res2)
#
# r = iter(range(1, 3000))
# res1 = 2022 in r   # res1 = True
# res2 = 2023 in r   # res1 = False
# print(res1)
# print(res2)
#
# '''
# В первом варианте объект range в операторе
# in каждый раз возвращает новый итератор и перебор
# последовательности начинается с начала.
# Во втором варианте явно указывается итератор,
# который в строчке res2 = 2022 in r продолжает перебор
# последовательности с числа 2023.
# '''

# class GeomRange:
#     def __init__(self, start, step, stop):
#         self.start = start
#         self.step = step
#         self.stop = stop
#         self.__value = self.start
#
#     def __next__(self):
#         if self.__value < self.stop:
#             ret_value = self.__value
#             self.__value *= self.step
#             return ret_value
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         self.__value = self.start
#         return self
#
# g = GeomRange(1, 1.2, 2)
# for x in g: print(x)
# for x in g: print(x)
# res = next(g)
# res = next(g)
# it = iter(g); res = next(g)

# 5
# Объявите в программе класс Person, объекты
# которого создаются командой:
#
# p = Person(fio, job, old, salary, year_job)
#
# где
# fio - ФИО сотрудника (строка);
# job - наименование должности (строка);
# old - возраст (целое число);
# salary - зарплата (число: целое или вещественное);
# year_job - непрерывный стаж на указанном месте
# работы (целое число).
#
# В каждом объекте класса Person автоматически
# должны создаваться локальные атрибуты с такими же именами:
# fio, job, old, salary, year_job и соответствующими
# значениями.
#
# Также с объектами класса Person должны поддерживаться
# следующие команды:
#
# data = p[indx] # получение данных по порядковому
#   номеру (indx) атрибута (порядок: fio, job, old,
#   salary, year_job и начинается с нуля)
# p[indx] = value # запись в поле с указанным индексом
#   (indx) нового значения value
# for v in p: # перебор всех атрибутов объекта в
#   порядке: fio, job, old, salary, year_job
#     print(v)
#
# При работе с индексами, проверить корректность
# значения indx. Оно должно быть целым числом в
# диапазоне [0; 4]. Иначе, генерировать исключение
# командой:
#
# raise IndexError('неверный индекс')
#
# Пример использования класса (эти строчки в
# программе не писать):
#
# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError
#
# P.S. В программе нужно объявить только
# класс. Выводить на экран ничего не нужно.

# class Person:
#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
#
#     def __getitem__(self, indx):
#         if indx not in range(5):
#             raise IndexError('неверный индекс')
#         if indx == 0:
#             return self.fio
#         elif indx == 1:
#             return self.job
#         elif indx == 2:
#             return self.old
#         elif indx == 3:
#             return self.salary
#         elif indx == 4:
#             return self.year_job
#
#     def __setitem__(self, indx, value):
#         if indx not in range(5):
#             raise IndexError('неверный индекс')
#         if indx == 0:
#             self.fio = value
#         elif indx == 1:
#             self.job = value
#         elif indx == 2:
#             self.old = value
#         elif indx == 3:
#             self.salary = value
#         elif indx == 4:
#             self.year_job = value
#
#     def __iter__(self):
#         self.iter_count = 0
#         return self
#
#     def __next__(self):
#         if self.iter_count == 0:
#             self.iter_count += 1
#             return self.fio
#         elif self.iter_count == 1:
#             self.iter_count += 1
#             return self.job
#         elif self.iter_count == 2:
#             self.iter_count += 1
#             return self.old
#         elif self.iter_count == 3:
#             self.iter_count += 1
#             return self.salary
#         elif self.iter_count == 4:
#             self.iter_count += 1
#             return self.year_job
#         else:
#             raise StopIteration

# 6
# Вам дают задание разработать итератор для
# последовательного перебора элементов вложенных
# (двумерных) списков следующей структуры:
#
# lst = [[x00],
#        [x10, x11],
#        [x20, x21, x22],
#        [x30, x31, x32, x33],
#        ...
#       ]
#
# Для этого необходимо в программе объявить класс
# с именем TriangleListIterator, объекты которого
# создаются командой:
#
# it = TriangleListIterator(lst)
#
# где lst - ссылка на перебираемый список.
#
# Затем, с объектами класса TriangleListIterator
# должны быть доступны следующие операции:
#
# for x in it:  # последовательный перебор всех
#               # элементов списка: x00, x10, x11, x20, ...
#     print(x)
#
# it_iter = iter(it)
# x = next(it_iter)
#
# Итератор должен перебирать элементы списка по
# указанной треугольной форме. Даже если итератору
# на вход будет передан прямоугольная таблица
# (вложенный список), то ее перебор все равно
# должен осуществляться по треугольнику.
# Если же это невозможно (из-за структуры списка),
# то естественным образом должна возникать ошибка
# IndexError: index out of range (выход индекса
# за допустимый диапазон).
#
# P.S. В программе нужно объявить только класс.
# Выводить на экран ничего не нужно.

# class TriangleListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.row = 0
#         self.col = 0
#
#     def __iter__(self):
#         self.row = 0
#         self.col = 0
#         return self
#
#     def __next__(self):
#         if self.row >= len(self.lst):
#             raise StopIteration
#         if self.col <= self.row:
#             current_value = self.lst[self.row][self.col]
#             if self.col == self.row:
#                 self.row += 1
#                 self.col = 0
#             else:
#                 self.col += 1
#             return current_value
#         else:
#             raise IndexError('index out of range')

# 7
# Теперь, вам необходимо разработать итератор,
# который бы перебирал указанные столбцы двумерного
# списка. Список представляет собой двумерную таблицу
# из данных:
#
# lst = [[x11, x12, ..., x1N],
#        [x21, x22, ..., x2N],
#        ...
#        [xM1, xM2, ..., xMN]
#       ]
#
# Для этого в программе необходимо объявить
# класс с именем IterColumn, объекты которого
# создаются командой:
#
# it = IterColumn(lst, column)
#
# где
# lst - ссылка на двумерный список;
# column - индекс перебираемого столбца
#   (отсчитывается от 0).
#
# Затем, с объектами класса IterColumn должны
# быть доступны следующие операции:
#
# it = IterColumn(lst, 1)
# for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
#     print(x)
#
# it_iter = iter(it)
# x = next(it_iter)
#
# P.S. В программе нужно объявить только
# класс итератора. Выводить на экран
# ничего не нужно.

# class IterColumn:
#     def __init__(self, lst, column):
#         self.lst = lst
#         self.column = column
#         self.current_row = 0
#
#     def __iter__(self):
#         self.current_row = 0
#         return self
#
#     def __next__(self):
#         if self.current_row < len(self.lst):
#             if self.column < len(self.lst[self.current_row]):
#                 current_value = self.lst[self.current_row][self.column]
#                 self.current_row += 1
#                 return current_value
#             else:
#                 raise IndexError('index out of range')
#         else:
#             raise StopIteration

# 8
# Вы несколько раз уже делали стек-подобную
# структуру, когда объекты последовательно
# связаны между собой
# ...pic...
# Доведем ее функционал до конца. Для этого,
# по прежнему, нужно объявить классы:
#
# Stack - для представления стека в целом;
# StackObj - для представления отдельных объектов стека.
#
# В классе Stack должны быть методы:
#
# push_back(obj) - для добавления нового объекта obj в конец стека;
# push_front(obj) - для добавления нового объекта obj в начало стека.
#
# В каждом объекте класса Stack должен быть публичный атрибут:
#
# top - ссылка на первый объект стека
# (при пустом стеке top = None).
#
# Объекты класса StackObj создаются командой:
#
# obj = StackObj(data)
#
# где data - данные, хранящиеся
# в объекте стека (строка).
#
# Также в каждом объекте класса StackObj
# должны быть публичные атрибуты:
#
# data - ссылка на данные объекта;
# next - ссылка на следующий объект стека (если его нет, то next = None).
#
# Наконец, с объектами класса Stack
# должны выполняться следующие команды:
#
# st = Stack()
#
# st[indx] = value # замена прежних данных
#                  # на новые по порядковому индексу
#                  (indx); отсчет начинается с нуля
# data = st[indx]  # получение данных из объекта стека по индексу
# n = len(st) # получение общего числа объектов стека
#
# for obj in st: # перебор объектов стека (с начала и до конца)
#     print(obj.data)  # отображение данных в консоль
#
# При работе с индексами (indx), нужно
# проверять их корректность. Должно
# быть целое число от 0 до N-1,
# где N - число объектов в стеке. Иначе,
# генерировать исключение командой:
#
# raise IndexError('неверный индекс')
#
# P.S. В программе нужно объявить
# только классы. Выводить на экран
# ничего не нужно.

# class StackObj:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.length = 0
#
#     def push_back(self, obj):
#         if self.top is None:
#             self.top = obj
#         else:
#             current = self.top
#             while current.next is not None:
#                 current = current.next
#             current.next = obj
#         self.length += 1
#
#     def push_front(self, obj):
#         obj.next = self.top
#         self.top = obj
#         self.length += 1
#
#     def __setitem__(self, indx, value):
#         if not (0 <= indx < self.length):
#             raise IndexError('неверный индекс')
#         current = self.top
#         for _ in range(indx):
#             current = current.next
#         current.data = value
#
#     def __getitem__(self, indx):
#         if not (0 <= indx < self.length):
#             raise IndexError('неверный индекс')
#         current = self.top
#         for _ in range(indx):
#             current = current.next
#         return current.data
#
#     def __len__(self):
#         return self.length
#
#     def __iter__(self):
#         self.current = self.top
#         return self
#
#     def __next__(self):
#         if self.current is None:
#             raise StopIteration
#         else:
#             temp = self.current
#             self.current = self.current.next
#             return temp

# 9
# В программе необходимо реализовать
# таблицу TableValues по следующей схеме
# ...pic...
# Каждая ячейка таблицы должна быть
# представлена классом Cell.
# Объекты этого класса создаются командой:
#
# cell = Cell(data)
#
# где data - данные в ячейке. В каждом
# объекте класса Cell должен формироваться
# локальный приватный атрибут __data с соответствующим
# значением. Для работы с ним в классе Cell
# должно быть объект-свойство (property):
#
# data - для записи и считывания информации
# из атрибута __data.
#
# Сам класс TableValues представляет
# таблицу в целом, объекты которого создаются командой:
#
# table = TableValues(rows, cols, type_data)
#
# где
# rows, cols - число строк и столбцов таблицы;
# type_data - тип данных ячейки (int - по умолчанию,
# float, list, str и т.п.). Начальные значения
# в ячейках таблицы равны 0 (целое число).
#
# С объектами класса TableValues должны
# выполняться следующие команды:
#
# table[row, col] = value# запись нового
# значения в ячейку с индексами row, col
# (индексы отсчитываются с нуля)
# value = table[row, col] # считывание значения из ячейки с индексами row, col
#
# for row in table:  # перебор по строкам
#     for value in row: # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()
#
# При попытке записать по индексам
# table[row, col] данные другого типа
# (не совпадающего с атрибутом type_data
# объекта класса TableValues), должно
# генерироваться исключение командой:
#
# raise TypeError('неверный тип присваиваемых данных')
#
# При работе с индексами row, col,
# необходимо проверять их корректность.
# Если индексы не целое число или они выходят
# за диапазон размера таблицы, то генерировать
# исключение командой:
#
# raise IndexError('неверный индекс')
#
# P.S. В программе нужно объявить
# только классы. Выводить на
# экран ничего не нужно.
# вариант 1
# class Cell:
#     def __init__(self, data = 0):
#         self.__row = self.__col = 0
#         self.data = data
#         self.row = 0
#         self.col = 0
#
#     @property
#     def data(self):
#         return self.__data
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#     @property
#     def row(self):
#         return self.__row
#     @row.setter
#     def row(self, row):
#         self.__row = row
#     @property
#     def col(self, col):
#         return self.__col
#     @col.setter
#     def col(self,col):
#         self.__col = col
#
# class RowOfCells:
#     def __init__(self, cols = 0, start=0, stop = 0, step = 1):
#         if type(start) != int or type(stop) !=int or type(step) != int:
#             raise IndexError('Значения начала, конца и шага должны быть целыми числами')
#         self.start = start
#         self.stop = stop if stop > 0 else cols
#         self.step = step
#         self.cols = cols
#         self.data_row = []
#         for col in range(cols):
#             self.data_row.append(Cell())
#             self.data_row[col].col = col
#
#     def __iter__(self):
#         self.col_counter = self.start - self.step
#         return self
#     def __next__(self):
#         self.col_counter += self.step
#         if self.col_counter < self.stop:
#             return self.data_row[self.col_counter]
#         else:
#             raise StopIteration
#
#     def __getitem__(self, item):
#         if type(item)!=int or not (0 <= item < self.cols):
#             raise IndexError('неверный индекс')
#         return self.data_row[item]
#     def __setitem__(self, key, value):
#         if type(key)!=int or not (0 <= col < self.cols):
#             raise IndexError('неверный индекс')
#         self.data_row[key] = value
#
#
# class TableValues:
#     def __init__(self, rows, cols, type_data = int):
#         self.rows = self.cols = 0
#         self.type_data = type_data
#         self.table = []
#         if type(rows) == int and rows>0 and type(cols) == int and cols >0:
#             self.rows = rows
#             self.cols = cols
#             for row in range(rows):
#                 self.table.append(RowOfCells(self.cols))
#                 for cell in self.table[row]:
#                     cell.row = row
#                     cell.data = 0
#
#     def __getitem__(self, index):
#         row, col = index
#         if not (0 <= row < self.rows) or not (0 <= col < self.cols):
#             raise IndexError('неверный индекс')
#         return self.table[row][col].data
#
#     def __setitem__(self, index, value):
#         row, col = index
#         if not (0 <= row < self.rows) or (0 <= col < self.cols):
#             raise IndexError('неверный индекс')
#         if type(value) != self.type_data:
#             raise TypeError('неверный тип присваиваемых данных')
#         self.table[row][col].data = value
#
#     def set_iter_attributes(self,
#         row_iter_start = 0, row_iter_stop = 0, row_iter_step = 1,
#         col_iter_start = 0, col_iter_stop = 0, col_iter_step = 1):
#         # print(
#         #     'self.row_iter_start',row_iter_start,'\n'
#         #     'self.row_iter_stop', row_iter_stop,'\n'
#         #     'self.row_iter_step', row_iter_step,'\n'
#         #     'self.col_iter_start',col_iter_start,'\n'
#         #     'self.col_iter_stop', col_iter_stop,'\n'
#         #     'self.col_iter_step', col_iter_step,
#         # )
#
#         if  type(row_iter_start) != int or row_iter_start >= self.rows or \
#             type(row_iter_stop)  != int or row_iter_stop < row_iter_start or \
#             type(row_iter_step)  != int or row_iter_step <= 0 or \
#             type(col_iter_start) != int or col_iter_start >= self.cols or \
#             type(col_iter_stop)  != int or col_iter_stop < col_iter_start or \
#             type(col_iter_step)  != int or col_iter_step <= 0:
#             raise IndexError('Что то не так с началом / концом / шагом итерирования')
#
#         self.row_iter_start = row_iter_start
#         self.row_iter_stop = row_iter_stop if row_iter_stop > 0 else self.rows
#         self.row_iter_step = row_iter_step
#         self.col_iter_start = col_iter_start
#         self.col_iter_stop = col_iter_stop if col_iter_stop > 0 else self.cols
#         self.col_iter_step = col_iter_step
#
#     def __iter__(self):
#         self.set_iter_attributes()
#         self.row_counter = self.row_iter_start - self.row_iter_step
#         return self
#
#     def __next__(self):
#         self.row_counter += self.row_iter_step
#         if self.row_counter < self.row_iter_stop:
#             return iter(self.table[self.row_counter])
#         raise StopIteration
#
#
# rows = 3
# cols = 4
# table = TableValues(rows,cols,int)
# for row in range(rows):
#     for col in range(cols):
#         print(table[row,col])
# for row in table:
#     for cell in row:
#         print(cell.data, end=' ')
#     print()
# вариант 2
# class Cell:
#     def __init__(self, data):
#         self.__data = data
#
#     @property
#     def data(self):
#         return self.__data
#
#
# class TableValues:
#     def __init__(self, rows, cols, type_data=int):
#         self.rows = rows
#         self.cols = cols
#         self.type_data = type_data
#         self.table = [[Cell(type_data()) for _ in range(cols)] for _ in range(rows)]
#
#     def __getitem__(self, index):
#         row, col = index
#         if not (0 <= row < self.rows and 0 <= col < self.cols):
#             raise IndexError('неверный индекс')
#         return self.table[row][col].data
#
#     def __setitem__(self, index, value):
#         row, col = index
#         if not (0 <= row < self.rows and 0 <= col < self.cols):
#             raise IndexError('неверный индекс')
#         if not isinstance(value, self.type_data):
#             raise TypeError('неверный тип присваиваемых данных')
#         self.table[row][col] = Cell(value)
#
#     def __iter__(self):
#         for row in self.table:
#             yield [cell.data for cell in row]

# 10
# Объявите класс Matrix (матрица) для
# операций с матрицами. Объекты этого
# класса должны создаваться командой
# m1 = Matrix(rows, cols, fill_value)
#
# где
# rows, cols - число строк и столбцов матрицы;
# fill_value - заполняемое начальное значение
#   элементов матрицы (должно быть число:
#   целое или вещественное). Если в качестве
#   аргументов передаются не числа,
#   то генерировать исключение:
#
# raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
#
# Также объекты можно создавать командой:
#
# m2 = Matrix(list2D)
#
# где
# list2D - двумерный список (прямоугольный),
#   состоящий из чисел (целых или вещественных).
#   Если список list2D не прямоугольный, или
#   хотя бы один из его элементов не число,
#   то генерировать исключение командой:
#
# raise TypeError('список должен быть прямоугольным, состоящим из чисел')
#
# Для объектов класса Matrix должны
# выполняться следующие команды:
#
# matrix = Matrix(4, 5, 0)
# res = matrix[0, 0] # возвращается первый элемент матрицы
# matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
#
# Если в результате присвоения тип
# данных не соответствует числу, то
# генерировать исключение командой:
#
# raise TypeError('значения матрицы должны быть числами')
#
# Если указываются недопустимые
# индексы матрицы (должны быть целыми
# числами от 0 и до размеров матрицы),
# то генерировать исключение:
#
# raise IndexError('недопустимые значения индексов')
#
# Также с объектами класса Matrix должны выполняться операторы:
#
# matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
# matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
# matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
# matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
#
# Во всех этих операция должна
# формироваться новая матрица с
# соответствующими значениями.
# Если размеры матриц не совпадают
# (разные хотя бы по одной оси), то
# генерировать исключение командой:
#
# raise ValueError('операции возможны только с матрицами равных размеров')
#
# Пример для понимания использования
# индексов (эти строчки в программе
# писать не нужно):
#
# mt = Matrix([[1, 2], [3, 4]])
# res = mt[0, 0] # 1
# res = mt[0, 1] # 2
# res = mt[1, 0] # 3
# res = mt[1, 1] # 4
#
# P.S. В программе нужно объявить
# только класс. Выводить на экран
# ничего не нужно.

# class Matrix:
#     def __init__(self, rows, cols=None, fill_value=None):
#         if cols is None and isinstance(rows, list):
#             self.check_list2D(rows)
#             self.matrix = rows
#         elif all(isinstance(i, int) for i in [rows, cols]):
#             if not isinstance(fill_value, (int, float)):
#                 raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
#             self.matrix = [[fill_value] * cols for _ in range(rows)]
#         else:
#             raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
#
#     def check_list2D(self, list2D):
#         if not all(isinstance(i, list) for i in list2D) or not all(all(isinstance(j, (int, float)) for j in i) for i in list2D):
#             raise TypeError('список должен быть прямоугольным, состоящим из чисел')
#         cols = len(list2D[0])
#         if not all(len(i) == cols for i in list2D):
#             raise TypeError('список должен быть прямоугольным, состоящим из чисел')
#         self.matrix = list2D
#
#     def __getitem__(self, indices):
#         row, col = indices
#         return self.matrix[row][col]
#
#     def __setitem__(self, indices, value):
#         row, col = indices
#         if not isinstance(value, (int, float)):
#             raise TypeError('значения матрицы должны быть числами')
#         self.matrix[row][col] = value
#
#     def __add__(self, other):
#         if isinstance(other, Matrix):
#             if len(self.matrix) != len(other.matrix) or any(len(self.matrix[i]) != len(other.matrix[i]) for i in range(len(self.matrix))):
#                 raise ValueError('операции возможны только с матрицами равных размеров')
#             result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
#         elif isinstance(other, (int, float)):
#             result = [[self.matrix[i][j] + other for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
#         else:
#             raise TypeError('операция невозможна')
#         return Matrix(result)
#
#     def __sub__(self, other):
#         if isinstance(other, Matrix):
#             if len(self.matrix) != len(other.matrix) or any(len(self.matrix[i]) != len(other.matrix[i]) for i in range(len(self.matrix))):
#                 raise ValueError('операции возможны только с матрицами равных размеров')
#             result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
#         elif isinstance(other, (int, float)):
#             result = [[self.matrix[i][j] - other for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
#         else:
#             raise TypeError('операция невозможна')
#         return Matrix(result)
#
#     def __repr__(self):
#         return f'Matrix({self.matrix})'
#
# list2D = [[1, 2], [3, 4], [5, 6, 7]]
# try:
#     st = Matrix(list2D)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"
#
# list2D = [[1, []], [3, 4], [5, 6]]
# try:
#     st = Matrix(list2D)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"
#
# try:
#     st = Matrix('1', 2, 0)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"
#
# list2D = [[1, 2], [3, 4], [5, 6]]
# matrix = Matrix(list2D)
# assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"
#
# matrix = Matrix(4, 5, 10)
# assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"
#
# try:
#     v = matrix[3, -1]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
# try:
#     v = matrix['0', 4]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
# matrix[0, 0] = 7
# assert matrix[0, 0] == 7, "неверно отработал __setitem__"
#
# try:
#     matrix[0, 0] = 'a'
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError в __setitem__"
#
# m1 = Matrix([[1, 2], [3, 4]])
# m2 = Matrix([[1, 1], [1, 1], [1, 1]])
#
# try:
#     matrix = m1 + m2
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"
#
# m1 = Matrix([[1, 2], [3, 4]])
# m2 = Matrix([[1, 1], [1, 1]])
# matrix = m1 + m2
# assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
# assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
# assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
#        and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"
#
# m1 = Matrix(2, 2, 1)
# id_m1_old = id(m1)
# m2 = Matrix(2, 2, 1)
# m1 = m1 + m2
# id_m1_new = id(m1)
# assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"
#
# matrix = Matrix(2, 2, 0)
# m = matrix + 10
# assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
# assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"
#
# m1 = Matrix(2, 2, 1)
# m2 = Matrix([[0, 1], [1, 0]])
# identity_matrix = m1 - m2  # должна получиться единичная матрица
# assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
#        and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
# assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"
#
# matrix = Matrix(2, 2, 1)
# m = matrix - 1
# assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
# assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
# ************************************
# ************************************
# ************************************
# ИСПЫТАНИЕ МАГИЕЙ
# Вы прошли магические методы. Начальство
# оценило вашу стойкость, рвение и решило
# дать вам испытание для подтверждения
# уровня полученных навыков. Вам выпала
# великая честь создать полноценную программу
# игры в "Крестики-нолики". И вот перед
# вами текст с заданием самого испытания.
# Техническое задание
#
# Необходимо объявить класс с именем
# TicTacToe (крестики-нолики) для
# управления игровым процессом. Объекты
# этого класса будут создаваться командой:
#
# game = TicTacToe()
#
# В каждом объекте этого класса должен
# быть публичный атрибут:
#
# pole - двумерный кортеж, размером 3x3.
#
# Каждый элемент кортежа pole является
# объектом класса Cell:
#
# cell = Cell()
#
# В объектах этого класса должно
# автоматически формироваться
# локальное свойство:
#
# value - текущее значение в ячейке:
#   0 - клетка свободна;
#   1 - стоит крестик;
#   2- стоит нолик.
#
# Также с объектами класса Cell
# должна выполняться функция:
#
# bool(cell) - возвращает True,
#   если клетка свободна (value = 0) и
#   False - в противном случае.
#
# К каждой клетке игрового поля
# должен быть доступ через операторы:
#
# res = game[i, j] # получение значения
#                  # из клетки с индексами i, j
# game[i, j] = value # запись нового значения
#                    # в клетку с индексами i, j
#
# Если индексы указаны неверно (не целые
# числа или числа, выходящие за диапазон
# [0; 2]), то следует генерировать
# исключение командой:
#
# raise IndexError('некорректно указанные индексы')
#
# Чтобы в программе не оперировать величинами:
# 0 - свободная клетка;
# 1 - крестики и 2 - нолики,
# в классе TicTacToe должны быть три
# публичных атрибута (атрибуты класса):
#
# FREE_CELL = 0      # свободная клетка
# HUMAN_X = 1        # крестик (игрок - человек)
# COMPUTER_O = 2     # нолик (игрок - компьютер)
#
# В самом классе TicTacToe должны быть
# объявлены следующие методы (как минимум):
#
# init() - инициализация игры (очистка
#          игрового поля, возможно, еще
#          какие-либо действия);
# show() - отображение текущего состояния
#          игрового поля (как именно - на
#          свое усмотрение);
# human_go() - реализация хода игрока
#              (запрашивает координаты свободной
#              клетки и ставит туда крестик);
# computer_go() - реализация хода компьютера
#                 (ставит случайным образом нолик
#                 в свободную клетку).
#
# Также в классе TicTacToe должны быть
# следующие объекты-свойства (property):
#
# is_human_win - возвращает True, если
#                победил человек, иначе - False;
# is_computer_win - возвращает True, если
#                   победил компьютер,
#                   иначе - False;
# is_draw - возвращает True, если ничья,
#           иначе - False.
#
# Наконец, с объектами класса TicTacToe
# должна выполняться функция:
#
# bool(game) - возвращает True, если
#              игра не окончена (никто не
#              победил и есть свободные клетки)
#              и False - в противном случае.
#
# Все эти функции и свойства предполагается
# использовать следующим образом (эти
# строчки в программе не писать):
#
# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")
#
# Вам в программе необходимо объявить
# только два класса: TicTacToe и Cell так,
# чтобы с их помощью можно было бы сыграть
# в "Крестики-нолики" между человеком
# и компьютером.
#
# P.S. Запускать игру и выводить
# что-либо на экран не нужно.
# Только объявить классы.
#
# P.S.S. Домашнее задание: завершите
# создание этой игры и выиграйте у
# компьютера хотя бы один раз.

# import random
#
# class Cell:
#     def __init__(self):
#         self.value = 0
#
#     def __bool__(self):
#         return self.value == 0
#
#
# class TicTacToe:
#     FREE_CELL = 0
#     HUMAN_X = 1
#     COMPUTER_O = 2
#
#     def __init__(self):
#         self.pole = tuple([Cell() for _ in range(3)] for _ in range(3))
#
#     def init(self):
#         self.pole = tuple([Cell() for _ in range(3)] for _ in range(3))
#
#     def show(self):
#         for row in self.pole:
#             print([cell.value for cell in row])
#
#     def human_go(self):
#         while True:
#             try:
#                 i, j = map(int, input("Введите координаты хода в формате 'x y': ").split())
#                 if not (0 <= i <= 2 and 0 <= j <= 2):
#                     raise ValueError
#                 if bool(self.pole[i][j]):
#                     self.pole[i][j].value = self.HUMAN_X
#                     break
#                 else:
#                     print("Клетка занята, попробуйте снова.")
#             except ValueError:
#                 print("Некорректный ввод, попробуйте снова.")
#
#     def computer_go(self):
#         available_cells = [(i, j) for i in range(3) for j in range(3) if bool(self.pole[i][j])]
#         if available_cells:
#             i, j = random.choice(available_cells)
#             self.pole[i][j].value = self.COMPUTER_O
#
#     @property
#     def is_human_win(self):
#         return any(all(self.pole[i][j].value == self.HUMAN_X for j in range(3)) or
#                    all(self.pole[j][i].value == self.HUMAN_X for j in range(3)) for i in range(3)) or \
#                all(self.pole[i][i].value == self.HUMAN_X for i in range(3)) or \
#                all(self.pole[i][2 - i].value == self.HUMAN_X for i in range(3))
#
#     @property
#     def is_computer_win(self):
#         return any(all(self.pole[i][j].value == self.COMPUTER_O for j in range(3)) or
#                    all(self.pole[j][i].value == self.COMPUTER_O for j in range(3)) for i in range(3)) or \
#                all(self.pole[i][i].value == self.COMPUTER_O for i in range(3)) or \
#                all(self.pole[i][2 - i].value == self.COMPUTER_O for i in range(3))
#
#     @property
#     def is_draw(self):
#         return all(self.pole[i][j].value != self.FREE_CELL for i in range(3) for j in range(3))
#
#     def __bool__(self):
#         return not (self.is_human_win or self.is_computer_win or self.is_draw)
#
#     def __getitem__(self, key):
#         i, j = key
#         return self.pole[i][j].value
#
#     def __setitem__(self, key, value):
#         i, j = key
#         if not (0 <= i <= 2 and 0 <= j <= 2):
#             raise IndexError('некорректно указанные индексы')
#         self.pole[i][j].value = value
#
# # тесты, которые должна проходить программа
#
#
# cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
# assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
# cell.value = 1
# assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"
#
# assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"
#
# game = TicTacToe()
# assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
# assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
# game[1, 1] = TicTacToe.HUMAN_X
# assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
#
# game[0, 0] = TicTacToe.COMPUTER_O
# assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
#
# game.init()
# assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"
#
# try:
#     game[3, 0] = 4
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
# game.init()
# assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"
#
# game[0, 0] = TicTacToe.HUMAN_X
# game[1, 1] = TicTacToe.HUMAN_X
# game[2, 2] = TicTacToe.HUMAN_X
# assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
#
# game.init()
# game[0, 0] = TicTacToe.COMPUTER_O
# game[1, 0] = TicTacToe.COMPUTER_O
# game[2, 0] = TicTacToe.COMPUTER_O
# assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

