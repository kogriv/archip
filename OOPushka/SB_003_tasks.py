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
# class Line():
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Rect():
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Ellipse():
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
class TriangleChecker():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        for side in [self.a, self.b, self.c]:
            # print('side:',side)
            if (((not isinstance(side, float)) and
                 (not isinstance(side, int))) or
                side <= 0):
                # print('side not float or int')
                return 1
            # if side <= 0:
                # print('side <=0')
                # return 1
        if (((self.a + self.b) <= self.c) or
            ((self.b + self.c) <= self.a) or
            ((self.a + self.c) <= self.b)
        ):
            return 2
        return 3

a, b, c = map(int, input().split())
# print(a,b,c)
tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())