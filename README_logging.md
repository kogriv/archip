Для создания документа использовались материалы платного курса Олега Мочалова
`https://boosty.to/omolchanov/posts/20b11a20-1b42-415e-b93d-2b9d0104e023`

Также другие открытые обучающий материалы

## logging common case

Создаем просто логгер - корневой объект (root)
```python
logger = logging.getLogger()
```
`.getLogger()` принимает только один аргумент - имя_логгера. При вызовез без переданного значения создается корневой логгер: `<RootLogger root (WARNING)> `.

Логгеры - объекты, которые предоставляют API для работы с логированием.
Когда мы вызываем методы логеров (`.debug()`, `.info()` ...), логеры создают объекты - экземпляры класса `LogRecord`, которые содержат всю нужную информацию о произошедшем событии (это могут быть имена ф-й, в которых вызваются методы логера, имя модуля, номер строки, время события, значения переменных и т.д.)
Полный список - в документации - `LogRecord attributes`. Собственно, объекты `LogRecord` - это и есть те данные, которые пишутся в лог.
Затем объекты `LogRecord` направляются логером в обработчик(и) `Handler`, которые фильтруют эти записи, и с нужными что то делают (обрабатывают: выводят в консоль, в лог-файл, отправляют не почту и т.д).
Обработчики создаются отдельными инструкциями (независимо от логгеров) и привызываются (добавляются) к объектам-логерам.
Дефолтный обработчик выводит обращение в консоль (`StreamHandler`)
Объекты `LogRecord` перед выводом в назначенное место необходимо преобразовать в строку. Для этого используются объекты класса `Formatter`. Форматировщики создаются отдельными инструкциями (независимо от обработчиков). Форматировщики привязываются к объектам-обработчикам.

Пример
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# настройка обработчика - создается как отдельная от логера сущность
handler = logging.FileHandler(f"{__name__}.log", mode='w')
# настройка форматировщика - создается как отдельная от обработчика сущность
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
handler.setFormatter(formatter)
# добавление обработчика к логгеру
logger.addHandler(handler)

logger.info(f"Testing the custom logger for module {__name__}...")
```

## уровни

По умолчанию объекты рут-логера имеют уровень `WARNING`. Уровень можно вывести на печать:
```python
print(logger.level)
```

Установка инструкцией
```python
logger.setLevel('DEBUG') # 10 / logging.DEBUG
```

Уровни логеров и обработчиков устанавливаются независимо друг от друга.

Привязанные к логеру обработчики можно вывести инструкцией:
```python
print(logger.handlers)
```

## Обработчик базовый

Для несконфигурированного рут-логера (полученного инструкцией `logging.getLogger()`) создается обработчик класса `StreamHandler()` с уровнем `WARNING`.

`StreamHandler()` пишет сообщения не просто в канал `stdout`, а в канал для ошибок `stderr`, поэтому сообщения выводятся красным цветом.

Такой обработчик создается, но не закрепляется за объектом рут-логер. Инструкция `print(logging.getLogger().handlers)` выдаст пустой список.

# Конфигурация базовая

Базовая конфигурация логера инструкцией:
```python
logging.basicConfig()
```
Установит рут-логгер уровень в `NOTSET`. Также создаст обработчик `[<StreamHandler <stderr> (NOTSET)>]`

Базовая конфигурация логера инструкцией:
```python
logging.basicConfig(level='DEBUG')
```
Даст результат:
- объект логера `<RootLogger root (DEBUG)>`
- обработчики `[<StreamHandler <stderr> (NOTSET)>]` - <Пишем в консоль> <Канал> <Уровень>
- дефолтный формат сообщения: `DEBUG:root:<Some_massage>`

`.basicConfig` - проверяет у рутового логера наличие закрепленных за ним обработчиков (используя `.handlers`). Если обработчиков нет, то метод создает обработчик класса `StreamHandler` и закрепляет его за объектом рут-логер (присваивает его в аттрибутах `.handlers`). По дефолту у такого обработчика устананавливается уровень `NOTSET`

При указании имени файла в аргументах метода, создастся обработчик `FileHandler` для записи в файл:
`[<FileHandler C:\path\to\file\filename.log (NOTSET)>]`

```python
logging.basicConfig(level='DEBUG',
                    filename='filename.log')
```
По дефолту у такого обработчика `FileHandler` устананавливается уровень также `NOTSET`

## Подмодули и ОДИНОЧКА
Выполним код:
```python
import logging
import requests

logging.basicConfig(level='DEBUG')

logger = logging.getLogger()

def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')
    r = requests.get('https://www.google.ru')


if __name__ == '__main__':
    main('func_name_specified')
```
Получим вывод
```cmd
DEBUG:root:Enter in the main() function: name = func_name_specified
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.google.ru:443
DEBUG:urllib3.connectionpool:https://www.google.ru:443 "GET / HTTP/1.1" 200 None
```

Мы видим вывод от библиотек, используемых подмодулей. Все дело в том, что модуль `logging` использует паттерн `Singletone` (одиночка). Т.е. это глобальный модуль для всего нашего проекта.

Объекты-логеры - глобальны.

`logging.basicConfig(level='DEBUG')` создает глобальные установки для всех используемых нами модулей. Поскольку `.basicConfig` создает настройки для рут-логера, и т.к. все логеры имеют своим предком рут-логер, то базовая конфигурация затронет все подмодули проекта.

Посмотреть все логеры, используемые в проекте (используем менеджер):
```python
for key in logging.Logger.manager.loggerDict:
    print(key)
```

Получим
```cmd
DEBUG:root:Enter in the main() function: name = func_name_specified
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.google.ru:443
urllib3.util.retry
urllib3.util
urllib3
urllib3.connection
urllib3.response
urllib3.connectionpool
urllib3.poolmanager
charset_normalizer
requests
DEBUG:urllib3.connectionpool:https://www.google.ru:443 "GET / HTTP/1.1" 200 None
```
"Выключим" логер `urllib3`.
```python
logging.getLogger('urllib3').setLevel('CRITICAL')
```

## Иерархия логгеров

Создадим именованный логер. И посмотрим его предка
```python
app_logger = logging.getLogger('app_logger')
print(app_logger)
print(app_logger.parent)
```
Получим
```cmd
<Logger app_logger (WARNING)>
<RootLogger root (WARNING)>
```
Иерархия: `root.app_logger.child_1.child_2...`

По умолчанию используется уровень, который установлен на предке. Установка уровня более низкого, чем на предке, при `propagate` = `True`, не изменит уровень. Уровень будет унаследован от предка.

Рассмотрим как происходит обработка сообщений в следующем коде:
```python
import logging

logging.basicConfig()

print('logging.getLogger info:',logging.getLogger())
print('logging.getLogger parent info:',logging.getLogger().parent)
print()

logger = logging.getLogger()
logger.setLevel('INFO')
print('logging.getLogger info:',logging.getLogger())
print('logging.getLogger parent info:',logging.getLogger().parent)
print()

print('logger info:',logger)
print('logger parent info:',logger.parent)
print()

app_logger = logging.getLogger('app_logger')
print('app_logger info:',app_logger)
print('app_logger parent info:',app_logger.parent)
print('app_logger Handlers:',app_logger.handlers)

print()
print('root Handlers:',app_logger.parent.handlers)
print()

utils_logger = logging.getLogger('app_logger.utils')
utils_logger.setLevel('DEBUG')
print('app.logger.utils info:',utils_logger)
print('app.logger.utils parent info:',utils_logger.parent)
print('utils_logger Handlers:',utils_logger.handlers)

def main():
    utils_logger.debug('Hellow world')


if __name__ == '__main__':
    main()
```
Получим вывод
```cmd
DEBUG:app_logger.utils:Hellow world
logging.getLogger info: <RootLogger root (INFO)>
logging.getLogger parent info: None

setting logger (root) level to INFO
logging.getLogger info: <RootLogger root (INFO)>
logging.getLogger parent info: None

logger info: <RootLogger root (INFO)>
logger parent info: None

app_logger info: <Logger app_logger (INFO)>
app_logger parent info: <RootLogger root (INFO)>
app_logger Handlers: []

root Handlers: [<StreamHandler <stderr> (NOTSET)>]

app.logger.utils info: <Logger app_logger.utils (DEBUG)>
app.logger.utils parent info: <Logger app_logger (INFO)>
utils_logger Handlers: []
```

Происходит следующее:
Самый младший логгер `utils` установлен в `DEBUG`. Логгер начинает работу (создает объект `LogRecord`) только при условии, что метод вызова (.gebug('msg'), .info('msg.), ...) не ниже установленного уровня у логгера. Здесь - совпадает `utils_logger.debug(...)` и `utils_logger.setLevel('DEBUG')`. Но при этом у данного логера нет привязанных обработчиков. Поэтому логгер передает сообщение вверх по иерархии. Родительский логгер app_logger уже не проверяет уровень сообщения от наследника (не фильтрует), и пытается обработать его. При отсутствии привязанных обработчиков, app_logger передает сообщение к своему предку- в данном случае к рут-логгеру. У рута уже есть обработчик `root Handlers: [<StreamHandler <stderr> (NOTSET)>]`, уровень которого не выше уровня метода наследника `utils_logger.debug(...)` запустившего процесс- поэтому сообщение будет обработано этим обработчиком.
Все существующие обработчики каждого предка (при соответствии уровня обработчика методу-стартеру) обработают данное сообщение.
Этот процесс называется propagation - распространение.

## propagate

Если этому атрибуту `propagate` присвоено значение `True`, события, зарегистрированные в этом регистраторе, будут переданы обработчикам регистраторов более высокого уровня (предков) в дополнение к любым обработчикам, подключенным к этому регистратору. Сообщения передаются непосредственно обработчикам регистраторов-предков - ни уровень, ни фильтры рассматриваемых регистраторов-предков не учитываются.

Если значение этого параметра равно `False`, сообщения о протоколировании не передаются обработчикам регистраторов-предков.

Поясним это на примере: если атрибут propagate регистратора с именем `A.B.C` принимает значение `True`, любое событие, зарегистрированное в `A.B.C` с помощью вызова метода, такого как `logging.getLogger('A.B.C').error(...)`, будет [при условии передачи уровня этого регистратора и настройки фильтра] передано по очереди любым обработчикам, подключенным к регистраторам с именами `A.B`, `A` и корневому регистратору, после предварительной передачи любым обработчикам, подключенным к `A.B.C`. Если для любого регистратора в цепочке `A.B.C`, `A.B`, `A` атрибут `propagate` установлен в значение `False`, то это последний регистратор, обработчикам которого предлагается обработать событие, и распространение прекращается на этом этапе.

Конструктор устанавливает для этого атрибута значение True.

```python
child_logger.propagate = True  # Включаем наследование уровня журналирования
```

