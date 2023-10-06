class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

# вариант 1- через свойство-объект
#     old = property()
#     def get_old(self):
#         return self.__old
#
#     def set_old(self, old):
#         self.__old = old
#
#     # old = property(get_old, set_old)
#     old = old.setter(set_old)
#     old = old.getter(get_old)

# вариант 2- через дектораторы
    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

p = Person('Сергей', 20)
p.__dict__['old'] = 'old attribute in p object'
p.old = 35
print(p.old, p.__dict__)
del p.old
print(p.__dict__)

'''
Получим (до удаления):
`35 {_Person__name': 'Сергей', '_Person__old': 35, 'old': 'old attribute in p object'}`

При работе класса приоритет объекта-свойства
`property` выше, чем у просто аттрибута
с тем же именем.
Поэтому создав локальное свойство путем:
`p.__dict__['old'] = 'old attribute in p object'`
и обратившись после этого к тому же имени 
в объекте: `p.old`. Произойдет вызов
объекта-свойства. А локальное свойство в данном
случае не будет использовано.
'''
