# 3
# Объявите класс с именем Clock и определите
# в нем следующие переменные и методы:
#
# - приватная локальная переменная time для
# хранения текущего времени, целое число
# (своя для каждого объекта класса Clock
# с начальным значением 0);
# - публичный метод set_time(tm) для установки
# текущего времени (присваивает значение tm
# приватному локальному свойству time, если
# метод check_time(tm) возвратил True);
# - публичный метод get_time() для получения
# текущего времени из приватной локальной
# переменной time;
# - приватный метод класса check_time(tm)
# для проверки корректности времени в
# переменной tm (возвращает True, если
# значение корректно и False - в противном
# случае).
#
# Проверка корректности выполняется по
# критерию: tm должна быть целым числом,
# больше или равна нулю и меньше 100 000.
#
# Объекты класса Clock предполагается
# использовать командой:
#
# clock = Clock(время)
#
# Создайте объект clock класса Clock
# и установите время, равным 4530.
#
# P.S. На экран ничего выводить не нужно.

# class Clock:
#     __time = 0
#     def __check_time(cls, tm):
#         return type(tm) == int and 0 <= tm < 100_000
#
#     def __init__(self, time):
#         if self.__check_time(time):
#             self.__time = time
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
# clock = Clock(4530)

# 4
# Объявите класс с именем Money и определите
# в нем следующие переменные и методы:
#
# - приватная локальная переменная money
#    (целочисленная) для хранения количества
#    денег (своя для каждого объекта
#    класса Money);
# - публичный метод set_money(money) для
#    передачи нового значения приватной
#    локальной переменной money (изменение
#    выполняется только если метод
#    check_money(money) возвращает
#    значение True);
# - публичный метод get_money() для
#    получения текущего объема
#    средств (денег);
# - публичный метод add_money(mn)
#    для прибавления средств из объекта
#    mn класса Money к средствам
#    текущего объекта;
# - приватный метод класса
#    check_money(money) для проверки
#    корректности объема средств в
#    параметре money (возвращает True,
#    если значение корректно и False -
#    в противном случае).
#
# Проверка корректности выполняется
# по критерию: параметр money должен
# быть целым числом, больше или
# равным нулю.
#
# Пример использования класса Money
# (эти строчки в программе не писать):
#
# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()    # 100
# m2 = mn_2.get_money()    # 120

# class Money:
#
#     def __init__(self, mn):
#         self.__money = 0 # ЛОКАЛЬНАЯ приватная
#         if self.__check_money(mn):
#             self.__money = mn
#
#     @classmethod
#     def __check_money(cls, mn):
#         return type(mn) == int and mn >= 0
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         # mn - объект класса Money
#         self.__money += mn.get_money()

# 6
# Объявите класс Book со следующим набором
# сеттеров и геттеров:
#
# set_title(self, title) - запись в
#   локальное приватное свойство __title
#   объектов класса Book значения title;
# set_author(self, author) - запись в
#   локальное приватное свойство __author
#   объектов класса Book значения author;
# set_price(self, price) - запись в
#   локальное приватное свойство __price
#   объектов класса Book значения price;
# get_title(self) - получение значения
#   локального приватного свойства __title
#   объектов класса Book;
# get_author(self) - получение значения
#   локального приватного свойства __author
#   объектов класса Book;
# get_price(self) - получение значения
#   локального приватного свойства __price
#   объектов класса Book;
#
# Объекты класса Book предполагается
# создавать командой:
#
# book = Book(автор, название, цена)
#
# При этом, в каждом объекте должны
# создаваться приватные локальные свойства:
#
# __author - строка с именем автора;
# __title - строка с названием книги;
# __price - целое число с ценой книги.
#
# P.S. В программе требуется объявить
# только класс. Ничего на экран выводить не нужно

# class Book:
#
#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price

# 7
# Объявите класс Line для описания линии
# на плоскости, объекты которого
# предполагается создавать командой:
#
# line = Line(x1, y1, x2, y2)
#
# При этом в объекте line должны
# создаваться следующие приватные
# локальные свойства:
#
# __x1, __y1 - начальная координата;
# __x2, __y2 - конечная координата.
#
# В самом классе Line должны быть
# реализованы следующие сеттеры и геттеры:
#
# set_coords(self, x1, y1, x2, y2) - для
#   изменения координат линии;
# get_coords(self) - для получения кортежа
#   из текущих координат линии.
#
# А также метод:
#
# draw(self) - для отображения в консоли
# списка текущих координат линии
# (в одну строчку через пробел).
#
# P.S. В программе требуется объявить
# только класс. Ничего на экран выводить не нужно.

# class Line:
#
#     def __init__(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self):
#         return (
#             self.__x1,
#             self.__y1,
#             self.__x2,
#             self.__y2
#         )
#     def draw(self):
#         print(*self.get_coords())

# 8
# Объявите в программе два класса Point
# и Rectangle. Объекты первого класса
# должны создаваться командой:
#
# pt = Point(x, y)
#
# где x, y - координаты точки на плоскости
#   (целые или вещественные числа). При этом
#   в объектах класса Point должны
#   формироваться следующие локальные
#   свойства:
#
# __x, __y - координаты точки на плоскости.
#
# и один геттер:
#
# get_coords() - возвращение кортежа
#   текущих координат __x, __y
#
# Объекты второго класса Rectangle
# (прямоугольник) должны создаваться
# командами:
#
# r1 = Rectangle(Point(x1, y1), Point(x2, y2))
#
# или
#
# r2 = Rectangle(x1, y1, x2, y2)
#
# Здесь первая координата
#   (x1, y1) - верхний левый угол,
# а вторая координата
#   (x2, y2) - правый нижний.
# При этом, в объектах класса Rectangle
# (вне зависимости от способа их создания)
# должны формироваться следующие
# локальные свойства:
#
# __sp - объект класса Point с координатами
#   x1, y1 (верхний левый угол);
# __ep - объект класса Point с координатами
#   x2, y2 (нижний правый угол).
#
# Также к классе Rectangle должны быть
# реализованы следующие методы:
#
# set_coords(self, sp, ep) - изменение
#   текущих координат, где
#   sp, ep - объекты класса Point;
# get_coords(self) - возвращение кортежа
#   из объектов класса Point с текущими
#   координатами прямоугольника (ссылки
#   на локальные свойства __sp и __ep);
# draw(self) - отображение в консоли
#   сообщения:
#   "Прямоугольник с координатами: (x1, y1) (x2, y2)".
#   Здесь x1, y1, x2, y2 - соответствующие
#   числовые значения координат.
#
# Создайте объект rect класса Rectangle с
# координатами (0, 0), (20, 34).
#
# P.S. На экран ничего выводить не нужно.

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return (self.__x, self.__y)
#
# class Rectangle:
#
#     def __init__(self, a, b, c = None, d = None):
#         self.__sp = self.__ep = None
#         if isinstance(a, Point) and isinstance(b, Point):
#             self.__sp = a
#             self.__ep = b
#         elif all(map(lambda x: type(x) in (int,float),(a,b,c,d))):
#             self.__sp = Point(a,b)
#             self.__ep = Point(c,d)
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f"Прямоугольник с координатами: "+
#               f"{self.__sp.get_coords()} {self.__ep.get_coords()}")
#
# rect = Rectangle(0, 0, 20, 34)

# 9
# Необходимо реализовать связный список
# (не список языка Python и не хранить
# объекты в списке Python), когда объекты
# класса ObjList связаны с соседними
# через приватные свойства __next и __prev:
# ...
#
# Для этого объявите класс LinkedList,
# который будет представлять связный
# список в целом и иметь набор
# следующих методов:
#
# add_obj(self, obj) - добавление нового
#   объекта obj класса ObjList в конец
#   связного списка;
# remove_obj(self) - удаление последнего
#   объекта из связного списка;
# get_data(self) - получение списка из
#   строк локального свойства __data
#   всех объектов связного списка.
#
# И в каждом объекте этого класса
# должны создаваться локальные
# публичные атрибуты:
#
# head - ссылка на первый объект
#   связного списка (если список
#   пустой, то head = None);
# tail - ссылка на последний объект
#   связного списка (если список
#   пустой, то tail = None).
#
# Объекты класса ObjList должны иметь
# следующий набор приватных локальных
# свойств:
#
# __next - ссылка на следующий объект
#   связного списка (если следующего
#   объекта нет, то __next = None);
# __prev - ссылка на предыдущий объект
#   связного списка (если предыдущего
#   объекта нет, то __prev = None);
# __data - строка с данными.
#
# Также в классе ObjList должны быть
# реализованы следующие сеттеры и геттеры:
#
# set_next(self, obj) - изменение приватного
#   свойства __next на значение obj;
# set_prev(self, obj) - изменение приватного
#   свойства __prev на значение obj;
# get_next(self) - получение значения
#   приватного свойства __next;
# get_prev(self) - получение значения
#   приватного свойства __prev;
# set_data(self, data) - изменение
#   приватного свойства __data
#   на значение data;
# get_data(self) - получение значения
#   приватного свойства __data.
#
# Создавать объекты класса ObjList
# предполагается командой:
#
# ob = ObjList("данные 1")
#
# А использовать класс LinkedList
# следующим образом (пример, эти строчки
# писать в программе не нужно):
#
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data() # ['данные 1', 'данные 2', 'данные 3']
#
# Объявите в программе классы
# LinkedList и ObjList
# в соответствии с заданием.
#
# P.S. На экран ничего выводить не нужно.

# class ObjList:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = self.__prev = None
#
#     # изменение приватного свойства __next на значение obj;
#     def set_next(self, obj):
#         self.__next = obj
#
#     # изменение приватного свойства __prev на значение obj;
#     def set_prev(self, obj):
#         self.__prev = obj
#
#     # получение значения приватного свойства __next;
#     def get_next(self):
#         return self.__next
#
#     # получение значения приватного свойства __prev;
#     def get_prev(self):
#         return self.__prev
#
#     # изменение приватного свойства __data на значение data;
#     def set_data(self, data):
#         self.__data = data
#
#     # получение значения приватного свойства __data.
#     def get_data(self):
#         return self.__data
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         if self.tail:
#             self.tail.set_next(obj)
#         obj.set_prev(self.tail)
#         self.tail = obj
#         if not self.head:
#             self.head = obj
#
#     def remove_obj(self):
#         if self.tail is None:
#             return
#
#         prev = self.tail.get_prev()
#         if prev:
#             prev.set_next(None)
#         self.tail = prev
#         if self.tail is None:
#             self.head = None
#
#     def get_data(self):
#         s = []
#         h = self.head
#         while h:
#             s.append(h.get_data())
#             h = h.get_next()
#         return s

# 10
# Объявите класс EmailValidator для проверки
# корректности email-адреса. Необходимо
# запретить создание объектов этого класса:
# при создании экземпляров должно возвращаться
# значение None, например:
#
# em = EmailValidator() # None
#
# В самом классе реализовать следующие методы
# класса (@classmethod):
#
# get_random_email(cls) - для генерации случайного
#   email-адреса по формату: xxxxxxx...xxx@gmail.com,
#   где x - любой допустимый символ в email (латинский
#   буквы, цифры, символ подчеркивания и точка);
# check_email(cls, email) - возвращает True, если
#   email записан верно и False - в противном случае.
#
# Корректность строки email определяется по
# следующим критериям:
#
# - допустимые символы: латинский алфавит, цифры,
#   символы подчеркивания, точки и собачка @ (одна);
# - длина email до символа @ не должна превышать
#   100 (сто включительно);
# - длина email после символа @ не должна быть
#   больше 50 (включительно);
# - после символа @ обязательно должна идти
#   хотя бы одна точка;
# - не должно быть двух точек подряд.
#
# Также в классе нужно реализовать приватный
# статический метод класса:
#
# is_email_str(email) - для проверки типа переменной
# email, если строка, то возвращается значение True,
# иначе - False.
#
# Метод is_email_str() следует использовать в методе
# check_email() перед проверкой корректности email.
# Если параметр email не является строкой,
# то check_email() возвращает False.
#
# Пример использования класса EmailValidator
# (эти строчки в программе писать не нужно):
#
# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False
#
# P.S. В программе требуется объявить только класс.
# На экран ничего выводить не нужно.

# from random import randint
# from string import ascii_lowercase, digits, ascii_uppercase
#
# class EmailValidator:
#     EMAIL_CHARS = ascii_uppercase +ascii_lowercase + digits + "_.@"
#     EMAIL_RANDOM_CHARS = ascii_uppercase + ascii_lowercase + digits + "_"
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     @staticmethod
#     def __is_email_str(email):
#         return type(email) == str
#
#     @classmethod
#     def check_email(cls, email):
#         if not cls.__is_email_str(email):
#             return False
#
#         if not set(email) < set(cls.EMAIL_CHARS):
#             return False
#
#         # проверка, что @ одна
#         s = email.split('@')
#         if len(s) != 2:
#             return False
#         if len(s[0]) > 100 or len(s[1]) >50:
#             return False
#         if '.' not in s[1]:
#             return False
#         if email.count('..'):
#             return False
#         return True
#
#     @classmethod
#     def get_random_email(cls):
#         n = randint(4, 20)
#         length = len(cls.EMAIL_RANDOM_CHARS) - 1
#         return ''.join(
#         cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) +\
#         '@gmail.com'




