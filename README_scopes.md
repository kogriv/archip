## dir(), globals(), locals()
Давайте рассмотрим, какие инструкции могут помочь вам понять области видимости и принцип замыкания.

1. `locals()` и `globals()` функции:  
- `locals()` возвращает словарь локальных символов в текущей области видимости.
- `globals()` возвращает словарь глобальных символов.  

2. dir() функция:  
- `dir()` возвращает отсортированный список имен в текущей локальной области видимости.


Пример:
```python
def say_name(name):
    def say_goodbye():
        print("Don't say me goodbye, " + name + "!")

    return say_goodbye

f = say_name("Ivan")

print("Global scope dict:", globals())
print("Local scope dict:", locals())
print("Local scope list:", dir())
```

Теперь, касательно замыкания (**closure**), важно понимать, что вложенная функция `say_goodbye` сохраняет доступ к переменной name, даже после завершения вызывающей функции `say_name`. Это происходит потому, что в момент создания функции `say_goodbye`, она "захватывает" (**captures**) переменную name из внешней функции `say_name`. Таким образом, say_goodbye является замыканием, так как она "замыкает" в себе значение `name` из внешней области видимости.

С использованием `dir(f)` вы сможете просмотреть область видимости для переменной `f`, и увидеть, какие имена связаны с этой переменной.
```python
# Используем dir() для просмотра области видимости переменной f
print("Scope list of variable 'f':", dir(f))
```

## Просмотр dir(замыкание)
Для инструкции `print("Scope list of variable 'f':", dir(f))` (`f`- результат замыкания) имеем вывод:
```cmd
Scope list of variable 'f': ['__annotations__', '__builtins__',  
'__call__', '__class__', '__closure__', '__code__', '__defaults__',  
'__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',  
'__ge__', '__get__', '__getattribute__', '__globals__', '__gt__',  
'__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__',  
'__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__',  
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',  
'__str__', '__subclasshook__']
```

Из вывода `dir(f)` можно выделить несколько атрибутов, связанных с внутренней функцией `say_goodbye` и переменной `name`. Вот некоторые из них:

`__closure__`: Этот атрибут содержит кортеж, представляющий замыкание (**closure**). В данном случае, вы можете просмотреть содержимое `__closure__`, чтобы увидеть, какие переменные замыкаются внутри функции `say_goodbye`. Ваш случай должен содержать значение (`'Ivan',`).
`__code__`: Этот атрибут предоставляет объект кода для функции. Вы можете использовать `__code__.co_varnames` для просмотра локальных переменных функции. Ваш случай должен содержать (`'name',`).
`__globals__`: Этот атрибут ссылается на глобальные переменные доступные внутри функции. Ваш случай должен содержать глобальные переменные.

Из полученных данных можно сделать следующие выводы:

**Closure (`__closure__`):**  
Вы видите, что __closure__ содержит кортеж с одним элементом. Этот элемент - объект типа `<cell at 0x...: str object at 0x...>`. Здесь `str object` - это тип объекта (строка), и адрес `0x...` представляет место в памяти, где хранится значение переменной name (в данном случае, `"Ivan"`).

**Local variables (`__code__.co_varnames`):**  
Кортеж имен переменных. В этом случае локальных переменных внутри функции `say_goodbye` нет, поэтому `co_varnames` пуст. Поместив в тело вложенной функции переменную, напрмер `nested_var = 'some_value_for_nested_var'`, в выводе мы увидим: `Local variables f.__code__.co_varnames: ('nested_var',)`

**Globals (`__globals__`):**  
Глобальные переменные в данном случае содержат информацию о модуле, в котором определена функция. `__name__`, `__file__`, и другие глобальные переменные относятся к модулю, в котором выполняется скрипт.

## Используем Closure (`__closure__`) чтобы понять имя замкнутых переменных
Используя атрибут `__closure__`, вы можете получить доступ к значениям переменных, которые замыкаются. В вашем случае `__closure__` содержит кортеж с одним элементом, который представляет замыкание. Этот элемент - объект типа `<cell at 0x...: str object at 0x...>`. Давайте извлечем значение переменной name из этого объекта:
```python
# Извлекаем значение переменной name из замыкания
closure_value = f.__closure__[0].cell_contents
print("Value of closed variable 'name':", closure_value)
```
вывод:
```cmd
Value of closed variable 'name': Ivan
```
Здесь `f.__closure__[0]` предоставляет доступ к ячейке замыкания, а `cell_contents` содержит фактическое значение переменной, которая была замкнута.  
Помните, что это специфично для вашего конкретного примера, где замыкается только одна переменная name. В более сложных случаях с несколькими переменными, вам придется итерироваться по элементам `__closure__` и извлекать значения соответствующих переменных.
```python
# Извлекаем значения переменных из замыкания
closure_values = [cell.cell_contents for cell in f.__closure__]
```

## Получение имен переменных для функции
Для получения имен переменных из функции Python, можно воспользоваться атрибутом `__code__.co_varnames`. Этот атрибут содержит имена аргументов и локальных переменных функции. Вот как это можно сделать:
```python
def get_variable_names(func):
    return func.__code__.co_varnames

def assign_variable_names(func):
    variable_names = get_variable_names(func)
    variable_assignments = [f"var_func_{func.__name__}_{i} = '{name}'" for i, name in enumerate(variable_names)]
    return variable_assignments

print("Variable assignments for nested [f=say_name(..)]:")
# Получаем имена переменных и создаем соответствующие переменные
variable_assignments = assign_variable_names(f)
for assignment in variable_assignments:
    exec(assignment)
# Печатаем созданные переменные
for i in range(len(variable_assignments)):
    print(f"Variable {i}: {eval(f'var_func_say_goodbye_{i}')}")
print('------------------------------------------')

print("Variable assignments for outer [say_name]:")
# Получаем имена переменных и создаем соответствующие переменные
variable_assignments = assign_variable_names(say_name)
for assignment in variable_assignments:
    exec(assignment)
# Печатаем созданные переменные
for i in range(len(variable_assignments)):
    print(f"Variable {i}: {eval(f'var_func_say_name_{i}')}")
print('------------------------------------------')
```
вывод:
```cmd
Variable assignments for f=say_name(..):
Variable 0: nested_var
------------------------------------------
Variable assignments for head:
Variable 0: name
Variable 1: say_goodbye
------------------------------------------
```
В этом примере `get_variable_names` возвращает имена переменных для заданной функции. `assign_variable_names` создает строки, присваивающие каждой переменной свое уникальное имя. Затем создаются соответствующие переменные с использованием `exec`, и их значения выводятся.

