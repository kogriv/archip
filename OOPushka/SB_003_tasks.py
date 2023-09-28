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
class CPU:
    pass
