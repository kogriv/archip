# class LimitException(Exception):
#     """Превышение лимита"""
#
#
# error = LimitException('превышение лимита нагрузки')
# raise error

# class LimitException(Exception):
#     """Превышение лимита"""
#
#
# class ServerLimitException(LimitException):
#     """Превышение нагрузки на сервер"""
#
#
# try:
#     raise ServerLimitException('превышение серверной нагрузки')
# except LimitException:
#     print("LimitException")
# except ServerLimitException:
#     print("ServerLimitException")

# 4
# Объявите класс-исключение с именем StringException,
# унаследованным от базового класса Exception.
# После этого объявите еще два класса-исключения:
#
# NegativeLengthString - ошибка, если длина отрицательная;
# ExceedLengthString - ошибка, если длина превышает заданное значение;
#
# унаследованные от базового класса StringException.
#
# Затем, в блоке try (см. программу) пропишите
# команду генерации исключения для перехода в
# блок обработки исключения ExceedLengthString.

# class StringException(Exception):
#     pass
#
# class NegativeLengthString(StringException):
#     pass
#
# class ExceedLengthString(StringException):
#     pass
#
# try:
#     raise ExceedLengthString("Длина строки превышает заданное значение")
# except NegativeLengthString:
#     print("NegativeLengthString")
# except ExceedLengthString:
#     print("ExceedLengthString")
# except StringException:
#     print("StringException")

# 5
# Объявите в программе класс-исключение
# с именем PrimaryKeyError, унаследованным
# от базового класса Exception. Объекты
# класса PrimaryKeyError должны
# создаваться командами:
#
# e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
# e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
# e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
#
# В первом варианте команды должно
# формироваться сообщение об ошибке
# "Первичный ключ должен быть целым
# неотрицательным числом". При втором варианте:
#
# "Значение первичного ключа id = <id> недопустимо"
#
# И при третьем:
#
# "Значение первичного ключа pk = <pk> недопустимо"
#
# Эти сообщения должны формироваться
# при отображении объектов класса PrimaryKeyError, например:
#
# print(e2) # Значение первичного
# ключа id = abc недопустимо
#
# Затем, сгенерируйте это исключение с
# аргументом id = -10.5, обработайте его
# и отобразите на экране объект исключения.
#
# Sample Input:
#
# Sample Output:
# Значение первичного ключа id = -10.5 недопустимо

# class PrimaryKeyError(Exception):
#     def __init__(self, id=None, pk=None):
#         if id is not None:
#             self.message = f"Значение первичного ключа id = {id} недопустимо"
#         elif pk is not None:
#             self.message = f"Значение первичного ключа pk = {pk} недопустимо"
#         else:
#             self.message = "Первичный ключ должен быть целым неотрицательным числом"
#
#     def __str__(self):
#         return self.message
#
# e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
# e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
# e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
#
# try:
#     raise PrimaryKeyError(id=-10.5)
# except PrimaryKeyError as e:
#     print(e)

# 6
# Объявите класс DateString для представления
# дат, объекты которого создаются командой:
#
# date = DateString(date_string)
#
# где date_string - строка с датой в формате:
#
# "DD.MM.YYYY"
#
# здесь
# DD - день (целое число от 1 до 31);
# MM - месяц (целое число от 1 до 12);
# YYYY - год (целое число от 1 до 3000).
# Например:
#
# date = DateString("26.05.2022")
# или
# date = DateString("26.5.2022") # незначащий ноль может отсутствовать
#
# Если указанная дата в строке записана
# неверно (не по формату), то генерировать
# исключение с помощью собственного класса:
#
# DateError - класс-исключения,
# унаследованный от класса Exception.
#
# В самом классе DateString переопределить
# магический метод __str__() для формирования
# строки даты в формате:
#
# "DD.MM.YYYY"
#
# (здесь должны фигурировать незначащие нули,
# например, для аргумента "26.5.2022" должна
# формироваться строка "26.05.2022").
#
# Далее, в программе выполняется считывание
# строки из входного потока командой:
#
# date_string = input()
#
# Ваша задача создать объект класса DateString
# с аргументом date_string и вывести
# объект на экран командой:
#
# print(date) # date - объект класса DateString
#
# Если же произошло исключение,
# то вывести сообщение (без кавычек):
#
# "Неверный формат даты"
#
# Sample Input:
#
# 1.2.1812
# Sample Output:
# 01.02.1812

# class DateError(Exception):
#     pass
#
# class DateString:
#     def __init__(self, date_string):
#         try:
#             day, month, year = map(int, date_string.split('.'))
#             if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3000):
#                 raise DateError
#             self.date_string = date_string
#         except:
#             raise DateError
#
#     def __str__(self):
#         day, month, year = map(int, self.date_string.split('.'))
#         return f"{day:02d}.{month:02d}.{year:04d}"
#
#
#
# date_string = input()
#
# # здесь создавайте объект класса DateString и выполняйте обработку исключений
# try:
#     date = DateString(date_string)
#     print(date)
# except DateError:
#     print("Неверный формат даты")

# 7
# Вам поручается разработать класс TupleData,
# элементами которого могут являются только
# объекты классов:
# CellInteger, CellFloat и CellString.
# Вначале в программе нужно объявить класс
# CellInteger, CellFloat и CellString,
# объекты которых создаются командами:
#
# cell_1 = CellInteger(min_value, max_value)
# cell_2 = CellFloat(min_value, max_value)
# cell_3 = CellString(min_length, max_length)
#
# где
# min_value, max_value - минимальное и максимальное
#   допустимое значение в ячейке;
# min_length, max_length - минимальная и максимальная
#   допустимая длина строки в ячейке.
#
# В каждом объекте этих классов должны
# формироваться локальные атрибуты с именами
# _min_value, _max_value или _min_length, _max_length
# и соответствующими значениями.
#
# Запись и считывание текущего значения в
# ячейке должно выполняться через
# объект-свойство (property) с именем:
#
# value - для записи и считывания значения
#   в ячейке (изначально возвращает значение None).
#
# Если в момент записи новое значение не
# соответствует диапазону
# [min_value; max_value] или [min_length; max_length],
# то генерируется исключения командами:
#
# raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
# raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
# raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
#
# Все три класса исключений должны быть
# унаследованы от одного общего класса:
#
# CellException
#
# Далее, объявите класс TupleData,
# объекты которого создаются командой:
#
# ld = TupleData(cell_1, ..., cell_N)
#
# где
# cell_1, ..., cell_N - объекты классов CellInteger,
#   CellFloat и CellString (в любом порядке и любом количестве).
#
# Обращение к отдельной ячейке должно
# выполняться с помощью оператора:
#
# value = ld[index] # считывание значения из ячейке с индексом index
# ld[index] = value # запись нового значения в ячейку с индексом index
#
# Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом. Если значение index выходит за диапазон [0; число ячеек-1], то генерировать исключение IndexError.
#
# Также с объектами класса TupleData
# должны выполняться следующие функции и операторы:
#
# res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
# for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
#     print(d)
#
# Все эти классы в программе можно использовать следующим образом:
#
# ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
#
# try:
#     ld[0] = 1
#     ld[1] = 20
#     ld[2] = -5.6
#     ld[3] = "Python ООП"
# except CellIntegerException as e:
#     print(e)
# except CellFloatException as e:
#     print(e)
# except CellStringException as e:
#     print(e)
# except CellException:
#     print("Ошибка при обращении к ячейке")
# except Exception:
#     print("Общая ошибка при работе с объектом TupleData")
#
# P.S. Данная программа должна быть
# выполнена штатно, без ошибок.
# На экран отображать ничего не нужно.


# class CellException(Exception):
#     pass
#
# class CellIntegerException(CellException):
#     pass
#
# class CellFloatException(CellException):
#     pass
#
# class CellStringException(CellException):
#     pass
#
# class CellInteger:
#     def __init__(self, min_value, max_value):
#         self._min_value = min_value
#         self._max_value = max_value
#         self._value = None
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, val):
#         if not (self._min_value <= val <= self._max_value):
#             raise CellIntegerException('значение выходит за допустимый диапазон')
#         self._value = val
#
# class CellFloat:
#     def __init__(self, min_value, max_value):
#         self._min_value = min_value
#         self._max_value = max_value
#         self._value = None
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, val):
#         if not (self._min_value <= val <= self._max_value):
#             raise CellFloatException('значение выходит за допустимый диапазон')
#         self._value = val
#
# class CellString:
#     def __init__(self, min_length, max_length):
#         self._min_length = min_length
#         self._max_length = max_length
#         self._value = None
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, val):
#         if not (self._min_length <= len(val) <= self._max_length):
#             raise CellStringException('длина строки выходит за допустимый диапазон')
#         self._value = val
#
# class TupleData:
#     def __init__(self, *cells):
#         self._data = list(cells)
#
#     def __len__(self):
#         return len(self._data)
#
#     def __getitem__(self, index):
#         if not 0 <= index < len(self._data):
#             raise IndexError
#         return self._data[index].value
#
#     def __setitem__(self, index, value):
#         if not 0 <= index < len(self._data):
#             raise IndexError
#         self._data[index].value = value
#
#     def __iter__(self):
#         for cell in self._data:
#             yield cell.value
#
# # эти строчки в программе не менять!
# ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
#
# try:
#     ld[0] = 1
#     ld[1] = 20
#     ld[2] = -5.6
#     ld[3] = "Python ООП"
# except CellIntegerException as e:
#     print(e)
# except CellFloatException as e:
#     print(e)
# except CellStringException as e:
#     print(e)
# except CellException:
#     print("Ошибка при обращении к ячейке")
# except Exception:
#     print("Общая ошибка при работе с объектом TupleData")
#
# t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))
#
# d = (1, 0, 'sergey')
# t[0] = d[0]
# t[1] = d[1]
# t[2] = d[2]
# for i, x in enumerate(t):
#     assert x == d[i], "объект класса TupleData хранит неверную информацию"
#
# assert len(t) == 3, "неверное число элементов в объекте класса TupleData"
#
# cell = CellFloat(-5, 5)
# try:
#     cell.value = -6.0
# except CellFloatException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellFloatException"
#
# cell = CellInteger(-1, 7)
# try:
#     cell.value = 8
# except CellIntegerException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellIntegerException"
#
# cell = CellString(5, 7)
# try:
#     cell.value = "hello world"
# except CellStringException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellStringException"
#
# assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
#     CellStringException,
#     CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"

