## Метод
Что называется методом класса?
- Любая (не статическая) функция, объявленная внутри класса
Что называют атрибутами класса?
- Переменные и имена методов (ссылки на методы) класса

## Без сельфи
```python
class Point:
    color = 'red'
    circle = 2
    def set_coords(): # удалим параметр self
        logger.debug('Вызов метода set_coord')
```
Посмотрим
```python
Point.set_coords
```
Получим
```cmd
<function Point.set_coords at 0x000002119A0EA7A0>
```
Имеем функцию.

Запустим:
```python
pt = Point()
pt.set_coords
```
Подучим:
```cmd
<bound method Point.set_coords of <__main__.Point object at 0x000002119A03ED50>>
```
Аттрибут `.set_coords` существует, и он ведет на связанный метод `bound method` класса Point. Вызовем метод на объекте:
```python
pt.set_coords()
```
Получим ошибку:
```cmd
...
TypeError: Point.set_coords() takes 0 positional arguments but 1 was given
```
Это происходит потому, что интерпритатор, при вызыве метода через объект класса, автоматически подставляет параметр `self`, который является ссылкой на экземпляр класса. Это происходит всегда при вызове функций объявленных внутри класса.

Если метод определнный в классе нужен для вызова через объект, то необходимо указывать параметр `self`.

Соответственно, при отсутствии параметра `self`, возможно скрывать доступ к каким то методам, работающим исключительно на уровне пространства имен класса.

## Как выглядит сельфи
Параметр `self` в функции в классе при вызове этой функции на объекте класса получит адрес этого объекта.
```python
class Point:
    color = 'red'
    circle = 2

    def set_coords(self):
        logger.debug('Вызов метода set_coord, self value: '+str(self))
        # print('Вызов метода set_coord')

def main():
    pt = Point()
    logger.debug('object pt str value: '+str(pt))
    pt.set_coords()

if __name__ == '__main__':
    main()
```
Получим:
```cmd
SB_003_methods_self:main:18 - object pt str value: <__main__.Point object at 0x0000024D74AD4E50>
SB_003_methods_self:set_coords:13 - Вызов метода set_coord, self value: <__main__.Point object at 0x0000024D74AD4E50>
```
Объекты совпадают.

## Получение адреса
При выводе на печать объекта класса Cell получаем:
```cmd
<__main__.Cell object at 0x000001B9C80F2210>
```
чтобы получить только адрес объекта:
```python
hex(id(self)).upper()
```
Python не предоставляет стандартного атрибута или магического метода для получения только адреса объекта, предоставляя его в шестнадцатеричной форме (как в hex(id(self))).




## Делать или не делать сельфи
Вызов метода (определенного в классе с параметром `self`) на классе без указания какого либо объекта в качестве аргумента:
```python
Point.set_coords
```
выдаст ошибку:
```cmd
TypeError: Point.set_coords() missing 1 required positional argument: 'self'
```
Необходимо в такой метод передавать аргумент-объект класса.
```python
pt = Point()
Point.set_coords(pt)
```

Инструкция `Point.set_coords(pt)` эквивалентна `pt.set_coords()`

## Установка свойств объекта
Использование `self` позволяет устанавливать индивидуальные значения свойств у объектов (в локальных областях имен этих объектов)
```python
    def set_coords(self, x, y):
        logger.info('Вызов метода set_coord, self value: '+str(self))
        self.x = x
        self.y = y
        logger.info('set_coord установил координаты, x: '
                     +str(self.x)+' y:'+str(self.y))
```
Метод не копируется в экземпляры класса, но можетработать с локальными областями экземпляров объектов через сельфи.

Установим значения:
```python
pt.set_coords(1, 2)
logger.info('property list for object: '+str(pt.__dict__))
```
Локальная область получила свойства:
```cmd
roperty list for object: {'x': 1, 'y': 2}
```

## getattr для получения имени метода
Имена методов класса находятся в пространстве имен класса - являются его аттрибутами.
```python
f = getattr(pt, 'get_coords')
logger.info(str(f))
```
Получим `<bound method Point.get_coords of <__main__.Point object at 0x000001EE57560F10>>` - связанный метод `bound method` класса Point.
Вызов метода:
```python
logger.info('get_coords call result:'+str(f()))
```
```cmd
get_coords call result:(1, 2)
```
Обращение через getattr может быть полезно, когда используется список методов класса.

