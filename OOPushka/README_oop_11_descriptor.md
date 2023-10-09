Класс дескриптор, описывающий создание сериализируемых (стандртных) свойств класса. Через дескриптор определяется стандартный интерфейс взаимодействия с тамими свойствами. Свойства таким образом определяются как объекты такого класса-дескриптора.

```python
# дескриптор для взаимодествия с целочисленными координатами
class Integer:
    # self - ссылка на объект-дескриптор, напр.: x = Integer()
    # owner - ссылка на класс, в котором создается self (Point3D)
    # name - имя (строковое) свойства (в данном случае - 'x')
    def __set_name__(self, owner, name):
        self.name = "_" + name
    
    # instanse - ссылка на объект класса Point3d, в котором
    # создается объект-дескриптор (pt = Point3D(1,2,3))
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value

# класс для точек в 3-х мерном пространстве
class Point3D:
    # сериализируемые свойства (координаты)
    x = Integer()
    y = Integer()
    z = Integer()
 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```


