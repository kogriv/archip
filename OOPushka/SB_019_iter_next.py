# from collections.abc import Iterable
#
# my_list = [1, 2, 3, 4, 5]
#
# # Проверка, является ли объект итерируемым
# if hasattr(my_list, '__iter__'):
#     print("Этот объект итерируемый")
#
# if isinstance(my_list, Iterable):
#     print("Этот объект является эземпляром Iterable")

# r = range(1, 3000)
# res1 = 2022 in r   # res1 = True
# res2 = 2022 in r   # res2 = True
# print(res1)
# print(res2)
#
# r = iter(range(1, 3000))
# res1 = 2022 in r   # res1 = True
# res2 = 2023 in r   # res1 = False
# print(res1)
# print(res2)
#
# '''
# В первом варианте объект range в операторе
# in каждый раз возвращает новый итератор и перебор
# последовательности начинается с начала.
# Во втором варианте явно указывается итератор,
# который в строчке res2 = 2022 in r продолжает перебор
# последовательности с числа 2023.
# '''

class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration

