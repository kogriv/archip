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
# # Односвязный список
# import sys
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     # для присоединения объекта obj такого
#     # же класса к текущему объекту self
#     def link(self, obj):
#         self.next_obj = obj
#
# # считывание списка из входного потока
# # (эту строкуне менять)
# lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять
#
# # На первый добавленный объект класса ListObject
# # должна ссылаться переменная head_obj
# # первая строка в первом объекте
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1, len(lst_in)):
#     obj_new = ListObject(lst_in[i])
#     obj.link(obj_new)
#     obj = obj_new
# ****************************************************
# ****************************************************
# ****************************************************
#
# 10
# Объявите два класса:
#
# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером
# N x N клеток.
#
# С помощью класса Cell предполагается создавать
# отдельные клетки командой:
#
# c1 = Cell(around_mines, mine)
#
# Здесь around_mines - число мин вокруг данной клетки поля;
# mine - булева величина (True/False), означающая
# наличие мины в текущей клетке. При этом, в
# каждом объекте класса Cell должны создаваться локальные
# свойства:
#
# around_mines - число мин вокруг клетки
#                (начальное значение 0);
# mine - наличие/отсутствие мины в текущей клетке
#        (True/False);
# fl_open - открыта/закрыта клетка - булево значение
#           (True/False).
#           Изначально все клетки закрыты (False).
#
# С помощью класса GamePole должна быть возможность
# создавать квадратное игровое поле с числом клеток N x N:
#
# pole_game = GamePole(N, M)
#
# Здесь N - размер поля; M - общее число мин на поле.
# При этом, каждая клетка представляется объектом
# класса Cell и все объекты хранятся в двумерном
# списке N x N элементов - локальном свойстве pole
# объекта класса GamePole.
#
# В классе GamePole должны быть также реализованы
# следующие методы:
#
# init() - инициализация поля с новой расстановкой
#          M мин (случайным образом по игровому полю,
#          разумеется каждая мина должна находиться в
#          отдельной клетке).
# show() - отображение поля в консоли в виде таблицы
#          чисел открытых клеток (если клетка не открыта,
#          то отображается символ #;
#          мина отображается символом *;
#          между клетками при отображении ставить пробел).
#
# При создании экземпляра класса GamePole в его
# инициализаторе следует вызывать метод init() для
# первоначальной инициализации игрового поля.
#
# В классе GamePole могут быть и другие вспомогательные
# методы.
#
# Создайте экземпляр pole_game класса GamePole
# с размером поля N = 10 и числом мин M = 12.

from random import randint
class Cell:
    def __init__(self, around_mines: int = 0,
                 mine: bool = False
                 ):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [
            [Cell() for column in range(self._n)]
            for row in range(self._n)
        ]
        self.init()
        # print(pole_matrix)

    # расстановка мин
    def init(self):
        m = 0
        while m < self._m:
            column = randint(0, self._n - 1)
            row = randint(0, self._n - 1)
            if self.pole[row][column].mine:
                continue
            self.pole[row][column].mine = True
            m += 1
        # сдвиги индексов вокруг выбранной клетки
        # аффинное преобразование
        idx_shift = ((-1,-1), (-1,0), (-1,1),
                     (0 ,-1),         (0 ,1),
                     (1 ,-1), (1 ,0), (1 ,1))
        # проверка мин вокруг клеток
        for row in range(self._n):
            for column in range(self._n):
                # считаем мины только вокруг
                # не заминированных клеток (?)
                if not self.pole[row][column].mine:
                    mines_around_selected_cell = sum(
                (self.pole[row+row_shift][column+column_shift].mine
                 for row_shift, column_shift in idx_shift
                 if 0 <= row+row_shift < self._n and
                    0 <= column+column_shift <self._n)
                )
                    self.pole[row][column].around_mines = \
                        mines_around_selected_cell
                    # print('cell: ',row+1,column+1, 'mac:',
                    #       self.pole[row][column].around_mines)

    def show(self):
        for row in self.pole:
            print(*map(lambda x:
                    '#' if not x.fl_open
                    else x.around_mines
                        # if not x.mine else '*'
                       , row))
            # print(*map(lambda x: x.around_mines
            #             , row))
        print('================================')
        for row in self.pole:
            print(*map(lambda x:
                    '#' if not x.fl_open
                    else x.around_mines
                        if not x.mine else '*'
                       , row))
            # print(*map(lambda x: x.around_mines
            #             , row))
        print('========self.pole[0][0]=========')
        print(self.pole[0][0])
        print(id(self.pole[0][0]))
        print(hex(id(self.pole[0][0])))

pole_game = GamePole(2, 1)
pole_game.show()