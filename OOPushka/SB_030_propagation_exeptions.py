# class Geom:
#     def __init__(self, width, color):
#         if type(width) not in (int, float) or type(color) != str or width < 0:
#             raise ValueError('неверные параметры фигуры')
#
#         self._width = width
#         self._color = color
#
#
# class Ellipse(Geom):
#     def __init__(self, x1, y1, x2, y2, width=1, color='red'):
#         super().__init__(width, color)
#
#         if not self._is_valid(x1) or not self._is_valid(y1) or not self._is_valid(x2) or not self._is_valid(y2):
#             raise ValueError('неверные координаты фигуры')
#
#         self._x1 = x1
#         self._y1 = y1
#         self._x2 = x2
#         self._y2 = y2
#
#     def _is_valid(self, x):
#         return type(x) in (int, float)
#
# try:
#     x1, y1, x2, y2, w = map(float, input().split())
#     el = Ellipse(x1, y1, x2, y2, w)
# except ValueError as e:
#     print('exception:',e)

# def input_int_numbers():
#     while True:
#         try:
#             user_input = input().split()
#             if not user_input:
#                 raise EOFError('Нет ввода. Программа завершена.')
#             if all(isinstance(num, int) for num in user_input):
#                 numbers = tuple(map(int, user_input))
#                 return numbers
#             else:
#                 raise TypeError('все числа должны быть целыми')
#         except ValueError:
#             raise TypeError('все числа должны быть целыми')
#
# while True:
#     try:
#         result = input_int_numbers()
#         print(' '.join(map(str, result)))
#         break
#     except TypeError as e:
#         print(e)

# 4
# Объявите класс с именем ValidatorString, объекты которого создаются командой:
#
# vs = ValidatorString(min_length, max_length, chars)
#
# где min_length, max_length - минимально и максимально допустимая длина строки (целые числа, формируемые диапазон [min_length; max_length]); chars - строка из набора символов (хотя бы один из них должен присутствовать в проверяемой строке). Если chars - пустая строка, то проверку на вхождение символов не делать.
#
# В самом классе ValidatorString объявите метод:
#
# def is_valid(self, string): ...
#
# который проверяет строку string на соответствие критериям: string должна быть строкой, с длиной в диапазоне [min_length; max_length] и в string присутствует хотя бы один символ из chars. Если хотя бы один из этих критериев не выполняется, то генерируется исключение командой:
#
# raise ValueError('недопустимая строка')
#
# Затем, объявите класс с именем LoginForm, объекты которого создаются командой:
#
# lg = LoginForm(login_validator, password_validator)
#
# где login_validator - валидатор для логина (объект класса ValidatorString); password_validator - валидатор для пароля (объект класса ValidatorString).
#
# В самом классе LoginForm объявите следующий метод:
#
# def form(self, request): ...
#
# где request - объект запроса (словарь). В словаре request должен быть ключ 'login' со значением введенного логина (строки) и ключ 'password' со значением введенного пароля (строка). Если хотя бы одного ключа нет, то генерировать исключение командой:
#
# raise TypeError('в запросе отсутствует логин или пароль')
#
# В противном случае (если проверка для request прошла), проверять корректность полученного формой логина и пароля с помощью валидаторов, указанных в параметрах login_validator и password_validator, при создании объекта формы.
#
# Если логин/пароль введены верно, то в объекте класса LoginForm локальным атрибутам _login и _password присвоить соответствующие значения.
#
# Пример использования классов (эти строчки должны быть в программе):
#
# login_v = ValidatorString(4, 50, "")
# password_v = ValidatorString(10, 50, "!$#@%&?")
# lg = LoginForm(login_v, password_v)
# login, password = input().split()
# try:
#     lg.form({'login': login, 'password': password})
# except (TypeError, ValueError) as e:
#     print(e)
# else:
#     print(lg._login)
#
# Sample Input:
#
# sergey balakirev!
#
# Sample Output:
#
# sergey

# здесь объявляйте классы
# class ValidatorString:
#     def __init__(self, min_length, max_length, chars):
#         self.min_length = min_length
#         self.max_length = max_length
#         self.chars = chars
#
#     def is_valid(self, string):
#         if not isinstance(string, str) or not self.min_length <= len(string) <= self.max_length:
#             raise ValueError('недопустимая строка')
#
#         if self.chars:
#             if not any(char in self.chars for char in string):
#                 raise ValueError('недопустимая строка')
#
#
# class LoginForm:
#     def __init__(self, login_validator, password_validator):
#         self.login_validator = login_validator
#         self.password_validator = password_validator
#         self._login = None
#         self._password = None
#
#     def form(self, request):
#         if 'login' not in request or 'password' not in request:
#             raise TypeError('в запросе отсутствует логин или пароль')
#
#         login = request['login']
#         password = request['password']
#
#         try:
#             self.login_validator.is_valid(login)
#             self.password_validator.is_valid(password)
#             self._login = login
#             self._password = password
#         except ValueError as e:
#             raise e
#
# login_v = ValidatorString(4, 50, "")
# password_v = ValidatorString(10, 50, "!$#@%&?")
# lg = LoginForm(login_v, password_v)
# login, password = input().split()
# try:
#     lg.form({'login': login, 'password': password})
# except (TypeError, ValueError) as e:
#     print(e)
# else:
#     print(lg._login)

# 5
# Вы начинаете разрабатывать свой сервис
# по тестированию. Для этого вам поручается
# разработать базовый класс Test для всех
# видов тестов, объекты которого
# создаются командой:
#
# test = Test(descr)
#
# где descr - формулировка теста (строка).
# Если длина строки descr меньше 10 или
# больше 10 000 символов, то генерировать
# исключение командой:
#
# raise ValueError('формулировка теста
# должна быть от 10 до 10 000 символов')
#
# В самом классе Test должен быть
# объявлен абстрактный метод:
#
# def run(self): ...
#
# который должен быть переопределен в
# дочернем классе. Если это не так, то
# должно генерироваться исключение командой:
#
# raise NotImplementedError
#
# Далее, объявите дочерний класс с именем
# TestAnsDigit для тестирования правильного
# введенного числового ответа на вопрос теста.
# Объекты класса TestAnsDigit должны
# создаваться командой:
#
# test_d = TestAnsDigit(descr, ans_digit, max_error_digit)
#
# где
# ans_digit - верный числовой ответ на тест;
# max_error_digit - максимальная погрешность
#   в указании числового ответа (необходимо для
#   проверки корректности вещественных чисел,
#   по умолчанию принимает значение 0.01).
#
# Если аргумент ans_digit или max_error_digit
# не число (также проверить, что max_error_digit
# больше или равно нулю), то генерировать
# исключение командой:
#
# raise ValueError('недопустимые значения аргументов теста')
#
# В классе TestAnsDigit переопределите метод:
#
# def run(self): ...
#
# который должен читать строку из входного
# потока (ответ пользователя) командой:
#
# ans = float(input()) # именно такой
# командой, ее прописывайте в методе run()
#
# и возвращать булево значение True,
# если введенный числовой ответ ans
# принадлежит диапазону
# [ans_digit-max_error_digit; ans_digit+max_error_digit].
# Иначе возвращается булево значение False.
#
# Теперь нужно воспользоваться классом
# TestAnsDigit. Для этого в программе
# вначале читается сам тест с помощью команд:
#
# descr, ans = map(str.strip, input().split('|'))
#       # например: Какое значение получится
#       # при вычислении 2+2? | 4
# ans = float(ans) # здесь для простоты полагаем,
#                  # что ans точно число и ошибок
#                  # в преобразовании быть не может
#
# Далее, вам необходимо создать объект класса
# TestAnsDigit с аргументами descr, ans,
# а аргумент max_error_digit должен принимать
# значение по умолчанию 0.01.
#
# Запустите тест командой run() и выведите
# на экран результат его работы (значение
# True или False). Если в процессе создания
# объекта класса TestAnsDigit или в процессе
# работы метода run() возникли исключения,
# то они должны быть обработаны и на экран
# выведено сообщение, содержащееся в исключении.
#
# Sample Input:
#
# Какое значение получим, при выполнении команды int(5.7)? | 5
# 6
# Sample Output:
# False

# class Test:
#     def __init__(self, descr):
#         if not (10 <= len(descr) <= 10000):
#             raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
#         self.descr = descr
#
#     def run(self):
#         raise NotImplementedError("Метод должен быть переопределен.")
#
# class TestAnsDigit(Test):
#     def __init__(self, descr, ans_digit, max_error_digit=0.01):
#         if not (isinstance(ans_digit, (int, float)) and \
#                 isinstance(max_error_digit, (int, float)) and \
#                 max_error_digit >= 0):
#             raise ValueError('недопустимые значения аргументов теста')
#         super().__init__(descr)
#         self.ans_digit = ans_digit
#         self.max_error_digit = max_error_digit
#
#     def run(self):
#         ans = float(input())
#         return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit
#
# # например: Какое значение получится
# # при вычислении 2+2? | 4
# descr, ans = map(str.strip, input().split('|'))
#
# # здесь для простоты полагаем, что ans
# # точно число и ошибок в
# # преобразовании быть не может
# ans = float(ans)
#
# try:
#     test = TestAnsDigit(descr,ans)
#     res = test.run()
#     print(res)
# except ValueError as e:
#     print(e)

# 7
# В программе выполняется считывание
# числовых данных из входного
# потока, командой:
#
# digits = list(map(float, input().split()))
#
# Эти данные следует представить
# в виде объекта класса TupleLimit.
# Сам класс должен наследоваться от
# класса tuple, а его объекты
# создаваться командой:
#
# tl = TupleLimit(lst, max_length)
#
# где
# lst - коллекция (список или кортеж) из данных;
# max_length - максимально допустимая длина
#   коллекции TupleLimit.
#
# Если длина lst превышает значение max_length,
# то должно генерироваться исключение командой:
#
# raise ValueError('число элементов коллекции превышает заданный предел')
#
# В самом классе TupleLimit переопределить
# магические методы __str__() и __repr__()
# для отображения объекта класса TupleLimit
# в виде строки из набора данных lst,
# записанных через пробел. Например:
#
# "1.0 2.5 -5.0 11.2"
#
# Создайте в программе объект класса
# TupleLimit для прочитанных данных
# digits и параметром max_length = 5.
# Выведите на экран объект в случае
# его успешного создания. Иначе, выведите
# сообщение обработанного исключения.

# здесь объявляйте класс
# class TupleLimit(tuple):
#     def __new__(cls, lst, max_length):
#         if len(lst) > max_length:
#             raise ValueError('число элементов коллекции превышает заданный предел')
#         return super(TupleLimit, cls).__new__(cls, lst)
#
#     def __str__(self):
#         return ' '.join(map(str, self))
#
#     def __repr__(self):
#         return ' '.join(map(str, self))
#
# digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)
#
# # здесь создавайте объект класса
# try:
#     tl = TupleLimit(digits, 5)
#     print(tl)
# except ValueError as e:
#     print(e)

