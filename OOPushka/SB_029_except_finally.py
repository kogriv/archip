# try:
#     val = float(input())
# except ValueError as e:
#     print(e)
# else:
#     val *= 10
#     print(val)
#
# try:
#     val = float(input())
# except ValueError as e:
#     print(e)
# else:
#     val *= 10
#     print(val)
# finally:
#     print("finally")

# 4
# В программе вводятся два значения в
# одну строчку через пробел. Значениями
# могут быть числа, слова, булевы величины
# (True/False). Необходимо прочитать эти
# значения из входного потока. Если оба
# значения являются числами, то вычислить
# их сумму, иначе соединить их в одну
# строку с помощью оператора + (конкатенации
# строк). Результат вывести на экран
# (в блоке finally).
#
# P.S. Реализовать программу с
# использованием блоков try/except/finally.

# try:
#     values = input().split()
#     if all(value.isdigit() for value in values):
#         result = sum(map(int, values))
#     else:
#         result = ''.join(values)
# except:
#     result = "Ошибка ввода"
# finally:
#     print(result)

# 6
# В программе объявлена функция для вычисления частного двух чисел:
# def get_div(x, y):
#     try:
#         res = x / y
#         return res
#     except ZeroDivisionError:
#         res = 100
#         return res
#     finally:
#         res = -1
#         print(f"finally: {res}")
#
# # Выберите все верные утверждения, связанные с этой программой.
# print(get_div(10, 0))
# get_div(10, 0)

# 7
# В практике программирования блок else
# используют как элемент отладки программы:
# в него прописывают текст программы, в котором
# заведомо не произойдет исключений, отлавливаемых
# в блоке try. Выполним на практике такой пример.
#
# Вам необходимо объявить функцию с сигнатурой:
#
# def get_loss(w1, w2, w3, w4): ...
#
# где w1, w2, w3, w4 - любые числа. Функция
# должна возвращать значение, вычисленное
# по формуле:
#
# y = 10 * w1 // w2 - 5 * w2 * w3 + w4
#
# Здесь фрагмент вычисления w1 // w2 содержит
# потенциальную ошибку деления на ноль, поэтому
# его следует делать в блоке try. А в блоке
# else продолжить вычисления, где не
# используются операции деления.
#
# Если происходит деление на ноль, то
# функция должна возвращать строку:
#
# "деление на ноль"
#
# P.S. В программе нужно объявить
# только функцию. Вызывать ее и
# выводить на экран ничего не нужно.

# def get_loss(w1, w2, w3, w4):
#     try:
#         result = 10 * w1 // w2 - 5 * w2 * w3 + w4
#     except ZeroDivisionError:
#         return "деление на ноль"
#     else:
#         return result

# 8
#  Объявите класс с именем Rect (прямоугольник),
#  объекты которого создаются командой:
#
# r = Rect(x, y, width, height)
#
# где x, y - координаты верхнего левого угла
# (любые числа); width, height - ширина и
# высота прямоугольника (положительные числа). Ось абсцисс (Ox) направлена вправо, ось ординат (Oy) направлена вниз.
#
# В каждом объекте класса Rect должны
# формироваться локальные атрибуты с именами:
# _x, _y, _width, _height и соответствующими
# значениями. Если переданные аргументы x, y
# (не числа) и width, height не положительные
# числа, то генерировать исключение командой:
#
# raise ValueError('некорректные координаты
# и параметры прямоугольника')
#
# В классе Rect реализовать метод:
#
# def is_collision(self, rect): ...
#
# который проверяет пересечение текущего
# прямоугольника с другим (с объектом rect).
# Если прямоугольники пересекаются, то должно генерироваться исключение командой:
#
# raise TypeError('прямоугольники пересекаются')
#
# Сформировать в программе несколько
# объектов класса Rect со следующими
# значениями:
#
# 0; 0; 5; 3
# 6; 0; 3; 5
# 3; 2; 4; 4
# 0; 8; 8; 1
#
# Сохранить их в списке lst_rect. На
# основе списка lst_rect сформировать еще один список lst_not_collision, в котором должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.
#
# P.S. В программе требуется объявить
# только класс и списки. На экран выводить ничего не нужно.
#
# Подсказка. Для определения пересечения
# двух прямоугольников, у которых стороны
# параллельны осям координат (как в этом
# подвиге) достаточно проверить, что верхняя
# грань первого прямоугольника находится
# ниже нижней грани второго, или нижняя
# грань первого прямоугольника выше
# верхней грани второго. И то же
# самое для вертикальных граней.

# class Rect:
#     def __init__(self, x, y, width, height):
#         if not all(isinstance(i, (int, float)) for i in [x, y, width, height]) or width <= 0 or height <= 0:
#             raise ValueError('некорректные координаты и параметры прямоугольника')
#         self._x = x
#         self._y = y
#         self._width = width
#         self._height = height
#
#     def is_collision(self, rect):
#         if (self._y - self._height > rect._y) or (self._y < rect._y - rect._height) or (self._x + self._width < rect._x) or (self._x > rect._x + rect._width):
#             return False
#         raise TypeError('прямоугольники пересекаются')
#
# lst_rect = [
#     Rect(0, 0, 5, 3),
#     Rect(6, 0, 3, 5),
#     Rect(3, 2, 4, 4),
#     Rect(0, 8, 8, 1)
# ]
#
# def not_collision(rect):
#     for x in lst_rect:
#         try:
#             if x != rect:
#                 rect.is_collision(x)
#         except TypeError:
#             return False
#     return True
#
# lst_not_collision = list(filter(not_collision, lst_rect))
#
#
#
# r = Rect(1, 2, 10, 20)
# assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"
#
# r2 = Rect(1.0, 2, 10.5, 20)
#
# try:
#     r2 = Rect(0, 2, 0, 20)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"
#
#
# assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
# assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"
#
# def not_collision(rect):
#     for x in lst_rect:
#         try:
#             if x != rect:
#                 rect.is_collision(x)
#         except TypeError:
#             return False
#     return True
#
# f = list(filter(not_collision, lst_rect))
# assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"
#
# r = Rect(3, 2, 2, 5)
# rr = Rect(1, 4, 6, 2)
#
# try:
#     r.is_collision(rr)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"

