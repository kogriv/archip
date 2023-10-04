
# 10
# В программе предполагается реализовать
# парсер (обработчик) строки с данными string
# в определенный выходной формат.
# Для этого объявлен следующий класс:
'''
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq
'''
# И предполагается его использовать следующим
# образом:
'''
res = Loader.parse_format("4, 5, -6", Factory)
'''
# На выходе (в переменной res) ожидается
# получать список из набора целых чисел.
# Например, для заданной строки, должно
# получиться:
#
# [4, 5, -6]
#
# Для реализации этой идеи необходимо
# вначале программы прописать класс Factory
# с двумя статическими методами:
#
# build_sequence() - для создания пустого
# списка (метод возвращает пустой список);
# build_number(string) - для преобразования
# строки (string) в целое число (метод
# озвращает полученное целочисленное значение).
#
# Объявите класс с именем Factory, чтобы
# получать на выходе искомый результат.

# class Factory:
#     @staticmethod
#     def build_sequence():
#         return []
#
#     @staticmethod
#     def build_number(string):
#         return int(string)
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
# res = Loader.parse_format("4, 5, -6", Factory)

# 7
# В программе объявлен следующий класс для
# работы с формами ввода логин/пароль:
'''
class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join([
        '<form action="#">',
        self.login.get_html(),
        self.password.get_html(),
        '</form>'
        ])
'''
# Который предполагается использовать
# следующим образом:
'''
login = FormLogin(
    TextInput("Логин"),
    PasswordInput("Пароль")
)
html = login.render_template()
'''
# Необходимо прописать классы TextInput и
# PasswordInput, объекты которых формируются
# командами:
'''
login = TextInput(name, size)
psw = PasswordInput(name, size)
'''
# В каждом объекте этих классов должны
# быть следующие локальные свойства:
#
# name - название для поля (сохраняет
# передаваемое имя, например, "Логин" или
# "Пароль");
# size - размер поля ввода
# (целое число, по умолчанию 10).
#
# Также классы TextInput и PasswordInput
# должны иметь метод:
#
# get_html(self) - возвращает сформированную
# HTML-строку в формате (1-я строка для класса
# TextInput ; 2-я - для класса PasswordInput):
'''
<p class='login'><имя поля>: <input type='text' size=<размер поля> />
<p class='password'><имя поля>: <input type='text' size=<размер поля> />
'''
# Например, для поля login:
'''
<p class='login'>Логин: <input type='text' size=10 />
'''
# Также классы TextInput и PasswordInput
# должны иметь метод класса (@classmethod):
#
# check_name(cls, name) - для проверки
# корректности переданного имя поля (следует
# вызывать в инициализаторе) по следующим критериям:
#
# - длина имени не менее 3 символов и не более 50;
# - в именах могут использоваться только
# символы русского, английского алфавитов,
# цифры и пробелы
#
# Если проверка не проходит, то генерировать
# исключение командой:
#
# raise ValueError("некорректное поле name")
#
# Для проверки допустимых символов в каждом
# классе должен быть прописан атрибут
# CHARS_CORRECT:
'''
CHARS = \
"абвгдеёжзийклмнопрстуфхцчшщьыъэюя " \
+ ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
'''
# По заданию нужно объявить только классы
# TextInput и PasswordInput с соответствующим
# функционалом. Более ничего.
#
# P. S. В данном задании получится дублирование
# кода в классах TextInput и PasswordInput.
# На данном этапе - это нормально.

# from string import ascii_lowercase, digits
#
# # здесь объявляйте классы
# # TextInput и PasswordInput
# class TextInput:
#     CHARS = \
#     "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " \
#     + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     @classmethod
#     def check_name(cls, name):
#         if (type(name) != str
#             or len(name) < 3
#             or len(name) > 50
#         ):
#             raise ValueError(
#                 "некорректное поле name")
#
#         if not set(name) < set(cls.CHARS_CORRECT):
#             raise ValueError(
#                 "некорректное поле name")
#
#     def __init__(self,name,size: int = 10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         responce = f"<p class='login'>{self.name}" +\
#         f": <input type='text' size={self.size} />"
#         return responce
#
# class PasswordInput:
#     CHARS = \
#     "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " \
#     + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     @classmethod
#     def check_name(cls, name):
#         if (type(name) != str
#             or len(name) < 3
#             or len(name) > 50
#         ):
#             raise ValueError(
#                 "некорректное поле name")
#
#         if not set(name) < set(cls.CHARS_CORRECT):
#             raise ValueError(
#                 "некорректное поле name")
#
#     def __init__(self,name,size: int = 10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         responce = f"<p class='password'>{self.name}" +\
#         f": <input type='text' size={self.size} />"
#         return responce
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()

#******************************************
# 8
# Объявите класс CardCheck для проверки
# корректности информации на пластиковых
# картах. Этот класс должен иметь
# следующие методы:
#
# check_card_number(number) - проверяет
# строку с номером карты и возвращает
# булево значение True, если номер в
# верном формате и False - в противном
# случае. Формат номера следующий:
# XXXX-XXXX-XXXX-XXXX,
# где X - любая цифра (от 0 до 9).
# check_name(name) - проверяет строку
# name с именем пользователя карты.
# Возвращает булево значение True,
# если имя записано верно и False
# - в противном случае.
#
# Формат имени: два слова (имя и фамилия)
# через пробел, записанные заглавными
# латинскими символами и цифрами.
# Например, SERGEI BALAKIREV.
#
# Предполагается использовать класс
# CardCheck следующим образом (эти
# строчки в программе не писать):
#
# is_number = CardCheck\
# .check_card_number("1234-5678-9012-0000")
# is_name = CardCheck\
# .check_name("SERGEI BALAKIREV")
#
# Для проверки допустимых символов в
# классе должен быть прописан атрибут:
#
# CHARS_FOR_NAME = \
# ascii_lowercase.upper() + digits
#
# Подумайте, как правильнее объявить
# методы check_card_number и check_name
# (декораторами @classmethod и @staticmethod).

# from string import ascii_lowercase, digits
# class CardCheck:
#     CHARS_FOR_NAME = \
#         ascii_lowercase.upper() + digits
#     SET_CHARS = set(CHARS_FOR_NAME)
#
#     @classmethod
#     def check_card_number(cls, number):
#         if type(number) != str:
#             return  False
#         s = number.split('-')
#         # проверка, что строка из
#         # 4-х фрагментов
#         if len(s) != 4:
#             return False
#         if not all(map(
#             lambda  x: len(x) == 4,s)):
#             return False
#         return all(map(
#             lambda x: x.isdigit(),s))
#
#     @classmethod
#     def check_name(cls, name):
#         if type(name) != str:
#             return  False
#         s = name.split()
#         if len(s) != 2:
#             return False
#         return all(map(
#             lambda x: set(x) < cls.SET_CHARS,
#             s
#         ))

# ******************************************
# ******************************************
# ******************************************

# 9
# Объявите в программе класс Video с
# двумя методами:
#
# create(self, name) - для задания
# имени name текущего видео (метод
# сохраняет имя name в локальном
# атрибуте name объекта класса Video);
# play(self) - для воспроизведения
# видео (метод выводит на экран строку
# "воспроизведение видео <name>").
#
# Объявите еще один класс с именем
# YouTube, в котором объявите два
# метода (с декоратором @classmethod):
#
# add_video(cls, video) - для добавления
# нового видео (метод помещает объект
# video класса Video в список);
# play(cls, video_indx) - для
# проигрывания видео из списка по указанному
# индексу (индексация с нуля).
#
# (здесь cls - ссылка на класс YouTube).
# И список (тоже внутри класса YouTube):
#
# videos - для хранения добавленных
# объектов класса Video (изначально
# список пуст).
#
# Метод play() класса YouTube должен
# обращаться к объекту класса Video
# по индексу списка videos и, затем,
# вызывать метод play() класса Video.
#
# Методы add_video и play вызывайте
# напрямую из класса YouTube. Создавать
# экземпляр этого класса не нужно.
#
# Создайте два объекта v1 и v2 класса
# Video, затем, через метод create()
# передайте им имена "Python" и
# "Python ООП". После этого с помощью
# метода add_video класса YouTube,
# добавьте в него эти два видео и
# воспроизведите (с помощью метода
# play класса YouTube) сначала первое,
# а затем, второе видео

# class Video:
#
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"воспроизведение видео {self.name}")
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
#
# v1 = Video()
# v2 = Video()
# v1.create('Python')
# v2.create('Python ООП')
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)

# ******************************************
# ******************************************
# ******************************************

# 10
# Объявите класс AppStore - интернет-магазин
# приложений для устройств под iOS. В этом
# классе должны быть реализованы следующие
# методы:
#
# add_application(self, app) - добавление
# нового приложения app в магазин;
# remove_application(self, app) - удаление
# приложения app из магазина;
# block_application(self, app) - блокировка
# приложения app (устанавливает локальное
# свойство blocked объекта app в
# значение True);
# total_apps(self) - возвращает общее
# число приложений в магазине.
#
# Класс AppStore предполагается использовать
# следующим образом (эти строчки
# в программе не писать):
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
#
# Здесь Application - класс, описывающий
# добавляемое приложение с указанным
# именем. Каждый объект класса Application
# должен содержать локальные свойства:
#
# name - наименование приложения (строка);
# blocked - булево значение:
# - True - приложение заблокировано;
# - False - не заблокировано;
# изначально False.
#
# Как хранить список приложений
# в объектах класса AppStore решите сами.

# class Application:
#     def __init__(self, name):
#         self.name = name
#         self.blocked = False
#
# class AppStore:
#     def __init__(self):
#         self.apps = {}
#
#     def add_application(self, app):
#         self.apps[id(app)] = app
#
#     def remove_application(self, app):
#         self.apps.pop(id(app))
#
#     def block_application(self, app):
#         obj = self.apps.get(id(app),False)
#         if not obj:
#             return False
#         obj.blocked = True
#         return True
#
#     def total_apps(self):
#         return len(self.apps)
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)

# ******************************************
# ******************************************
# ******************************************

# 11
# Объявите класс для мессенджера с именем
# Viber. В этом классе должны быть
# следующие методы:
#
# add_message(msg) - добавление нового
# сообщения в список сообщений;
# remove_message(msg) - удаление
# сообщения из списка;
# set_like(msg) - поставить/убрать лайк
# для сообщения msg (т.е. изменить
# атрибут fl_like объекта msg: если
# лайка нет то он ставится, если уже
# есть, то убирается);
# show_last_message(число) - отображение
# последних сообщений;
# total_messages() - возвращает общее
# число сообщений.
#
# Эти методы предполагается использовать
# следующим образом (эти строчки в
# программе не писать):
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(
# Message("Это курс по Python ООП."))
# Viber.add_message(
# Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
#
# Класс Message (необходимо также объявить)
# позволяет создавать объекты-сообщения
# со следующим набором локальных свойств:
#
# text - текст сообщения (строка);
# fl_like - поставлен или не поставлен
# лайк у сообщения (булево значение
# True - если лайк есть и
# False - в противном случае,
# изначально False)

# class Viber:
#     messages = {}
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.messages[id(msg)] = msg
#
#     @classmethod
#     def remove_message(cls, msg):
#         obj = cls.messages.get(id(msg), False)
#         '''
#         key id(msg)
#         if key in cls.messages:
#             ...
#         '''
#         if not obj:
#             return False
#         cls.messages.pop(id(msg))
#         return True
#
#     @classmethod
#     def set_like(cls, msg):
#         msg.fl_like = not msg.fl_like
#         '''
#         is_like = cls.messages[id(msg)].fl_like
#         if is_like:
#             cls.messages[id(msg)].fl_like = False
#         else:
#             cls.messages[id(msg)].fl_like = True
#         '''
#
#     @classmethod
#     def show_last_message(cls, number):
#         # берем отрицательный срез словаря
#         # при этом необходимо сделать кортеж
#         for m in tuple(cls.messages.values())[-number:]:
#             print(m.text)
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.messages)
#
# class Message:
#     def __init__(self, text):
#         self.text = text
#         self.fl_like = False
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.show_last_message(2)
# Viber.remove_message(msg)
