# class Point():
#     def __init__(self, x, y, color = 'black'):
#         self.x = x
#         self.y = y
#         self.color = color
#         # print(self.color)
#
# points = []
# for i in range(1000):
#     if i != 1:
#         points.append(Point(1+2*i,1+2*i))
#     else: points.append(Point(1+2*i,1+2*i,'yellow'))

# from random import randint
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# elements = [(Line, Rect, Ellipse)[randint(0,2)]
#             (1,2,3,4) for n in range(217)]
#
# for obj in elements:
#     if isinstance(obj, Line):
#         obj.sp = obj.ep = 0

# 5
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def is_triangle(self):
#         ''' мое решение
#         for side in [self.a, self.b, self.c]:
#             # print('side:',side)
#             if (((not isinstance(side, float)) and
#                  (not isinstance(side, int))) or
#                 side <= 0):
#                 # print('side not float or int')
#                 return 1
#             # if side <= 0:
#                 # print('side <=0')
#                 # return 1
#         if (((self.a + self.b) <= self.c) or
#             ((self.b + self.c) <= self.a) or
#             ((self.a + self.c) <= self.b)
#         ):
#             return 2
#         return 3
#         '''
#         # красивое решение СБ
#         res_digit = all(map(lambda x: type(x) in (int, float),
#                       (self.a, self.b, self.c)))
#         if not res_digit:
#             return 1
#
#         res_positive = all(map(lambda x: x > 0,
#                       (self.a, self.b, self.c)))
#         if not res_positive:
#             return 1
#
#         a, b, c = self.a, self.b, self.c
#         if a>=b+c or b>=a+c or c >=a+b:
#             return 2
#         return 3
#
# a, b, c = map(int, input().split())
# # print(a,b,c)
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())

# 6
# class Graph:
#     def __init__(self, data, is_show = True):
#         self.data = data[0:]
#         self.is_show = is_show
#
#     def set_data(self, data):
#         self.data = data[0:]
#
#     def show_table(self):
#         if self.is_show:
#             print(*self.data)
#         else: print("Отображение данных закрыто")
#
#     def show_graph(self):
#         if self.is_show:
#             print("Графическое отображение данных:",
#                   *self.data)
#         else: print("Отображение данных закрыто")
#
#     def show_bar(self):
#         if self.is_show:
#             print("Столбчатая диаграмма:",
#                   *self.data)
#         else: print("Отображение данных закрыто")
#
#     def set_show(self, is_show):
#         self.is_show = is_show
#
# data_graph = list(map(int, input().split()))
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()

# 7
# класс для описания процессоров
# from typing import List
# class CPU:
#
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
# # класс для описания памяти
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
# # класс для описания материнских плат
# class MotherBoard:
#     def __init__(self, name, cpu: CPU, *mems):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mems[:self.total_mem_slots]
#
#     def get_config(self):
#         return [
# f'Материнская плата: {self.name}',
# f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
# f'Слотов памяти: {self.total_mem_slots}',
# 'Память: ' + '; '.join(map(lambda x: f'{x.name} - {x.volume}',
#                            self.mem_slots))
#         ]
#
# mb = MotherBoard('RX9',CPU('Ryz0',1000),
#                  Memory('Kig',2000),
#                  Memory('WD',8000))

# 8
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     # добавление в корзину товара, представленного объектом gd
#     def add(self, gd):
#         self.goods.append(gd)
#
#     # удаление из корзины товара по индексу index
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     # получение из корзины товаров в виде списка из строк
#     def get_list(self):
#         return [f'{x.name}: {x.price}' for x in self.goods]
#
# cart = Cart()
# cart.add(TV('sam',1000))
# cart.add(TV('son',1100))
# cart.add(Table('duk',100))
# cart.add(Notebook('dell',1000))
# cart.add(Notebook('len',1000))
# cart.add(Cup('coboyashi',10))

# 9
# Односвязный список
import sys
class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    # для присоединения объекта obj такого
    # же класса к текущему объекту self
    def link(self, obj):
        self.next_obj = obj

# считывание списка из входного потока
# (эту строкуне менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

# На первый добавленный объект класса ListObject
# должна ссылаться переменная head_obj
# первая строка в первом объекте
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new
