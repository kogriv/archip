# try:
#     val = float(input())
# except ValueError as e:
#     print(e)

# def get_number(x):
#     try:
#         print('return int(x):',int(x))
#         return int(x)
#     except:
#         try:
#             print('return float(x):', float(x))
#             return float(x)
#         except:
#             print('return x:', x)
#             return x
#
# res_1 = get_number('-5')
# res_2 = get_number('5.78')
# res_3 = get_number('8(912)000-000-00')
# res_4 = get_number(True)

# 5
# В программе объявлен класс Point:
#
# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
# И создается объект этого класса:
#
# pt = Point(1, 2)
#
# Далее, вам нужно обратиться к атрибуту
# z объекта pt и, если такой атрибут существует,
# то вывести его значение на экран.
# Иначе вывести строку (без кавычек):
#
# "Атрибут с именем z не существует"
#
# Реализовать проверку следует с
# помощью блоков try/except.
#
# Подсказка: при обращении к несуществующему
# атрибуту генерируется исключение AttributeError.

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
# pt = Point(1, 2)
#
# try:
#     print(pt.z)
# except AttributeError:
#     print("Атрибут с именем z не существует")

# 7
# В программе вводятся в одну строчку через
# пробел некоторые данные, например:
#
# "1 -5.6 2 abc 0 False 22.5 hello world"
#
# Эти данные разбиваются по пробелу и
# представляются в виде списка строк:
#
# lst_in = input().split()
#
# Ваша задача посчитать сумму всех
# целочисленных значений, присутствующих
# в списке lst_in. Результат (сумму)
# вывести на экран.
#
# Подсказка: отбор только целочисленных
# значений можно выполнить с помощь
# функции filter() с последующим их
# преобразованием в целые числа с помощью
# функции map() и, затем, вычислением их
# суммы с помощью функции sum(). Для отбора
# целочисленных значений рекомендуется
# объявить вспомогательную функцию, которая
# бы возвращала True для строк, в которых
# присутствует целое число и False -
# для всех остальных строк.

# lst_in = input().split()
#
# def is_integer(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False
#
# sum_integers = sum(map(int, filter(is_integer, lst_in)))
# print(sum_integers)

# 8
# В программе вводятся в одну строчку
# через пробел некоторые данные, например:
#
# "1 -5.6 True abc 0 23.56 hello"
#
# Эти данные разбиваются по пробелу
# и представляются в виде списка строк:
#
# lst_in = input().split()
#
# Ваша задача сформировать новый
# список с именем lst_out, в котором
# строки с целыми числами будут
# представлены как целые числа (тип int),
# строки с вещественными числами,
# как вещественные (тип float), а
# остальные данные - без изменений.
#
# Например:
#
# lst_out = [1, -5.6, 'True', 'abc', 0, 23.56, 'hello']  # после обработки введенной строки "1 -5.6 True abc 0 23.56 hello"
#
# Реализовать эту задачу следует с
# помощью функции map() и объявления
# вспомогательной функции с механизмом
# обработки исключений для непосредственного
# преобразования данных в целые
# или вещественные числа.
#
# P.S. В программе нужно только
# сформировать список lst_out.
# На экран ничего выводить не нужно.

# def convert_data(s):
#     try:
#         return int(s)
#     except ValueError:
#         try:
#             return float(s)
#         except ValueError:
#             return s
#
# lst_in = input().split()
# lst_out = list(map(convert_data, lst_in))

# 9
# Объявите в программе класс Triangle,
# объекты которого создаются командой:
#
# tr = Triangle(a, b, c)
#
# где a, b, c - длины сторон треугольника
# (любые положительные числа). В каждом
# объекте класса Triangle должны
# формироваться локальные атрибуты
# _a, _b, _c с соответствующими значениями.
#
# Если в качестве хотя бы одной величины
# a, b, c передается не числовое значение,
# или меньше либо равно нулю, то должно
# генерироваться исключение командой:
#
# raise TypeError('стороны треугольника должны быть положительными числами')
#
# Если из переданных значений a, b, c
# нельзя составить треугольник
# (условие: каждая сторона должна быть
# меньше суммы двух других), то
# генерировать исключение командой:
#
# raise ValueError('из указанных длин сторон нельзя составить треугольник')
#
# Затем, на основе следующего набора данных:
#
# input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
#
# необходимо сформировать объекты
# класса Triangle, но только в том случае,
# если не возникло никаких исключений.
# Все созданные объекты представить
# в виде списка с именем lst_tr.
#
# P.S. В программе нужно только
# сформировать список lst_tr.
# На экран ничего выводить не нужно.

# class Triangle:
#     def __init__(self, a, b, c):
#         if not all(isinstance(side, (int, float)) for side in (a, b, c)) or any(side <= 0 for side in (a, b, c)):
#             raise TypeError('стороны треугольника должны быть положительными числами')
#         if a + b <= c or a + c <= b or b + c <= a:
#             raise ValueError('из указанных длин сторон нельзя составить треугольник')
#         self._a = a
#         self._b = b
#         self._c = c
#
# input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
#
# lst_tr = []
#
# for item in input_data:
#     try:
#         tr = Triangle(*item)
#         lst_tr.append(tr)
#     except (TypeError, ValueError) as e:
#         pass

# 10
# Объявите в программе класс FloatValidator,
# объекты которого создаются командой:
#
# fv = FloatValidator(min_value, max_value)
#
# где min_value, max_value - минимальное и
# максимальное допустимое значение
# (диапазон [min_value; max_value]).
#
# Объекты этого класса предполагается
# использовать следующим образом:
#
# fv(value)
#
# где value - проверяемое значение.
# Если value не вещественное число или не
# принадлежит диапазону [min_value; max_value],
# то генерируется исключение командой:
#
# raise ValueError('значение не прошло валидацию')
#
# По аналогии, объявите класс IntegerValidator,
# объекты которого создаются командой:
#
# iv = IntegerValidator(min_value, max_value)
#
# и используются командой:
#
# iv(value)
#
# Здесь также генерируется исключение:
#
# raise ValueError('значение не прошло валидацию')
#
# если value не целое число или не
# принадлежит диапазону [min_value; max_value].
#
# После этого объявите функцию с сигнатурой:
#
# def is_valid(lst, validators): ...
#
# где
# lst - список из данных;
# validators - список из объектов-валидаторов
#   (объектов классов FloatValidator и IntegerValidator).
#
# Эта функция должна отбирать из
# списка все значения, которые прошли
# хотя бы по одному валидатору.
# И возвращать новый список с элементами,
# прошедшими проверку.
#
# Пример использования классов и
# функции (эти строчки в программе не писать):
#
# fv = FloatValidator(0, 10.5)
# iv = IntegerValidator(-10, 20)
# lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
#
# P.S. В программе нужно только объявить
# классы и функцию. На экран
# ничего выводить не нужно.

class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != float:
            raise ValueError('значение не прошло валидацию')
        if not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')

class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != int:
            raise ValueError('значение не прошло валидацию')
        if not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')

def is_valid(lst, validators):
    valid_values = []
    for value in lst:
        for validator in validators:
            try:
                validator(value)
                valid_values.append(value)
                break
            except ValueError:
                pass
    return valid_values