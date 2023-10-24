# class A:
#     def __init__(self, name, old):
#         super().__init__()
#         self.name = name
#         self.old = old
#
#
# class B:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#
# class C(B, A):
#     def __init__(self, name, old, weight, height):
#         super().__init__(name, old)
#         self.weight = weight
#         self.height = height
#
#
# person = C("Balakirev", 33, 80, 185)

# 4
# С помощью множественного наследования
# удобно описывать принадлежность объектов к
# нескольким разным группам.
# Выполним такой пример.
# Определите в программе классы в соответствии
# с их иерархией:
# Digit - базовый класс
# Integer, Float, Positive, Negative - наследуются
# от Digit
# Каждый объект этих классов должен
# создаваться однотипной командой вида:
#
# obj = Имя_класса(value)
#
# где value - числовое значение.
# В каждом классе следует делать свою
# проверку на корректность значения value:
#
# - в классе Digit: value - любое число;
# - в классе Integer: value - целое число;
# - в классе Float: value - вещественное число;
# - в классе Positive: value - положительное число;
# - в классе Negative: value - отрицательное число.
#
# Если проверка не проходит, то генерируется
# исключение командой:
#
# raise TypeError('значение не соответствует типу объекта')
#
# После этого объявите следующие дочерние классы:
#
# PrimeNumber - (простые числа) наследуется от классов Integer и Positive;
# FloatPositive - наследуется от классов Float и Positive.
#
# Создайте три объекта класса PrimeNumber
# и пять объектов класса FloatPositive с
# произвольными допустимыми для них значениями.
# Сохраните все эти объекты в виде списка digits.
#
# Затем, используя функции isinstance() и
# filter(), сформируйте следующие списки из
# указанных объектов:
#
# lst_positive - все объекты, относящиеся к
#                классу Positive;
# lst_float - все объекты, относящиеся к классу Float.
#
# P.S. В программе требуется объявить только
# классы и создать списки. На экран выводить
# ничего не нужно.

# class Digit:
#     def __init__(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('значение не соответствует типу объекта')
#         self.value = value
#
#
# class Integer(Digit):
#     def __init__(self, value):
#         if not isinstance(value, int):
#             raise TypeError('значение не соответствует типу объекта')
#         super().__init__(value)
#
#
# class Float(Digit):
#     def __init__(self, value):
#         if not isinstance(value, float):
#             raise TypeError('значение не соответствует типу объекта')
#         super().__init__(value)
#
#
# class Positive(Digit):
#     def __init__(self, value):
#         if value <= 0:
#             raise TypeError('значение не соответствует типу объекта')
#         super().__init__(value)
#
#
# class Negative(Digit):
#     def __init__(self, value):
#         if value >= 0:
#             raise TypeError('значение не соответствует типу объекта')
#         super().__init__(value)
#
#
# class PrimeNumber(Integer, Positive):
#     def __init__(self, value):
#         if not self.is_prime(value):
#             raise TypeError('значение не соответствует типу объекта')
#         super().__init__(value)
#
#     @staticmethod
#     def is_prime(n):
#         if n <= 1:
#             return False
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
#
#
# class FloatPositive(Float, Positive):
#     def __init__(self, value):
#         if value <= 0:
#             raise TypeError('значение не соответствует типу объекта')
#         super().__init__(value)
#
#
# # Создание объектов
# digits = [
#     PrimeNumber(2),
#     PrimeNumber(3),
#     PrimeNumber(5),
#     FloatPositive(1.5),
#     FloatPositive(2.5),
#     FloatPositive(3.7),
#     FloatPositive(4.2),
#     FloatPositive(5.0)
# ]
#
# # Фильтрация объектов
# lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
# lst_float = list(filter(lambda x: isinstance(x, Float), digits))

# 5
# В программе объявлены два класса:
#
# class ShopItem:
#     ID_SHOP_ITEM = 0
#
#     def __init__(self):
#         super().__init__()
#         ShopItem.ID_SHOP_ITEM += 1
#         self._id = ShopItem.ID_SHOP_ITEM
#
#     def get_pk(self):
#         return self._id
#
#
# class Book(ShopItem):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year
#
# Затем, создается объект класса Book
# (книга) и отображается в консоль:
#
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)
#
# В результате, на экране увидим что то вроде:
#
# <__main__.Book object at 0x0000015FBA4B3D00>
#
# Но нам требуется, чтобы здесь отображались
# локальные атрибуты объекта с
# их значениями в формате:
#
# <атрибут_1>: <значение_1>
# <атрибут_2>: <значение_2>
# ...
# <атрибут_N>: <значение_N>
#
# Для этого вам дают задание
# разработать два класса:
#
# ShopGenericView - для отображения всех
#                   локальных атрибутов
#                   объектов любых дочерних
#                   классов (не только Book);
# ShopUserView - для отображения всех локальных
#                атрибутов, кроме атрибута _id,
#                объектов любых дочерних классов
#                (не только Book).
#
# То есть, в этих классах нужно переопределить
# два магических метода: __str__() и __repr__().
#
# Пример использования классов
# (эти строчки в программе писать не нужно):
#
# class Book(ShopItem, ShopGenericView): ...
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)
# # на экране увидим строчки:
# # _id: 1
# # _title: Python ООП
# # _author: Балакирев
# # _year: 2022
#
# Другой вариант использования классов:
#
# class Book(ShopItem, ShopUserView): ...
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)
# # на экране увидим строчки:
# # _title: Python ООП
# # _author: Балакирев
# # _year: 2022
#
# P.S. В программе требуется объявить
# только классы. На экран выводить
# ничего не нужно.

# class ShopItem:
#     ID_SHOP_ITEM = 0
#
#     def __init__(self):
#         super().__init__()
#         ShopItem.ID_SHOP_ITEM += 1
#         self._id = ShopItem.ID_SHOP_ITEM
#
#     def get_pk(self):
#         return self._id
#
#
# class ShopGenericView:
#     def __str__(self):
#         attributes = [f"{attr}: {getattr(self, attr)}" for attr in vars(self)]
#         return "\n".join(attributes)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class ShopUserView:
#     def __str__(self):
#         attributes = [f"{attr}: {getattr(self, attr)}" for attr in vars(self) if attr != '_id']
#         return "\n".join(attributes)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Book(ShopItem, ShopGenericView):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year
# class Book(ShopItem, ShopUserView):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year
# '''
# С форума:
# На самом деле, ввело в заблуждение то,
# что по условию "class Book(ShopItem):
# " не наследуется он тех классов
# (ShopGenericView и ShopGenericView),
# что нужно определить. Поэтому не мог придумать,
# как оформить наследование, не изменяя уже
# готовый код (обычно ведь мы ничего не
# должны менять!), но тут все наоборот.
# Надо сделать классы, которые будут работать
# с таким условием
# class Book(ShopItem, ShopGenericView):
# и class Book(ShopItem, ShopUserView):
# , т.е. класс Book мы должны переписать
# под новые условия.
# '''

# 8
# Часто множественное наследование используют
# для наполнения дочернего класса определенным
# функционалом. То есть, с указанием каждого
# нового базового класса, дочерний класс
# приобретает все больше и больше возможностей.
# И, наоборот, убирая часть базовых классов,
# дочерний класс теряет соответствующую
# часть функционала.
#
# Например, паттерн миксинов активно используют
# в популярном фреймворке Django.  В частности,
# когда нужно указать дочернему классу,
# какие запросы от клиента он должен обрабатывать
# (запросы типа GET, POST, PUT, DELETE и т.п.).
# В качестве примера реализуем эту идею в очень
# упрощенном виде, но сохраняя
# суть паттерна миксинов.
#
# Предположим, что в программе уже
# существует следующий набор классов:
#
# class RetriveMixin:
#     def get(self, request):
#         return "GET: " + request.get('url')
#
#
# class CreateMixin:
#     def post(self, request):
#         return "POST: " + request.get('url')
#
#
# class UpdateMixin:
#     def put(self, request):
#         return "PUT: " + request.get('url')
#
# Здесь в каждом классе выполняется
# имитация обработки запросов. За GET-запрос
# отвечает метод get() класса RetriveMixin,
# за POST-запрос - метод post() класса
# CreateMixin, за PUT-запрос - метод put()
# класса UpdateMixin.
#
# Далее, вам нужно объявить класс с именем
# GeneralView, в котором следует указать
# атрибут (на уровне класса):
#
# allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
#
# для перечня разрешенных запросов. А также
# объявить метод render_request со
# следующей сигнатурой:
#
# def render_request(self, request): ...
#
# Здесь request - это словарь (объект запроса),
# в котором обязательно должны быть два ключа:
#
# 'url' - адрес для обработки запроса;
# 'method' - метод запроса: 'GET', 'POST', 'PUT', 'DELETE' и т. д.
#
# В методе render_request() нужно сначала
# проверить, является ли указанный запрос
# в словаре request разрешенным
# (присутствует в списке allowed_methods).
# И если это не так, то генерировать
# исключение командой:
#
# raise TypeError(f"Метод {request.get('method')} не разрешен.")
#
# Иначе, вызвать метод по его имени:
#
# method_request = request.get('method').lower()
#               # имя метода, малыми буквами
#
# Подсказка: чтобы получить ссылку на метод
# с именем method_request, воспользуйтесь
# магическим методом __getattribute__().
#
# Для использования полученных классов,
# в программе объявляется следующий
# дочерний класс:
#
# class DetailView(RetriveMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )
#
# Воспользоваться им можно, например,
# следующим образом (эти строчки в
# программе не писать):
#
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
# print(html)   # GET: https://stepik.org/course/116336/
#
# Если в запросе указать другой метод:
#
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
#
# то естественным образом возникнет
# исключение (реализовывать в программе не нужно,
# это уже встроено в сам язык Python):
#
# AttributeError: 'DetailView' object has no attribute 'put'
#
# так как дочерний класс DetailView
# не имеет метода put. Поправить это можно,
# если указать соответствующий базовый класс:
#
# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )
#
# Теперь, при выполнении команд:
#
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
# print(html)
#
# будет выведено:
#
# PUT: https://stepik.org/course/116336/
#
# Это и есть принцип работы паттерна миксинов.
#
# P.S. В программе требуется объявить
# только класс GeneralView. На экран
# выводить ничего не нужно.

# class RetriveMixin:
#     def get(self, request):
#         return "GET: " + request.get('url')
#
#
# class CreateMixin:
#     def post(self, request):
#         return "POST: " + request.get('url')
#
#
# class UpdateMixin:
#     def put(self, request):
#         return "PUT: " + request.get('url')
#
#
# # здесь объявляйте класс GeneralView
# class GeneralView:
#     allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
#
#     def render_request(self, request):
#         if request.get('method') not in self.allowed_methods:
#             raise TypeError(f"Метод {request.get('method')} не разрешен.")
#         try:
#             method_request = request.get('method').lower()
#             return self.__getattribute__(method_request)(request)
#         except AttributeError:
#             raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{method_request}'")
#
# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'POST', )
#
#
# assert issubclass(DetailView, GeneralView), "класс DetailView должен наследоваться от класса GeneralView"
#
#
# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'POST',)
#
#
# view = DetailView()
#
# try:
#     html = view.render_request({'url': '123', 'method': 'POST'})
# except AttributeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение AttributeError при вызове команды render_request({'url': '123', 'method': 'POST'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"
#
# try:
#     html = view.render_request({'url': '123', 'method': 'PUT'})
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError при вызове команды render_request({'url': '123', 'method': 'PUT'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"
#
# html = view.render_request({'url': '123', 'method': 'GET'})
# assert html == "GET: 123", "метод render_request вернул неверные данные"
#
#
# class DetailView(RetriveMixin, UpdateMixin, CreateMixin, GeneralView):
#     allowed_methods = ('GET', 'POST',)
#
#
# view = DetailView()
# html = view.render_request({'url': '123', 'method': 'POST'})
# assert html == "POST: 123", "метод render_request вернул неверные данные"

# 9
# Объявите класс с именем Money (деньги),
# объекты которого создаются командой:
#
# money = Money(value)
#
# где value - любое число (целое или вещественное).
# Если указывается не числовое значение,
# то генерируется исключение командой:
#
# raise TypeError('сумма должна быть числом')
#
# В каждом объекте этого класса должен
# формироваться локальный атрибут _money
# с соответствующим значением. Также в
# классе Money должно быть
# объект-свойство (property):
#
# money - для записи и считывания
# значения из атрибута _money.
#
# В связке с классом Money
# работает еще один класс:
#
# class MoneyOperators:
#     def __add__(self, other):
#         if type(other) in (int, float):
#             return self.__class__(self.money + other)
#
#         if type(self) != type(other):
#             raise TypeError('Разные типы объектов')
#
#         return self.__class__(self.money + other.money)
#
# Он определяет работу арифметических
# операторов. В данном примере описан
# алгоритм сложения двух объектов класса
# Money (или объектов его дочерних классов).
#
# Обратите внимание, как реализован метод
# __add__() в этом классе. Он универсален
# при работе с любыми объектами класса
# Money или его дочерних классов. Здесь
# атрибут __class__ - это ссылка на класс
# объекта self. С помощью __class__ можно
# создавать объекты того же класса, что и self.
#
# Вам необходимо добавить в класс MoneyOperators
# аналогичную реализацию оператора вычитания.
#
# На основе двух классов (Money и MoneyOperators)
# предполагается создавать классы кошельков
# разных валют. Например, так:
#
# class MoneyR(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyR: {self.money}"
#
#
# class MoneyD(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyD: {self.money}"
#
# И, затем применять их следующим образом
# (эти строчки в программе писать не нужно):
#
# m1 = MoneyR(1)
# m2 = MoneyD(2)
# m = m1 + 10
# print(m)  # MoneyR: 11
# m = m1 - 5.4
# m = m1 + m2  # TypeError
#
# P.S. В программе требуется объявить
# только классы. На экран выводить
# ничего не нужно.

# class Money:
#     def __init__(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('сумма должна быть числом')
#         self._money = value
#
#     @property
#     def money(self):
#         return self._money
#
#
# class MoneyOperators:
#     def __add__(self, other):
#         if type(other) in (int, float):
#             return self.__class__(self.money + other)
#         if type(self) != type(other):
#             raise TypeError('Разные типы объектов')
#         return self.__class__(self.money + other.money)
#
#     def __sub__(self, other):
#         if type(other) in (int, float):
#             return self.__class__(self.money - other)
#         if type(self) != type(other):
#             raise TypeError('Разные типы объектов')
#         return self.__class__(self.money - other.money)
#
#
# class MoneyR(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyR: {self.money}"
#
#
# class MoneyD(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyD: {self.money}"

# В Python self.__class__ используется
# для ссылки на класс текущего объекта.
# Это позволяет создавать новый объект
# того же класса, что и текущий, с помощью
# текущего состояния. Таким образом,
# self.__class__ обычно используется внутри
# методов экземпляра класса для создания
# нового объекта того же класса.
#
# В данном случае, инструкция
# self.__class__(self.money + other)
# создает новый объект того же класса,
# что и текущий (так как self.__class__),
# но с обновленным значением атрибута money.
# Она берет текущее значение атрибута money
# у текущего объекта (self.money),
# добавляет к нему значение other и использует
# это новое значение как атрибут money для
# нового объекта того же класса.
# Это позволяет производить арифметические
# операции с объектами класса Money,
# создавая новые объекты того же типа
# с обновленными значениями.
