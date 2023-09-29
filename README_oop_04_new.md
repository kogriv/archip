## Описание метода __new__
Магический метод __new__ вызывается перед созданием объекта.
Выполним
```python
class Point():
    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для'+str(cls))

    def __init__(self, x=0, y=0):
        print('Вызов метода __init__'+str(self))
        self.x = x
        self.y = y

pt = Point(1,2)
print(pt)
```
`cls` - ссылка на текущий экземпляр класса - как объект базового класса Object
`self` - ссылка еа уже созданный экземпляр
>>>
```cmd
Вызов __new__ для<class '__main__.Point'>
None
```
Т.е. метод __init__ не был вызван. Объект `pt` не был создан. Поскольку при использовании метода __new__ не был возвращен адрес нового объекта. Добавим:
```python
class Point():
    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для'+str(cls))
        return super().__new__(cls)
```
>>>
```cmd
Вызов __new__ для<class '__main__.Point'>
Вызов метода __init__<__main__.Point object at 0x000002641E574B90>
<__main__.Point object at 0x000002641E574B90>
```

