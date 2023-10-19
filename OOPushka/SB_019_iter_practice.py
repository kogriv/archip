# Использованы материалы видеокурса Михаила Корнеева

from collections.abc import Iterable
from pprint import pprint

numbers = [1,2,3,4]
if isinstance(numbers, Iterable):
    print("Список numbers = [1,2,3,4] - наследуется от collections.abc.Iterable")
if hasattr(numbers, '__iter__'):
    print("Этот объект итерируемый - имеет атрибут __iter__")
if not hasattr(numbers, '__next__'):
    print("Этот объект НЕ итератор - не имеет атрибут __next__")
print()

# теперь вызовем метод __iter__ на итерируемом объекте
my_iterator = numbers.__iter__() # эквивалентная инструкция: iter(numbers)
print('my_iterator = numbers.__iter__() это',my_iterator)
if isinstance(my_iterator, Iterable):
    print("Итератор numbers.__iter__ - наследуется от collections.abc.Iterable")
if hasattr(my_iterator, '__iter__'):
    print("Этот объект итерируемый - имеет атрибут __iter__")
if hasattr(my_iterator, '__next__'):
    print("Этот объект ЕСТЬ итератор - ИМЕЕТ атрибут __next__")
print()

new_iterator = my_iterator.__iter__()
print('new_iterator = my_iterator.__iter__() это',new_iterator)

print()
if new_iterator is my_iterator:
    pprint('Объект-итератор, созданный на основе исходной последовательности '+
          'совпадает с объектом-итератором, созданным основе объекта-итериатора')

print('***********************************************')

# итерироваться по порождающей последовательности  numbers можно
# с помощью инструкций: new_iterator.__next__ / next(new_iterator)
# до конца последовательности = до появления исключения StopIteration
# инструкция for работает так:
# сначала из последовательности создается итератор путем вызова __iter__
# потом "выстреливает" обойма __next__ до появления исключения
# метод next(iterator_in_for) возвращает значение из последовательности
# и присваивает его переменной-варианте например, i, цикла

# Свой итератор
# можно создавать отдельно классы iterable (без некст) и класс-итератор
# Можно - совмещать. Ниже пример совмещенного класса
print()
print('Пример кастомного итератора. Класс HellowWorld:')

class HellowWorld:
    def __init__(self, num_iters):
        self.num_iters = num_iters
        self.counter = 0

    # __iter__ возвращает объект своего класса
    # поскольку сам уже является итератором
    # т.к. __next__ будет определен
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.counter:
            self.counter += 1
            return "Hello World"
        raise StopIteration

print()
greeter = HellowWorld(3)
print('greeter = HellowWorld(3) это',greeter)

print()
print('greeter.__iter__() это',greeter.__iter__())
if isinstance(greeter, Iterable):
    print("Итератор greeter - наследуется от collections.abc.Iterable")
if hasattr(greeter, '__iter__'):
    print("Этот объект итерируемый - имеет атрибут __iter__")
if hasattr(greeter, '__next__'):
    print("Этот объект ЕСТЬ итератор - ИМЕЕТ атрибут __next__")
print()

# видим, что greeter и greeter.__iter__ - один объект - итератор

# Генератор - наследник итератора
def string_by_letter(string):
    for letter in string:
        yield letter.upper()

gen = string_by_letter('Some string')
print("gen = string_by_letter('Some string') это:",gen)
print('gen.__iter__() это',gen.__iter__())
if isinstance(gen, Iterable):
    print("Итератор gen - наследуется от collections.abc.Iterable")
if hasattr(gen, '__iter__'):
    print("Этот объект итерируемый - имеет атрибут __iter__")
if hasattr(gen, '__next__'):
    print("Этот объект ЕСТЬ итератор - ИМЕЕТ атрибут __next__")
print()