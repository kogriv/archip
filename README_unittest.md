# Структура библиотеки
Библиотека `unittest` в Python является встроенным модулем, предоставляющим средства для создания и выполнения тестов. Она основана на архитектуре `xUnit`, которая широко используется в разных языках программирования.
**Общая структура библиотеки `unittest`**

Библиотека включает несколько ключевых модулей и классов, каждый из которых выполняет свою роль.
## 1. Основной модуль: `unittest`

Этот модуль предоставляет базовые классы и функции для тестирования.  
**Основные компоненты:**

    `TestCase`:
    Базовый класс для написания тестов.
    Методы:
        `setUp`, `tearDown`: Подготовка и очистка перед/после каждого теста.
        `setUpClass`, `tearDownClass`: Подготовка и очистка на уровне класса.
        Методы утверждений (`assertEqual`, `assertTrue`, `assertRaises` и др.).

    `TestSuite`:
    Класс для объединения нескольких тестов в одну группу (набор тестов).

    `TestLoader`:
    Класс для автоматического поиска и загрузки тестов.

    `TextTestRunner`:
    Класс для выполнения тестов и вывода результатов в текстовом формате.

    `TestResult`:
    Класс для хранения результатов тестов, таких как количество успешных, неудачных и пропущенных тестов.

Пример использования:
```python
import unittest

class ExampleTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()
```
## 2. Модуль: `unittest.mock`

Этот модуль предоставляет инструменты для создания мок-объектов и патчей. Используется для подмены зависимостей, изоляции кода и эмуляции внешних взаимодействий.  
**Основные компоненты:**

    `Mock`:
    Класс для создания мок-объектов, которые могут имитировать поведение любых объектов.

    `patch` / `patch.object`:
    Декораторы и контекстные менеджеры для временной подмены объектов, функций или методов.

    `MagicMock`:
    Расширенная версия `Mock` с предопределёнными магическими методами (например, `__getitem__`, `__call__`).

    `call`, `ANY`, `DEFAULT`:
    Инструменты для проверки вызовов мок-объектов.

Пример использования:
```python
from unittest.mock import Mock

mock_func = Mock(return_value=42)
result = mock_func()
mock_func.assert_called_once()
```
## 3. Модуль: unittest.runner

Этот модуль предоставляет классы и функции для запуска тестов.  
**Основные компоненты:**

    `TextTestRunner`:
    Класс, который выполняет тесты и выводит результаты в текстовом формате.

Пример:
```python
import unittest

suite = unittest.TestSuite()
suite.addTest(unittest.TestCase('test_example'))

runner = unittest.TextTestRunner()
runner.run(suite)
```
## 4. Модуль: unittest.result

Этот модуль определяет класс TestResult, который используется для хранения результатов тестов, таких как успешные, пропущенные и провалившиеся тесты.  
**Основные компоненты:**

    `TestResult`:
    Класс для сбора информации о результатах выполнения тестов.
    Содержит атрибуты: `errors`, `failures`, `skipped`, `testsRun`.

Пример:
```python
import unittest

result = unittest.TestResult()
print(result.testsRun)  # Число запущенных тестов
```
## 5. Модуль: unittest.suite

Модуль предоставляет классы для управления тестовыми наборами.  
**Основные компоненты:**

    `TestSuite`:
    Класс для объединения нескольких тестов в одну группу.

Пример:
```python
import unittest

suite = unittest.TestSuite()
suite.addTest(unittest.TestCase('test_example'))
```
## 6. Модуль: unittest.loader

Используется для автоматической загрузки тестов.
Основные компоненты:

    `TestLoader`:
    Класс для поиска тестов по именам файлов, модулей или классов.

Пример:
```python
loader = unittest.TestLoader()
suite = loader.discover('.')
```
## 7. Модуль: unittest.signals

Этот модуль предоставляет обработчики сигналов, которые позволяют корректно завершать выполнение тестов при прерывании пользователем (например, с помощью `Ctrl+C`).  
Основные компоненты:

    `installHandler`: Устанавливает обработчик сигналов.
    `removeHandler`: Удаляет обработчик сигналов.

## 8. Модуль: unittest.util

Содержит вспомогательные функции для работы с unittest.  
Основные компоненты:

    `strclass`: Преобразует класс в строковое представление.
    `safe_repr`: Создаёт безопасное строковое представление объекта.
    `unorderable_list_difference`: Находит разницу между списками без учёта порядка.

## Взаимосвязь модулей:

    `unittest` (основной) использует `unittest.mock` для подмены зависимостей и `unittest.runner` для запуска тестов.
    `unittest.loader` взаимодействует с `unittest.suite`, чтобы находить и добавлять тесты в набор.
    `unittest.result` хранит результаты выполнения тестов и используется `unittest.runner`.


# Тесты ннннада?
Тесты оправданы в следующих случаях:  
- Зависимость от внешних данных: сеть, файлы, базы данных.  
- Развертывание в нестабильном окружении: зависимость от библиотек.  
- Сложная логика обработки данных: много условий, ошибок.  
- Граничные случаи: большие числа, пустые значения, неожиданные форматы.  
- Работа с системными ресурсами: файловая система, права доступа.  

Тесты помогают минимизировать риски неожиданного поведения программы, особенно в условиях реального развертывания.

## 1. Функция зависит от внешних данных (API, файловая система, база данных)
Если функция использует данные из внешних источников, поведение может зависеть от этих данных. Тесты нужны, чтобы убедиться, что код правильно обрабатывает различные ответы.
Пример: работа с API

Функция для получения данных о пользователе из API:
```python
import requests

def get_user_data(user_id):
    response = requests.get(f"https://example.com/api/users/{user_id}")
    if response.status_code == 404:
        return None
    return response.json()

# testing

import unittest
from unittest.mock import patch

class TestGetUserData(unittest.TestCase):
    @patch('requests.get')
    def test_user_found(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": 1, "name": "John Doe"}
        self.assertEqual(get_user_data(1), {"id": 1, "name": "John Doe"})

    @patch('requests.get')
    def test_user_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        self.assertIsNone(get_user_data(999))
```
Почему это важно?

    Зависимость от сети, доступности API, формата ответа.
    Тесты моделируют разные состояния (успех, ошибка).

## 2. Развертывание с установкой зависимостей

Когда приложение зависит от библиотек, неправильная установка окружения может привести к ошибкам. Тесты помогают убедиться, что код работает в ожидаемом окружении.
Пример: зависимости

Программа, использующая библиотеку pandas:
```python
import pandas as pd

def calculate_mean(data):
    if not isinstance(data, pd.Series):
        raise TypeError("Input must be a pandas Series")
    return data.mean()

# testing
import unittest

class TestCalculateMean(unittest.TestCase):
    def test_correct_input(self):
        import pandas as pd
        data = pd.Series([1, 2, 3, 4])
        self.assertEqual(calculate_mean(data), 2.5)

    def test_missing_dependency(self):
        with self.assertRaises(ModuleNotFoundError):
            import nonexistentlib  # Моделируем ошибку зависимости
```
Почему это важно?

    Позволяет выявить проблемы с окружением и зависимостями.

## 3. Функция обрабатывает сложные данные

Когда входные данные сложны, а результат зависит от многих условий, тесты помогают убедиться в правильности реализации.
Пример: парсинг данных

Функция для извлечения значений из JSON:
```python
def extract_prices(data):
    try:
        return [item['price'] for item in data['items'] if 'price' in item]
    except (KeyError, TypeError):
        raise ValueError("Invalid input data")

# testing
class TestExtractPrices(unittest.TestCase):
    def test_valid_data(self):
        data = {"items": [{"price": 100}, {"price": 200}]}
        self.assertEqual(extract_prices(data), [100, 200])

    def test_missing_price_key(self):
        data = {"items": [{"name": "item1"}, {"price": 200}]}
        self.assertEqual(extract_prices(data), [200])

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            extract_prices(None)
```
Почему это важно?

    Парсинг часто зависит от структуры данных, которая может меняться.
    Тесты моделируют разные типы входных данных (валидные, частично валидные, полностью невалидные).

## 4. Функция обрабатывает большое количество граничных случаев

Если функция имеет сложную логику с разными путями выполнения, тесты нужны для покрытия этих путей.
Пример: расчёт налогов
```python
def calculate_tax(income):
    if income < 0:
        raise ValueError("Income cannot be negative")
    if income <= 10000:
        return 0
    elif income <= 50000:
        return (income - 10000) * 0.1
    else:
        return 4000 + (income - 50000) * 0.2

# testing
class TestCalculateTax(unittest.TestCase):
    def test_no_tax(self):
        self.assertEqual(calculate_tax(5000), 0)

    def test_low_tax_bracket(self):
        self.assertEqual(calculate_tax(30000), 2000)

    def test_high_tax_bracket(self):
        self.assertEqual(calculate_tax(60000), 6000)

    def test_negative_income(self):
        with self.assertRaises(ValueError):
            calculate_tax(-1000)
```
Почему это важно?

    Граничные случаи часто упускают из вида при разработке.
    Тесты обеспечивают предсказуемость поведения.

## 5. Функция работает с системными ресурсами

Когда код взаимодействует с файловой системой, процессами или системными настройками, тесты помогают проверить эти взаимодействия.
Пример: работа с файлами

Функция для записи данных в файл:
```python
def save_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# testing
import os

class TestSaveToFile(unittest.TestCase):
    def test_file_creation(self):
        filename = "test.txt"
        content = "Hello, world!"
        save_to_file(filename, content)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), content)
        os.remove(filename)  # Удаляем файл после теста
```
Почему это важно?

    Функция зависит от среды выполнения (прав на запись, существования папок).
    Тесты проверяют корректность работы с файлами.


# Сначала код, затем тесты или наоборот?

Выбор подхода к написанию программы (сначала код, затем тесты или наоборот) зависит от цели проекта, стиля работы и предпочтений разработчика. Рассмотрим два подхода и их применение.

## 1. Сначала код, потом тесты

Этот подход предполагает написание основного кода, а затем добавление тестов для проверки его работы.

### Как работает:

1. Вы пишете основной код программы.  
2. Разрабатываете тесты, чтобы убедиться в корректности кода.  
3. Исправляете ошибки, если тесты выявляют их.

### Преимущества:

- Удобен для прототипирования: позволяет быстрее реализовать базовый функционал.  
- Хорош для простых задач или когда тесты менее важны.  
- Полезен, если требования к проекту нечеткие или меняются.  

### Недостатки:

- Возможно упущение граничных случаев, если тесты пишутся на этапе завершения работы.  
- Может возникнуть нежелательная привязанность к коду, что затрудняет рефакторинг.  
- Тесты могут быть слабыми, если писать их "на глазок" после реализации.  

---

## 2. Тесты и код пишутся одновременно (или тесты первыми)

Этот подход также называют **Test-Driven Development (TDD)**. Сначала пишутся тесты, затем создается код, который проходит эти тесты.

### Как работает:

1. Вы пишете минимально необходимый тест, чтобы описать ожидаемое поведение функции или модуля.  
2. Создаете минимальный код, чтобы пройти тест.  
3. Улучшаете код, проверяя его тестами.  
4. Повторяете цикл.  

### Преимущества:

- Код покрыт тестами с самого начала.  
- Заставляет вас думать о требованиях и сценариях использования заранее.  
- Помогает избежать избыточного кода: вы пишете только то, что нужно для прохождения теста.  
- Упрощает рефакторинг: тесты подтверждают, что изменения не ломают функционал.  

### Недостатки:

- На первый взгляд требует больше времени, особенно для новичков.  
- Сложнее, если проект неразработан до конца, и нет чётких требований.  
- Может быть трудно реализовать для слишком больших или неопределённых задач.  

---

## 3. Какой подход выбрать?

### Когда писать код, а потом тесты:

- Если вы работаете над исследовательским проектом или прототипом.  
- Когда функционал тривиален и тесты не критичны (например, скрипты для одноразовых задач).  
- Если вы точно знаете, как должна работать программа, и уверены в её реализации.  

### Когда писать тесты первыми или вместе с кодом:

- Если приложение сложное или критически важное (например, финансы, здравоохранение).  
- Когда работа ведётся в команде, и важна уверенность в стабильности кода.  
- Если проект разрабатывается итеративно, с фокусом на долгосрочную поддержку.  

---

## 4. Гибридный подход

Многие разработчики используют комбинированный подход:

- Для сложных или критичных частей системы пишут тесты до кода (TDD).  
- Для остальной части программы тесты добавляют после написания основного кода.  

### Рекомендации:

- Если вы новичок: начните с написания основного кода, а потом добавляйте тесты. Со временем экспериментируйте с TDD.  
- Если проект большой: попробуйте писать тесты на ключевые функции или критические компоненты перед их реализацией.  
- Автоматизируйте тестирование: используйте инструменты, такие как `pytest` или `unittest`, чтобы тесты запускались автоматически при изменении кода.  
- Не бойтесь рефакторить: если написание тестов показывает, что ваш код сложен или плохо структурирован, улучшите его.  

Главное — стремиться к тому, чтобы код оставался читаемым, надежным и легко проверяемым.

# TDD пайплайн. Как делать тесты без самой программы.

**Test-Driven Development (TDD)** — это методология разработки, в которой сначала пишутся тесты, а затем сам код, который должен эти тесты пройти.

## Пайплайн TDD

1. **Написание теста:**
    - Вы определяете, что именно должна делать функция или часть программы.
    - Пишете тест, который описывает это поведение.
    - Тест изначально не проходит, так как функция ещё не реализована.

2. **Реализация кода:**
    - Реализуете минимально необходимый код, чтобы тест прошёл.
    - Это может быть самый простой способ, даже если он временный.

3. **Запуск теста:**
    - Убедитесь, что новый тест проходит.
    - При необходимости дорабатываете код.

4. **Рефакторинг:**
    - Улучшаете структуру кода, делаете его более читаемым и оптимальным.
    - Тесты служат гарантией, что изменения не ломают функциональность.

5. **Повторение:**
    - Добавляете новый тест.
    - Реализуете новый функционал.
    - Постепенно выстраиваете приложение, поддерживая высокое качество кода.

## Как писать тесты без программы

TDD предполагает, что тесты пишутся до того, как код создан. Это достигается за счёт чёткого понимания требований и планирования. Вот пример процесса:

### Пример TDD

**Требование:**

Создать функцию `add_positive_numbers(a, b)`, которая:

- Принимает два положительных числа.
- Складывает их и возвращает результат.
- Выбрасывает ошибку, если одно из чисел отрицательное.

### 1. Написание тестов (без реализации кода)

```python
import unittest

class TestAddPositiveNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_positive_numbers(2, 3), 5)  # Сложение двух положительных чисел
    
    def test_negative_number_error(self):
        with self.assertRaises(ValueError):
            add_positive_numbers(-1, 3)  # Один из аргументов отрицательный
    
    def test_zero_is_invalid(self):
        with self.assertRaises(ValueError):
            add_positive_numbers(0, 5)  # Ноль не считается положительным числом

if __name__ == "__main__":
    unittest.main()
```
Что происходит:

    Вы пишете тесты, как если бы функция уже существовала.
    Эти тесты описывают желаемое поведение.

### 2. Запуск тестов

Если вы запустите тесты сейчас, они не пройдут, потому что функции add_positive_numbers ещё не существует.
### 3. Реализация минимального кода

Создаём минимальную реализацию функции, чтобы тесты начали проходить:
```python
def add_positive_numbers(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive")
    return a + b
```
### 4. Проверка тестов

Запускаем тесты снова. Если все тесты проходят — код работает корректно.
### 5. Рефакторинг

Если требуется, можно улучшить код или тесты. Например:

    Добавить больше проверок.
    Оптимизировать код функции.

Преимущества подхода TDD

    Чёткое понимание требований: Тесты формируют спецификацию для кода.
    Меньше ошибок: Ошибки выявляются до того, как код разрастётся.
    Простота рефакторинга: Тесты гарантируют, что изменения не ломают функциональность.
    Документация: Тесты объясняют, как должен работать код.

**Когда TDD сложен**

    Если требования не ясны — сложно описать поведение заранее.
    Для исследовательского кода, где неизвестно, будет ли он работать.
    В случаях, когда тесты требуют сложной настройки окружения или данных.

**Заключение**

В TDD тесты пишутся первыми и задают направление разработки. Начинать стоит с маленьких, конкретных функций, постепенно выстраивая весь функционал. Это позволяет разрабатывать стабильные, протестированные приложения, особенно полезные для долгосрочных проектов.

# Пирамида тестов
**Пирамида тестов** — это концепция в тестировании, описывающая соотношение различных уровней тестов, которые должны быть написаны для обеспечения надежности системы. Она помогает сбалансировать скорость тестирования, стоимость и охват.

---

## Основная идея
Пирамида тестов изображает, как уровни тестирования организованы в виде трёхслойной структуры:
1. **Юнит-тесты** — база пирамиды (самая большая часть).
2. **Интеграционные тесты** — средний уровень.
3. **Энд-то-энд (E2E) или UI-тесты** — вершина.

Чем ниже уровень в пирамиде:
- Тем больше таких тестов должно быть.
- Тем быстрее они выполняются.
- Тем дешевле их написание и поддержка.

---

## Уровни пирамиды тестов

### 1. **Юнит-тесты (Unit Tests)**
- **Описание**: Тестируют отдельные функции или методы изолированно от других частей системы.
- **Цель**: Убедиться, что каждая функция/метод работает корректно.
- **Примеры**:
  - Проверка функции расчёта налога.
  - Проверка обработки исключений в методе.
- **Особенности**:
  - Быстрые.
  - Простые в написании.
  - Не зависят от внешнего окружения (БД, API).
- **Инструменты**: `unittest`, `pytest`.

### 2. **Интеграционные тесты (Integration Tests)**
- **Описание**: Тестируют взаимодействие между модулями, компонентами или внешними системами (например, базой данных или API).
- **Цель**: Проверить, как компоненты системы работают вместе.
- **Примеры**:
  - Проверка, что функция корректно записывает данные в базу.
  - Тестирование взаимодействия между микросервисами.
- **Особенности**:
  - Медленнее, чем юнит-тесты.
  - Часто требуют настройки окружения (например, контейнеров или тестовых баз данных).
- **Инструменты**: `pytest`, `docker-compose` для создания тестового окружения.

### 3. **Энд-то-энд тесты (End-to-End, UI Tests)**
- **Описание**: Тестируют всю систему целиком — от ввода данных до получения результата, включая пользовательский интерфейс (UI).
- **Цель**: Убедиться, что приложение работает в реальных условиях, как ожидается.
- **Примеры**:
  - Проверка, что пользователь может оформить заказ в интернет-магазине.
  - Проверка работы аутентификации и авторизации.
- **Особенности**:
  - Самые медленные.
  - Трудозатратны в написании и поддержке.
  - Уязвимы к изменениям в интерфейсе или окружении.
- **Инструменты**: Selenium, Playwright, Cypress.

---

## Пропорции в пирамиде

- **Юнит-тесты**: Должны составлять **большую часть** (70-80%) всех тестов.
  - Они быстрые, дешёвые и дают уверенность в корректности отдельных частей кода.
- **Интеграционные тесты**: Около **15-20%**.
  - Их меньше, так как они сложнее и медленнее.
- **Энд-то-энд тесты**: Около **5-10%**.
  - Они покрывают только критически важные сценарии (например, оформление заказа или вход в систему).

---

## Расширенные подходы к пирамиде

1. **Песочные часы тестирования**:
   - Иногда интеграционные тесты занимают больше времени, чем юнит-тесты. Это характерно для микросервисной архитектуры, где взаимодействие между сервисами — ключевой аспект.

2. **Противоположность пирамиде — "Конус мороженого"**:
   - Возникает, если слишком много E2E-тестов и мало юнит- или интеграционных тестов.
   - Такой подход неэффективен из-за сложности поддержки, высокой стоимости и медленного выполнения.

---

## Пример построения пирамиды тестов

### Приложение: Интернет-магазин.

1. **Юнит-тесты**:
   - Проверка функции расчёта скидки.
   - Проверка метода формирования заказа.
   - Тестирование валидации данных при добавлении товара в корзину.

2. **Интеграционные тесты**:
   - Тестирование взаимодействия с базой данных: сохранение заказа, получение списка товаров.
   - Проверка взаимодействия между микросервисом корзины и микросервисом платежей.

3. **Энд-то-энд тесты**:
   - Проверка сценария оформления заказа через веб-интерфейс.
   - Тестирование процесса авторизации и регистрации пользователя.

---

## Советы по использованию пирамиды тестов

1. **Фокусируйтесь на юнит-тестах**:
   - Они должны покрывать большую часть логики приложения.
2. **Интеграционные тесты нужны там, где есть взаимодействие**:
   - Например, проверка работы API или баз данных.
3. **Минимизируйте E2E-тесты**:
   - Используйте их только для ключевых пользовательских сценариев.
4. **Автоматизируйте всё**:
   - Запускайте тесты при каждом изменении кода (CI/CD).

---

**Пирамида тестов** помогает организовать тестирование так, чтобы оно было быстрым, надёжным и эффективным. Правильное использование этого подхода позволяет обнаруживать ошибки на ранних этапах и снижать затраты на их исправление.

# Градация тестов: аспекты и уровни
Тесты можно разделить на уровни или аспекты, исходя из их назначения и контекста проверки. Это часть более широкой концепции пирамиды тестирования, которая помогает организовать тесты для достижения максимального покрытия и эффективности.

На примере `DataBaseFetcher` (Class to connect to a SQLite database, check database availability, and verify table existence)

#### 1. **Тесты функциональности (Unit Tests)**  
   - **Что проверяют:** внутреннюю корректность кода на уровне отдельных функций или классов.  
   - **Пример:** Для `DataBaseFetcher` это может быть тест, который проверяет, что метод корректно формирует SQL-запрос или выбрасывает исключение при некорректных параметрах.
   - **Подход:** часто используют **мокирование** внешних зависимостей (например, подключение к базе данных), чтобы изолировать тестируемый код.  
   - **Инструменты:** `unittest.mock`, `pytest-mock`.

#### 2. **Интеграционные тесты (Integration Tests)**  
   - **Что проверяют:** взаимодействие между компонентами, например, как ваш `DataBaseFetcher` работает с реальной базой данных.  
   - **Пример:** Тест на проверку подключения к конкретной базе данных, наличие таблицы, корректность структуры.  
   - **Подход:** работают с реальным окружением (база данных, файлы), но изолированы от внешних систем.  
   - **Особенности:** здесь важно поддерживать чистоту данных и предусматривать восстановление состояния после выполнения тестов.

#### 3. **Тесты окружения (Environment Tests)**  
   - **Что проверяют:** корректность работы программы в конкретной среде или с определённой конфигурацией.  
   - **Пример:** Проверка того, что приложение корректно работает с конкретной версией базы данных или с определёнными настройками конфигурационного файла.  

#### 4. **Тесты пользовательских сценариев (End-to-End Tests)**  
   - **Что проверяют:** полную цепочку работы приложения, имитируя действия пользователя.  
   - **Пример:** Проверка работы интерфейса приложения, которое использует `DataBaseFetcher` для извлечения данных и отображения их на веб-странице.  
   - **Подход:** такие тесты сложнее и медленнее, но полезны для проверки взаимодействия всех компонентов системы.

#### 5. **Тесты на производительность (Performance Tests)**  
   - **Что проверяют:** скорость выполнения кода, использование ресурсов (памяти, процессора).  
   - **Пример:** Проверить, что запросы, выполняемые через `DataBaseFetcher`, выполняются в разумное время.  

#### 6. **Тесты безопасности (Security Tests)**  
   - **Что проверяют:** уязвимости в коде и механизмы предотвращения атак.  
   - **Пример:** Проверка, что `DataBaseFetcher` защищён от SQL-инъекций.  

---


- **Изолированные тесты**: когда внешние зависимости заменяются моком (например, мокирование базы данных).  
- **Тесты с реальным окружением**: когда взаимодействие происходит с реальной базой или системой.  

---

### Какие ещё аспекты тестирования существуют?

1. **Тесты границ (Boundary Testing):** проверяют пограничные значения (минимальные/максимальные входные данные).  
2. **Тесты на регрессию (Regression Tests):** проверяют, что изменения в коде не ломают старый функционал.  
3. **Тесты на исключения (Negative Testing):** проверяют, как система реагирует на некорректные данные.  
4. **Тесты совместимости (Compatibility Testing):** проверяют работу приложения в разных средах (операционные системы, версии библиотек).  
5. **Smoke Tests:** быстрые тесты для проверки базовой работоспособности приложения после изменений.  
6. **Тесты на отказоустойчивость (Failover Testing):** проверяют поведение системы при сбоях (например, отключение базы).  

---

### Итог
Уровни тестирования помогают структурировать процесс проверки и изолировать проблемы на ранних этапах разработки. Каждый уровень играет свою роль, и их грамотное сочетание создаёт надёжную систему тестирования.



# Запуск тестов
Шаги для запуска тестов `unittest`, из корневой директории проекта (например, `app/src`).
1. Структура папок: Убедитесь, что структура папок выглядит (например) так:
```css
app/
├── src/
│   ├── datahub/
│   │   └── fetcher.py
│   └── tests/
│       └── test_fetcher.py
```
2. Создайте тесты в `test_fetcher.py`: Убедитесь, что ваши тесты в `test_fetcher.py` написаны с использованием стандартной библиотеки `unittest`. Например:
```python
import unittest
from datahub.fetcher import DataBaseFetcher  # Путь импорта должен быть правильным

class TestDataBaseFetcher(unittest.TestCase):

    def test_connection(self):
        db_fetcher = DataBaseFetcher(db_name='test_db.sqlite', db_table='test_table')
        self.assertTrue(db_fetcher.check_db_connection())

if __name__ == '__main__':
    unittest.main()
```

3. Запуск тестов: Чтобы запустить тесты из корневой директории `app/src`, используйте следующую команду в терминале:
```bash
python -m unittest discover -s tests -p "test_*.py"
```
- `-m unittest discover` указывает Python использовать модуль `unittest` для обнаружения тестов.
- `-s tests` указывает папку, где находятся тесты.
- `-p "test_*.py"` задает шаблон для имен файлов тестов (в данном случае, любые файлы, начинающиеся с `test_`).

# Пример мок-теста для коннектора к бд
## fetcher
```python
# fetcher.py
import os
import sqlite3

class DataBaseFetcher:
    """
    Class to connect to a SQLite database, check database availability, and verify table existence.

    Attributes:
    ----------
    db_path : str
        Path to the SQLite database, derived from the DB_PATH environment variable or the db_name parameter.
    db_table : str
        Name of the database table, derived from the DB_TABLE environment variable or the db_table parameter.
    conn : sqlite3.Connection
        Database connection, established when connect() is called.
    """

    def __init__(self, db_name=None, db_table=None):
        """
        Initializes DataFetcher with database path and table name.

        Parameters:
        ----------
        db_name : str, optional
            Database file name. If not specified, defaults to the DB_PATH environment variable or '/database/brtn.sqlite'.
        db_table : str, optional
            Name of the database table. If not specified, defaults to the DB_TABLE environment variable or 'default_table'.
        """
        db_folder_path = os.getenv("DB_PATH")
        db_file_name = db_name or os.getenv("DB_NAME")

        if db_folder_path and db_file_name:
            self.db_path = os.path.join(db_folder_path, db_file_name)
        else:
            self.db_path = None
        self.db_table = db_table or os.getenv("DB_TABLE")
        self.conn = None

    def connect(self):
        """
        Establishes a connection to the database.
        """
        if not self.db_path:
            raise ValueError("Database path is not set. Please provide a valid database path.")

        try:
            self.conn = sqlite3.connect(self.db_path)
            print(f"Connection established to database at: {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.conn:
            self.conn.close()
            print("Connection closed.")

    def check_connection_closed(self):
        """
        Checks if the database connection is closed by attempting to open a cursor.
        If the connection is closed, a ProgrammingError is raised.
        """
        try:
            self.conn.cursor()  # Attempt to open a cursor on a closed connection
            print("Connection is still open.")
        except sqlite3.ProgrammingError:
            print("Connection is closed successfully.")

    def check_db_connection(self):
        """
        Checks the database accessibility by attempting to connect to it.
        
        Returns:
        ----------
        bool
            True if the database is accessible, False otherwise.
        """
        try:
            self.connect()
            self.close_connection()
            print("Database is accessible.")
            return True
        except sqlite3.Error:
            print("Database is not accessible.")
            return False

    def check_table_availability(self):
        """
        Checks if the specified table exists and is accessible in the database.

        Returns:
        ----------
        bool
            True if the table is accessible, False otherwise.
        """
        if not self.db_table:
            raise ValueError("Table name is not set. Please provide a valid table name.")
        self.connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT 1 FROM {self.db_table} LIMIT 1;")
            print(f"Table '{self.db_table}' is available.")
            return True
        except sqlite3.Error:
            print(f"Table '{self.db_table}' is not available.")
            return False
        finally:
            self.close_connection()
```

## test
```python
import os
import unittest
from unittest.mock import patch, MagicMock
from datahub.fetcher import DataBaseFetcher

class TestDataBaseFetcher(unittest.TestCase):
    
    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.db'})
    def test_connect_success(self, mock_connect):
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        db_fetcher.connect()
        mock_connect.assert_called_once_with(db_fetcher.db_path)
        self.assertIsNotNone(db_fetcher.conn)

    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.db'})
    def test_connect_failure(self, mock_connect):
        mock_connect.side_effect = Exception("Connection error")
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        db_fetcher.connect()
        self.assertIsNone(db_fetcher.conn)

    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.db'})
    def test_close_connection(self, mock_connect):
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        db_fetcher.connect()
        db_fetcher.close_connection()
        mock_connect.return_value.close.assert_called_once()

    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.db'})
    def test_check_db_connection_success(self, mock_connect):
        mock_connect.return_value = MagicMock()
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        self.assertTrue(db_fetcher.check_db_connection())
        mock_connect.assert_called_once()

    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.db'})
    def test_check_db_connection_failure(self, mock_connect):
        mock_connect.side_effect = sqlite3.Error("Database not accessible")
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        self.assertFalse(db_fetcher.check_db_connection())

    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.db'})
    def test_check_table_availability_success(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = None
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        db_fetcher.connect()
        self.assertTrue(db_fetcher.check_table_availability())
        mock_cursor.execute.assert_called_once_with("SELECT 1 FROM test_table LIMIT 1;")

    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.db'})
    def test_check_table_availability_failure(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = sqlite3.Error("Table not found")
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        db_fetcher.connect()
        self.assertFalse(db_fetcher.check_table_availability())

    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.db'})
    def test_check_connection_closed(self, mock_connect):
        mock_connect.return_value.cursor.side_effect = sqlite3.ProgrammingError("Connection is closed")
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        db_fetcher.connect()
        db_fetcher.close_connection()
        
        with self.assertRaises(sqlite3.ProgrammingError):
            db_fetcher.check_connection_closed()

if __name__ == '__main__':
    unittest.main()
```

# Описание работы теста
В этом примере создаётся тестовый класс `TestDataBaseFetcher`, который наследуется от `unittest.TestCase`. Класс используется для тестирования функциональности класса `DataBaseFetcher` с помощью модуля `unittest` и библиотеки `unittest.mock`, которая позволяет заменять реальные зависимости мок-объектами. Основной тестовый метод `test_connect_success` проверяет, что метод connect класса `DataBaseFetcher` правильно вызывает функцию `sqlite3.connect` и устанавливает соединение с базой данных.

Рассмотрим работу кода по шагам.
## 1. Создание тестового класса

```python
class TestDataBaseFetcher(unittest.TestCase):
```
Класс `TestDataBaseFetcher` наследуется от `unittest.TestCase`, что позволяет ему использовать встроенные методы и функциональность `unittest`.` unittest.TestCase` предоставляет множество методов для проверки различных условий, таких как `assertIsNotNone`, `assertEqual`, `assertTrue`, и другие.

## 2. Использование декоратора `@patch`
```python
@patch('datahub.fetcher.sqlite3.connect')  # Изменено здесь
```
Декоратор `@patch` заменяет функцию или объект `sqlite3.connect` на мок-объект (имитацию), чтобы изолировать тестируемый код и исключить реальные вызовы к SQLite.

Декоратор `@patch` перехватывает любые вызовы к `sqlite3.connect` и вместо этого направляет их на `mock_connect`, который передаётся как аргумент в `test_connect_success`. Мок-объект позволяет контролировать и проверять взаимодействие с `sqlite3.connect` без реального подключения к базе данных.

Аргумент `mock_connect` создаётся автоматически благодаря декоратору `@patch`. Когда вы используете `@patch('datahub.fetcher.sqlite3.connect')`, `unittest.mock` перехватывает вызов `sqlite3.connect` и заменяет его на мок-объект. Этот мок-объект передаётся в тестовую функцию как аргумент — в данном случае `mock_connect`.

## 3. Определение метода `test_connect_success`
```python
def test_connect_success(self, mock_connect):
```
Метод `test_connect_success` — это тестовый метод, начинающийся с `test_`, чтобы `unittest` автоматически обнаружил его и выполнил как тест.

## 4. Создание экземпляра `DataBaseFetcher`
```python
db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
```
Внутри метода создаётся объект `DataBaseFetcher`, передавая ему тестовые значения для имени базы данных и таблицы.

## 5. Вызов `connect()` и проверка вызова
```python
db_fetcher.connect()
```
Затем вызывается метод connect у `db_fetcher`. Поскольку `sqlite3.connect` замокирован с помощью `@patch`, реального подключения не происходит, и все вызовы направляются на `mock_connect`.

После этого проверяется, был ли `mock_connect` вызван с ожидаемым аргументом `db_fetcher.db_path` — это предполагаемый путь к базе данных. Метод `assert_called_once_with` удостоверяется, что `sqlite3.connect` был вызван только один раз и с правильным аргументом.
```python
mock_connect.assert_called_once_with(db_fetcher.db_path)
```

## 6. Проверка, что соединение установлено
```python
self.assertIsNotNone(db_fetcher.conn)
```
Метод `assertIsNotNone` проверяет, что атрибут conn объекта `db_fetcher` не равен `None`, что указывает на успешное подключение (пусть и в виде мок-объекта).

# Объяснение работы `@patch`

- Замена целевой функции: Декоратор `@patch` принимает строку `'datahub.fetcher.sqlite3.connect'`, которая указывает путь к целевой функции, которую нужно заменить. В этом случае это функция `sqlite3.connect`, используемая в модуле `datahub.fetcher`.

- Создание мок-объекта: Декоратор `@patch` создаёт мок-объект для указанной функции, заменяя оригинальную функцию на время выполнения теста. Этот мок-объект перехватывает все вызовы к `sqlite3.connect`.

- Автоматическая передача мок-объекта как аргумента: `unittest.mock` автоматически передаёт созданный мок-объект в тестовую функцию в качестве аргумента. Имя аргумента (`mock_connect`) можно выбрать любое, но обычно оно совпадает с названием замещаемой функции для удобства чтения кода.

# Мокированные или реальные значения аргументов
```python
db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
```

Для успешного выполнения теста значения `db_name` и `db_table` не обязаны быть реальными или существующими, если вы используете `@patch` для замены методов, которые обращаются к реальной базе данных.  
Почему это работает с любыми значениями?

При использовании `@patch('datahub.fetcher.sqlite3.connect')`:  

Вы заменяете реальный метод `sqlite3.connect` мок-объектом, созданным `unittest.mock`.  
Этот мок-объект позволяет тесту выполняться без подключения к реальной базе данных, поскольку все вызовы `sqlite3.connect` перехватываются мок-объектом `mock_connect`.  
Тест проверяет только то, что метод `connect` был вызван с нужным аргументом (например, `db_fetcher.db_path`), и может выполнять другие проверки, не зависящие от существования базы данных.

Когда нужны реальные значения?

Реальные значения для `db_name` и `db_table` потребуются, если:  
- Вы не используете `@patch`, и функция действительно пытается подключиться к базе данных.  
- Вам нужно протестировать взаимодействие с реальной базой данных, например, если вы хотите провести интеграционные тесты, проверяющие фактические операции чтения и записи.

Для обычных юнит-тестов, изолированных от реальных внешних ресурсов, вы можете использовать любые фиктивные значения, такие как `'test.db'` и `'test_table'`.

# Случаи использования `@patch`
Декоратор `@patch` из библиотеки `unittest.mock` широко применяется для изоляции кода от внешних зависимостей, позволяя заменить реальные объекты их имитациями (mock-объектами). Вот несколько основных случаев его использования:  
1. Изоляция от внешних ресурсов  
`@patch` применяется, чтобы тест не зависел от реальных баз данных, файловой системы, сетевых подключений или API, к которым обращается тестируемый код. 

```python
@patch('module.external_api.call')
def test_api_call(self, mock_call):
    mock_call.return_value = {"status": "ok"}
    # тестируем код, который вызывает external_api.call
```

Вместо реального вызова `external_api.call` тест использует мок-объект `mock_call`, что позволяет контролировать его поведение и результаты.

2. Тестирование логики независимо от времени и случайностей  
Используется для изоляции от таких зависимостей, как случайные значения и дата-время. Это позволяет проверять поведение без случайных факторов:
```python
@patch('module.random.randint', return_value=5)
def test_random_behavior(self, mock_randint):
    # здесь random.randint всегда вернет 5
```

3. Имитирование поведения недоступных компонентов  
Удобно, когда в проекте тестируемый код взаимодействует с модулями или сервисами, которые находятся в разработке или недоступны. Моки позволяют имитировать поведение недоступного компонента.

4. Повышение производительности тестов  
Снижение времени выполнения тестов за счет предотвращения реальных вызовов, например к базе данных или удаленному API, что делает тесты более быстрыми и отзывчивыми.

5. Проверка взаимодействий и вызовов  
`@patch` позволяет проверять, как часто и с какими параметрами вызывается метод, проверяя корректность взаимодействия между компонентами:
```python
@patch('module.external_service.send_email')
def test_email_sending(self, mock_send_email):
    # тестируем код, который вызывает send_email
    mock_send_email.assert_called_once_with('user@example.com')
```

6. Подмена системных и встроенных методов  
Может быть использован для подмены стандартных библиотек, например, `open`, `os.environ` или `time.sleep`, для контроля над поведением системы:
```python
@patch('time.sleep', return_value=None)
def test_without_sleep(self, mock_sleep):
    # тестируем код, который использует time.sleep, без фактической задержки
```

7. Изоляция состояния  
`@patch` позволяет изолировать состояние и сохранять чистую среду выполнения для каждого теста. Это полезно для избежания побочных эффектов между тестами, например, когда состояние объекта должно быть всегда начальным.

Основные варианты использования `@patch`:

- В качестве декоратора тестового метода: `@patch('module.function')`
- Внутри тестового метода через `with: with patch('module.function') as mock_function`
- В аргументах декоратора `@patch.multiple` для нескольких объектов одновременно.

`@patch` делает тесты более предсказуемыми, быстрыми и независимыми от состояния внешних ресурсов, повышая их надёжность и гибкость.

# Подмена значений переменных окружения `os.environ`

Декоратор `@patch.dict(os.environ, {...})` из модуля `unittest.mock` используется для временной подмены значений переменных окружения `os.environ` на время выполнения теста. Вот как это работает более подробно:

Создание временного окружения: Когда используется `@patch.dict(os.environ, {...})`, Python берет текущие значения переменных окружения (из `os.environ`) и временно заменяет их на значения, указанные в словаре внутри `patch.dict`. Эти изменения применяются только в пределах области действия декорированной функции.

Использование подмененных значений: В нашем случае мы заменяем переменные окружения `DB_PATH` и `DB_NAME` значениями `'/test/path'` и `'test.db'`. Это значит, что внутри функции `test_connect_success`, вызовы к `os.getenv('DB_PATH')` и `os.getenv('DB_NAME')` вернут эти тестовые значения. Такой подход особенно удобен, если код, который мы тестируем, зависит от переменных окружения.

Автоматическое восстановление значений: Когда выполнение функции завершается (или тест заканчивается), `@patch.dict` автоматически возвращает переменные окружения к их исходным значениям. Это гарантирует, что изменения не повлияют на другие тесты или части кода.

# Тест неудачной попытки соединения с базой данных
Тест `test_connect_failure` направлен на проверку того, как метод `connect` обрабатывает исключение при неудачной попытке соединения с базой данных. Цель этого теста — удостовериться, что:

- Исключение, вызванное `mock_connect.side_effect`, перехватывается методом `connect`, и метод корректно обрабатывает ситуацию.
- После обработки исключения атрибут `self.conn` остается `None`, что подтверждает отсутствие установленного соединения.

Вместо реального подключения, `mock_connect.side_effect = Exception("Connection error")` подменяет `sqlite3.connect` и вызывает исключение. Метод `connect` должен "поймать" это исключение и установить `self.conn = None`, вместо того чтобы прерывать выполнение.  

Таким образом, тест `test_connect_failure проверяет`:
- Обработку исключений: Убедиться, что метод `connect` не завершает выполнение с ошибкой и не выбрасывает необработанное исключение.
- Корректность состояния: После исключения `self.conn` должно оставаться `None`, что указывает на отсутствие активного соединения.

Добавление обработки исключений в метод `connect` позволяет тесту успешно проверить, что код правильно обрабатывает ситуацию, когда соединение установить не удалось.

# Порядок вывода и обработки

`unittest` сначала выводит сообщение о тестах, а затем собирает и показывает результаты.  

В выводе `unittest`, каждая точка (`.`) представляет успешное выполнение одного теста. Первая точка (`.`) перед `"Connection established to database at: /test/path/test.db"` обозначает успешное завершение `test_connect_failure`, а затем второй тест (`test_connect_success`) выводит `"Connection established..."` и завершается точкой.  

## Как работает порядок выполнения тестов в unittest

`unittest` определяет порядок тестов, сортируя их названия в алфавитном порядке. Это значит, что тесты с названиями, начинающимися с символов, расположенных ближе к началу алфавита (например, `a`, `b`, и так далее), будут выполнены раньше.  

**Изменение порядка выполнения**
Если порядок выполнения тестов критичен, можно применить один из подходов:

- Переименовать тесты — изменить названия так, чтобы они шли в желаемом порядке, например, назвать первый тест `test_01_connect_failure`, а второй — `test_02_connect_success`.
- Использовать `TestSuite` — явным образом указать порядок тестов, добавив их в `TestSuite` в нужной последовательности.
- Плагин или ключ командной строки — например, с помощью библиотеки `pytest` можно задать порядок через параметры, такие как `--shuffle`, или использовать декораторы для упорядочивания выполнения тестов.

# Описание работы
Взято с pythonworld.ru

## Простой пример использования

В Python встроен модуль `unittest`, который поддерживает автоматизацию тестов, использование общего кода для настройки и завершения тестов, объединение тестов в группы, а также позволяет отделять тесты от фреймворка для вывода информации.

Для автоматизации тестов, unittest поддерживает некоторые важные концепции:

- Испытательный стенд (`test fixture`) - выполняется подготовка, необходимая для выполнения тестов и все необходимые действия для очистки после выполнения тестов. Это может включать, например, создание временных баз данных или запуск серверного процесса.
- Тестовый случай (`test case`) - минимальный блок тестирования. Он проверяет ответы для разных наборов данных. Модуль unittest предоставляет базовый класс `TestCase`, который можно использовать для создания новых тестовых случаев.
- Набор тестов (`test suite`) - несколько тестовых случаев, наборов тестов или и того и другого. Он используется для объединения тестов, которые должны быть выполнены вместе.
- Исполнитель тестов (`test runner`) - компонент, который управляет выполнением тестов и предоставляет пользователю результат. Исполнитель может использовать графический или текстовый интерфейс или возвращать специальное значение, которое сообщает о результатах выполнения тестов.

Модуль unittest предоставляет богатый набор инструментов для написания и запуска тестов. Однако достаточно лишь некоторых из них, чтобы удовлетворить потребности большинства пользователей.

Вот короткий скрипт для тестирования трех методов строк:
```python
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
```
Тестовый случай создаётся путём наследования от `unittest.TestCase`. 3 отдельных теста определяются с помощью методов, имя которых начинается на `test_`. Это соглашение говорит исполнителю тестов о том, какие методы являются тестами.

Суть каждого теста - вызов `assertEqual()` для проверки ожидаемого результата; `assertTrue()` или `assertFalse()` для проверки условия; `assertRaises()` для проверки, что метод порождает исключение. Эти методы используются вместо обычного `assert` для того, чтобы исполнитель тестов смог взять все результаты и оформить отчёт.

Методы `setUp()` и `tearDown()` (которые в данном простом случае не нужны) позволяют определять инструкции, выполняемые перед и после каждого теста, соответственно.

Последние 2 строки показывают простой способ запуска тестов. `unittest.main()` предоставляет интерфейс командной строки для тестирования программы. Будучи запущенным из командной строки, этот скрипт выводит отчёт, подобный этому:
```bash
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
## Интерфейс командной строки
unittest может быть использован из командной строки для запуска модулей с тестами, классов или даже отдельных методов:

```bash
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```
Можно также указывать путь к файлу:
```bash
python -m unittest tests/test_something.py
```
С помощью флага -v можно получить более детальный отчёт:
```bash
python -m unittest -v test_module
```
Для нашего примера подробный отчёт будет таким:
```bash
test_isupper (__main__.TestStringMethods) ... ok
test_split (__main__.TestStringMethods) ... ok
test_upper (__main__.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
**-b (--buffer)** - вывод программы при провале теста будет показан, а не скрыт, как обычно.

**-c (--catch)** - `Ctrl+C` во время выполнения теста ожидает завершения текущего теста и затем сообщает результаты на данный момент. Второе нажатие `Ctrl+C` вызывает обычное исключение `KeyboardInterrupt`.

**-f (--failfast)** - выход после первого же неудачного теста.

**--locals** (начиная с Python 3.5) - показывать локальные переменные для провалившихся тестов.

## Обнаружение тестов
unittest поддерживает простое обнаружение тестов. Для совместимости с обнаружением тестов, все файлы тестов должны быть модулями или пакетами, импортируемыми из директории верхнего уровня проекта

Обнаружение тестов реализовано в `TestLoader.discover()`, но может быть использовано из командной строки:
```bash
cd project_directory
python -m unittest discover
```
**-v (--verbose)** - подробный вывод.

**-s (--start-directory) directory_name** - директория начала обнаружения тестов (текущая по умолчанию).

***-p (--pattern) pattern*** - шаблон названия файлов с тестами (по умолчанию test*.py).

**-t (--top-level-directory) directory_name** - директория верхнего уровня проекта (по умолчанию равна start-directory).

## Организация тестового кода
Базовые блоки тестирования это тестовые случаи - простые случаи, которые должны быть проверены на корректность.

Тестовый случай создаётся путём наследования от `unittest.TestCase`.

Тестирующий код должен быть самостоятельным, то есть никак не зависеть от других тестов.

Простейший подкласс `TestCase` может просто реализовывать тестовый метод (метод, начинающийся с `test`). Вымышленный пример:
```python
import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))
```
Заметьте, что для того, чтобы проверить что-то, мы используем один из `assert\*()` методов.

Тестов может быть много, и часть кода настройки может повторяться. К счастью, мы можем определить код настройки путём реализации метода `setUp()`, который будет запускаться перед каждым тестом:
```python
import unittest

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
```
Мы также можем определить метод `tearDown()`, который будет запускаться после каждого теста:
```python
import unittest

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
```
Можно разместить все тесты в том же файле, что и сама программа (таком как `widgets.py`), но размещение тестов в отдельном файле (таком как `test_widget.py`) имеет много преимуществ:

- Модуль с тестом может быть запущен автономно из командной строки.  
- Тестовый код может быть легко отделён от программы.  
- Меньше искушения изменить тесты для соответствия коду программы без видимой причины.  
- Тестовый код должен изменяться гораздо реже, чем программа.  
- Протестированный код может быть легче переработан.  
- Тесты для модулей на C должны быть в отдельных модулях, так почему же не быть последовательным?  
- Если стратегия тестирования изменяется, нет необходимости изменения кода программы.

## Пропуск тестов и ожидаемые ошибки
`unittest` поддерживает пропуск отдельных тестов, а также классов тестов. Вдобавок, поддерживается пометка теста как "не работает, но так и надо".

Пропуск теста осуществляется использованием декоратора `skip()` или одного из его условных вариантов.
```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
```
```bash
test_format (__main__.MyTestCase) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase) ... skipped 'demonstrating skipping'
test_windows_support (__main__.MyTestCase) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK (skipped=3)
```
Классы также могут быть пропущены:
```python
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```
Ожидаемые ошибки используют декоратор expectedFailure():
```python
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```
Очень просто сделать свой декоратор. Например, следующий декоратор пропускает тест, если переданный объект не имеет указанного атрибута:
```python
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))
```
Декораторы, пропускающие тесты или говорящие об ожидаемых ошибках:

`@unittest.skip(reason)` - пропустить тест. reason описывает причину пропуска.  
`@unittest.skipIf(condition, reason)` - пропустить тест, если condition истинно.  
`@unittest.skipUnless(condition, reason)` - пропустить тест, если condition ложно.  
`@unittest.expectedFailure` - пометить тест как ожидаемая ошибка.  

Для пропущенных тестов не запускаются `setUp()` и `tearDown()`. Для пропущенных классов не запускаются `setUpClass()` и `tearDownClass()`. Для пропущенных модулей не запускаются `setUpModule()` и `tearDownModule()`.

## Различение итераций теста с помощью подтестов
Когда некоторые тесты имеют лишь незначительные отличия, например некоторые параметры, `unittest` позволяет различать их внутри одного тестового метода, используя менеджер контекста `subTest()`.

Например, следующий тест:
```python
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```
даст следующий отчёт:
```bash
======================================================================
FAIL: test_even (__main__.NumbersTest) (i=1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest) (i=3)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest) (i=5)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0
```
Без использования подтестов, выполнение будет остановлено после первой ошибки, и ошибку будет сложнее диагностировать, потому что значение `i` не будет показано:
```bash
======================================================================
FAIL: test_even (__main__.NumbersTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0
```

## Проверки на успешность
Модуль `unittest` предоставляет множество функций для самых различных проверок:

**`assertEqual(a, b)`** — `a == b`  
**`assertNotEqual(a, b)`** — `a != b`  
**`assertTrue(x)`** — `bool(x) is True`  
**`assertFalse(x)`** — `bool(x) is False`  
**`assertIs(a, b)`** — `a is b`  
**`assertIsNot(a, b)`** — `a is not b`  
**`assertIsNone(x)`** — x is None  
**`assertIsNotNone(x)`** — x is not None  
**`assertIn(a, b)`** — a in b  
**`assertNotIn(a, b)`** — a not in b  
**`assertIsInstance(a, b)`** — isinstance(a, b)  
**`assertNotIsInstance(a, b)`** — not isinstance(a, b)  
**`assertRaises(exc, fun, *args, **kwds) — fun(*args, **kwds)`** порождает исключение `exc`  
**`assertRaisesRegex(exc, r, fun, *args, **kwds) — fun(*args, **kwds)`** порождает исключение exc и сообщение соответствует регулярному выражению `r`  
**`assertWarns(warn, fun, *args, **kwds) — fun(*args, **kwds)`** порождает предупреждение  
**`assertWarnsRegex(warn, r, fun, *args, **kwds) — fun(*args, **kwds)`** порождает предупреждение и сообщение соответствует регулярному выражению `r`  
**`assertAlmostEqual(a, b)`** — round(a-b, 7) == 0  
**`assertNotAlmostEqual(a, b)`** — round(a-b, 7) != 0  
**`assertGreater(a, b)`** — a > b  
**`assertGreaterEqual(a, b)`** — a >= b  
**`assertLess(a, b)`** — a < b  
**`assertLessEqual(a, b)`** — a <= b  
**`assertRegex(s, r)`** — r.search(s)  
**`assertNotRegex(s, r)`** — not r.search(s)  
**`assertCountEqual(a, b)`** — a и b содержат те же элементы в одинаковых количествах, но порядок не важен

# Конфигурационные объекты и фикстуры в unittest
**Фикстуры (fixtures)** — это преднастроенные объекты, которые создаются перед тестами и очищаются после их выполнения. Они необходимы для подготовки окружения, разделяемого между тестами, чтобы обеспечить их предсказуемость и независимость.
Зачем нужны фикстуры?

    Подготовка данных и объектов для тестов:
        Создание объектов, которые тестируемый код будет использовать.
        Инициализация баз данных, файловых систем или внешних зависимостей.

    Гарантия изоляции тестов:
        Каждый тест запускается с "чистым листом".
        Состояние окружения не влияет на результаты тестов.

    Уменьшение дублирования:
        Код подготовки выносится в отдельные методы, исключая повторение в каждом тесте.

    Упрощение отладки:
        Фикстуры позволяют легко воспроизводить окружение для одного теста.

## **Фикстуры в unittest**

Модуль unittest предоставляет несколько механизмов для работы с фикстурами:

    Методы уровня модуля:
        `setUpModule` / `tearDownModule`: выполняются один раз для всего модуля
    Методы уровня класса:
        `setUpClass` / `tearDownClass`: выполняются один раз для всех тестов в классе.
    Методы уровня теста:
        `setUp` / `tearDown`: выполняются перед и после каждого теста.
    Ручное управление:
        Использование контекстных менеджеров или вручную написанных методов для более сложных сценариев.

## Возможные варианты использования фикстур
### 1. Инициализация простых объектов

Подготовка объектов, используемых в тестах.
```python
import unittest

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5

    def test_addition(self):
        self.assertEqual(self.a + self.b, 15)

    def test_subtraction(self):
        self.assertEqual(self.a - self.b, 5)

    def tearDown(self):
        # Очистка или логирование (если требуется)
        pass

if __name__ == "__main__":
    unittest.main()
```
### 2. Подготовка ресурсов (например, базы данных)

Создание временной базы данных, таблиц, загрузка данных.
```python
import unittest
import sqlite3

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Создаём базу данных и подключение
        cls.connection = sqlite3.connect(":memory:")
        cls.cursor = cls.connection.cursor()
        cls.cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")

    def setUp(self):
        # Загружаем данные для каждого теста
        self.cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
        self.cursor.execute("INSERT INTO users VALUES (2, 'Bob')")
        self.connection.commit()

    def test_user_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM users")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 2)

    def test_user_names(self):
        self.cursor.execute("SELECT name FROM users WHERE id = 1")
        name = self.cursor.fetchone()[0]
        self.assertEqual(name, 'Alice')

    def tearDown(self):
        # Очищаем таблицу после каждого теста
        self.cursor.execute("DELETE FROM users")
        self.connection.commit()

    @classmethod
    def tearDownClass(cls):
        # Закрываем подключение после всех тестов
        cls.connection.close()

if __name__ == "__main__":
    unittest.main()
```
### 3. Тестирование файловой системы

Создание временных файлов перед тестами.
```python
import unittest
import os

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # Создаём временный файл
        self.test_file = "test.txt"
        with open(self.test_file, 'w') as f:
            f.write("Hello, World!")

    def test_file_read(self):
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, "Hello, World!")

    def tearDown(self):
        # Удаляем временный файл
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()
```
### 4. Использование внешних зависимостей (например, API)

Для интеграционного тестирования или мокирования.
```python
import unittest
from unittest.mock import patch

class TestExternalAPI(unittest.TestCase):
    @patch("requests.get")
    def test_api_response(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"message": "success"}

        response = mock_get("http://example.com/api")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "success")

if __name__ == "__main__":
    unittest.main()
```
**Почему нельзя без фикстур?**

    Дублирование кода:
        Без фикстур каждый тест будет повторять одни и те же подготовительные операции.

    Неизолированные тесты:
        Если тесты работают с общими ресурсами (например, файл, база данных), их результаты могут влиять друг на друга.

    Усложнённая отладка:
        Неподготовленное или нестабильное окружение затрудняет определение причин сбоя тестов.

    Повышенный риск ошибок:
        Без фикстур сложно обеспечить единообразное состояние для всех тестов.

Фикстуры обеспечивают надёжность и простоту тестирования, особенно при работе с разделяемыми ресурсами или сложными конфигурациями. Использование фикстур позволяет создавать независимые, изолированные тесты с минимальными усилиями.

## Изоляция тестов
Изоляция тестов (на примере выше работы с БД) обеспечивается за счёт использования фикстур `setUp` и `tearDown`, а также разделения ответственности между методами `setUpClass` и `tearDownClass`.

Давайте разберёмся, почему тесты в этом случае изолированы и как это достигается.  
Ключевые элементы изоляции тестов в примере

    **Разделение подготовки окружения:**
        `setUpClass`: Выполняется один раз для всего класса, создавая общий ресурс — базу данных в памяти (`sqlite3.connect(":memory:")`). Это экономит время, так как база создаётся лишь один раз для всех тестов.
        `setUp`: Выполняется перед каждым тестом, добавляя данные (`INSERT INTO users`). Таким образом, каждый тест запускается в идентичных условиях: база данных содержит ровно два пользователя.

    Очистка состояния после теста:
        `tearDown`: Выполняется после каждого теста, очищая таблицу от всех записей (`DELETE FROM users`). Это предотвращает влияние одного теста на другой, даже если предыдущий тест модифицировал данные.

    Ручное управление ресурсами:
        `tearDownClass`: Выполняется один раз после всех тестов, чтобы закрыть соединение с базой данных. Это освобождает ресурсы.

**Где видно, что тесты изолированы?**

    Инициализация данных: Каждый раз перед тестом база данных наполняется одинаковыми данными через `setUp`. Например, в обоих тестах:
```python
self.cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
self.cursor.execute("INSERT INTO users VALUES (2, 'Bob')")
```

Тесты никогда не "унаследуют" изменения в базе данных, сделанные другими тестами.

Очищение данных: После выполнения каждого теста таблица "users" очищается:

`self.cursor.execute("DELETE FROM users")`

Это гарантирует, что ни один тест не оставляет "мусора" в общем ресурсе.

Если убрать `tearDown` и не очищать таблицу после каждого теста, состояние базы данных будет сохраняться между тестами.  
**Что пойдёт не так:**

    Первый тест (`test_user_count`) выполняется успешно:
        В `setUp` добавляются две записи.
        Тест проверяет, что в таблице ровно 2 записи, и завершается.

    Второй тест (`test_user_names`) ломается:
        В `setUp` снова добавляются две записи.
        Таблица теперь содержит 4 записи (2 от предыдущего теста + 2 новых).
        Если тест ищет запись `id=1`, он найдёт её, но избыточные записи могут повлиять на логику теста.

**Почему это важно?**

    Предсказуемость результатов:
        Каждый тест проверяет именно тот сценарий, который описан в нём, а не поведение, зависимое от предыдущих тестов.

    Локализация ошибок:
        Если тест падает, можно быть уверенным, что ошибка связана именно с ним, а не с побочным эффектом другого теста.

    Масштабируемость:
        Изолированные тесты легко выполнять параллельно, поскольку они не зависят друг от друга.

Фикстуры, такие как `setUp` и `tearDown`, обеспечивают эту изоляцию.

## Фикстуры уровня модуля

Фикстуры уровня модуля в `unittest` необходимы, когда требуется подготовить или разделить общий ресурс, который используется всеми тестами из модуля, а не только из одного класса. Это позволяет экономить ресурсы и время, избегая многократного создания и удаления ресурса для каждого тестового класса или теста.

Примером может быть работа с временной базой данных, API-сервером, файлом или другими ресурсами, которые достаточно создать один раз для всех тестов модуля.
Пример: Использование фикстуры уровня модуля для базы данных  

Задача  
Пусть у нас есть набор тестов, которые проверяют работу с базой данных. Создавать базу для каждого класса или теста слишком дорого, так как структура базы и начальные данные одинаковы для всех тестов.  
Мы можем использовать фикстуры уровня модуля для создания и удаления базы один раз для всех тестов.

Реализация
```python
import unittest
import sqlite3

# Общий ресурс для модуля
db_connection = None
db_cursor = None

def setUpModule():
    """
    Создаётся общий ресурс для всего модуля — временная база данных.
    """
    global db_connection, db_cursor
    db_connection = sqlite3.connect(":memory:")
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, age INTEGER)")
    db_cursor.execute("INSERT INTO users VALUES (1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35)")
    db_connection.commit()
    print("setUpModule: База данных создана.")

def tearDownModule():
    """
    Удаляется общий ресурс после завершения всех тестов модуля.
    """
    global db_connection
    db_connection.close()
    print("tearDownModule: База данных закрыта.")

class TestUserQueries(unittest.TestCase):
    def test_user_count(self):
        db_cursor.execute("SELECT COUNT(*) FROM users")
        count = db_cursor.fetchone()[0]
        self.assertEqual(count, 3)

    def test_user_age(self):
        db_cursor.execute("SELECT age FROM users WHERE name = 'Bob'")
        age = db_cursor.fetchone()[0]
        self.assertEqual(age, 25)

class TestDatabaseModifications(unittest.TestCase):
    def test_add_user(self):
        db_cursor.execute("INSERT INTO users VALUES (4, 'Diana', 40)")
        db_connection.commit()
        db_cursor.execute("SELECT COUNT(*) FROM users")
        count = db_cursor.fetchone()[0]
        self.assertEqual(count, 4)

    def test_delete_user(self):
        db_cursor.execute("DELETE FROM users WHERE name = 'Alice'")
        db_connection.commit()
        db_cursor.execute("SELECT COUNT(*) FROM users")
        count = db_cursor.fetchone()[0]
        self.assertEqual(count, 2)

if __name__ == "__main__":
    unittest.main()
```
**Разбор кода**

    Фикстура уровня модуля:
        setUpModule создаёт ресурс (базу данных) один раз для всех тестов модуля.
        tearDownModule освобождает ресурс (закрывает базу данных) после выполнения всех тестов.

    Общий ресурс:
        Глобальные переменные `db_connection` и `db_cursor` используются всеми тестами.
        База данных создаётся только один раз, что экономит время.

    Изоляция тестов:
        Каждый тест может менять состояние базы данных, но это не проблема, так как структура базы данных задаётся в фикстуре модуля. В реальных сценариях вы могли бы откатить изменения после каждого теста с помощью фикстур класса (set`Up/`tearDown`).

    Экономия времени:
        Нет необходимости каждый раз пересоздавать базу данных для каждого класса или теста. Это важно, если ресурс сложный или создаётся долго.

**Когда фикстуры уровня модуля обязательны?**

    Ресурс сложный или тяжёлый для инициализации:
        Например, работа с API-сервером, подключение к облачным сервисам, настройка Docker-контейнеров.

    Общий ресурс для всего набора тестов:
        Например, база данных, конфигурация приложения или большой объём данных, который используется всеми тестами.

    Экономия ресурсов и времени:
        Если создание ресурса занимает значительное время, имеет смысл делать это один раз для всего модуля.

Если вы уберёте `setUpModule` и будете создавать базу в каждом классе через `setUpClass`, база данных будет создаваться несколько раз. Это приведёт к лишним затратам ресурсов и увеличению времени выполнения тестов.

# Декораторы unittest
В unittest доступны несколько полезных декораторов, которые помогают изменять поведение тестов или добавлять дополнительную информацию. Вот их

## список, назначение и примеры использования:

1. `@unittest.skip(reason)`

    Назначение: Пропустить тест с указанием причины.
    Пример использования:
    ```python
    import unittest

    class TestExample(unittest.TestCase):
        @unittest.skip("Этот тест пока не реализован")
        def test_placeholder(self):
            self.assertEqual(1, 1)
    ```
2. `@unittest.skipIf(condition, reason)`

    Назначение: Пропустить тест, если указанное условие выполняется.
    Пример использования:
    ```python
    import unittest
    import sys

    class TestExample(unittest.TestCase):
        @unittest.skipIf(sys.version_info < (3, 9), "Тест требует Python 3.9 или выше")
        def test_new_feature(self):
            self.assertTrue(True)
    ```

3. `@unittest.skipUnless(condition, reason)`

    Назначение: Пропустить тест, если условие не выполняется.
    Пример использования:
    ```python
    import unittest

    class TestExample(unittest.TestCase):
        @unittest.skipUnless(hasattr(str, "casefold"), "Тест требует метод 'casefold'")
        def test_casefold(self):
            self.assertEqual("ABC".casefold(), "abc")
    ```

4. `@unittest.expectedFailure`

    Назначение: Помечает тест как ожидаемо неуспешный. Если тест неудачен, это не будет считаться ошибкой. Если тест вдруг проходит, это будет отмечено как неожиданное событие.
    Пример использования:
    ```python
    import unittest

    class TestExample(unittest.TestCase):
        @unittest.expectedFailure
        def test_failing(self):
            self.assertEqual(1, 2)  # Ожидаем, что тест упадёт
    ```

5. `@unittest.mock.patch(target, new=None)`

    Назначение: Заменяет объект указанного модуля фиктивным значением или объектом.
    Пример использования:
    ```python
    import unittest
    from unittest.mock import patch

    class TestExample(unittest.TestCase):
        @patch("builtins.print")
        def test_mock_print(self, mock_print):
            print("Hello, World!")
            mock_print.assert_called_with("Hello, World!")
    ```

6. `@unittest.mock.patch.object(target, attribute, new=None)`

    Назначение: Изменяет атрибут объекта фиктивным значением.
    Пример использования:
    ```python
    import unittest
    from unittest.mock import patch

    class Foo:
        def bar(self):
            return "original"

    class TestExample(unittest.TestCase):
        @patch.object(Foo, "bar", return_value="mocked")
        def test_patch_object(self, mock_method):
            foo = Foo()
            self.assertEqual(foo.bar(), "mocked")
    ```

7. `@unittest.mock.patch.dict(dictionary, values, clear=False)`

    Назначение: Изменяет содержимое словаря в тесте, возвращая его в исходное состояние после выполнения теста.
    Пример использования:
    ```python
    import unittest
    from unittest.mock import patch

    class TestExample(unittest.TestCase):
        @patch.dict("os.environ", {"TEST_ENV": "mocked"})
        def test_env(self):
            import os
            self.assertEqual(os.environ["TEST_ENV"], "mocked")
    ```

8. `@unittest.mock.patch.multiple(target, **kwargs)`

    Назначение: Патчит несколько атрибутов объекта одновременно.
    Пример использования:
    ```python
    import unittest
    from unittest.mock import patch

    class Foo:
        attr1 = "original1"
        attr2 = "original2"

    class TestExample(unittest.TestCase):
        @patch.multiple(Foo, attr1="mocked1", attr2="mocked2")
        def test_patch_multiple(self):
            self.assertEqual(Foo.attr1, "mocked1")
            self.assertEqual(Foo.attr2, "mocked2")
    ```

9. `@unittest.expectedFailureIf(condition) (дополнительный подход)`

В некоторых версиях могут быть доступны кастомные реализации на основе паттернов для expectedFailure с условием.  

**Когда использовать:**

    Пропуски тестов (`@skip`, `@skipIf`, `@skipUnless`):
        Удобно для тестов, которые зависят от версии ПО, платформы или доступных ресурсов.

    Ожидаемые неудачи (`@expectedFailure`):
        Используйте для тестов, описывающих баги или функции, которые ещё не реализованы.

    Моки и патчи (`@patch`, `@patch.object`, `@patch.dict`):
        Используются для изоляции тестов от внешних зависимостей, таких как сторонние API, база данных или системные вызовы.

Общий подход к созданию кастомных декораторов- логика должна быть полезной и повторяемой. Если вы часто сталкиваетесь с похожими условиями пропуска, это обоснованный повод создать кастомный декоратор.

## переопределение декораторов `@skip`

Переопределение декораторов вроде `@unittest.skip` и создание кастомных вариантов часто полезно для обработки сложных или динамических условий пропуска тестов. Рассмотрим несколько кейсов, где обосновано создание таких кастомных декораторов.

### 1. Пропуск теста на основе конфигурации окружения

Если тест зависит от переменных среды (например, API_KEY или DEBUG_MODE), можно пропустить его, если переменная не задана.
```python
import os
import unittest

def skipUnlessEnvVarSet(var_name):
    if os.getenv(var_name):
        return lambda func: func
    return unittest.skip(f"Переменная окружения {var_name} не установлена")

class TestAPI(unittest.TestCase):
    @skipUnlessEnvVarSet("API_KEY")
    def test_api_call(self):
        # Тест выполняется только если API_KEY задан
        self.assertTrue(True)
```
### 2. Пропуск теста в зависимости от версии Python

Некоторые тесты могут работать только с определённой версией Python.
```python
import sys
import unittest

def skipUnlessPythonVersion(min_version):
    if sys.version_info >= min_version:
        return lambda func: func
    return unittest.skip(f"Тест требует Python >= {min_version}")

class TestPythonFeatures(unittest.TestCase):
    @skipUnlessPythonVersion((3, 8))
    def test_new_feature(self):
        # Тест выполняется только на Python 3.8+
        self.assertTrue(True)
```
### 3. Пропуск теста, если нет доступного ресурса

Например, если тест зависит от доступности определённого сервиса, порта или базы данных.
```python
import socket
import unittest

def skipUnlessPortOpen(host, port):
    def is_port_open():
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except OSError:
            return False

    if is_port_open():
        return lambda func: func
    return unittest.skip(f"Порт {port} на {host} недоступен")

class TestNetworkService(unittest.TestCase):
    @skipUnlessPortOpen("localhost", 8080)
    def test_service_running(self):
        # Тест выполняется только если порт открыт
        self.assertTrue(True)
```
### 4. Пропуск теста для неподдерживаемой платформы

Если тест работает только на определённой операционной системе (например, Windows или Linux), его можно пропустить для других платформ.
```python
import unittest
import platform

def skipUnlessPlatform(target_platform):
    if platform.system() == target_platform:
        return lambda func: func
    return unittest.skip(f"Тест поддерживается только на платформе {target_platform}")

class TestPlatformSpecific(unittest.TestCase):
    @skipUnlessPlatform("Windows")
    def test_windows_functionality(self):
        # Тест выполняется только на Windows
        self.assertTrue(True)
```
### 5. Пропуск теста при отсутствии определённого атрибута
Следующий декоратор пропускает тест, если переданный объект не имеет указанного атрибута:
```python
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))
```

### 6. Пропуск теста при наличии определённого атрибута

Подобно примеру с `@skipUnlessHasattr`, но наоборот: пропустить тест, если объект имеет определённый атрибут.
```python
def skipIfHasattr(obj, attr):
    if hasattr(obj, attr):
        return unittest.skip(f"{obj!r} имеет атрибут {attr!r}")
    return lambda func: func

class SomeClass:
    pass

class TestCustom(unittest.TestCase):
    obj = SomeClass()
    @skipIfHasattr(obj, "forbidden_attr")
    def test_no_forbidden_attr(self):
        self.assertTrue(True)
```

### 7. Пропуск теста на основе состояния объекта

Пропуск теста, если объект находится в определённом состоянии (например, база данных закрыта, сессия истекла).
```python
class Database:
    def __init__(self, is_connected=True):
        self.is_connected = is_connected

def skipUnlessConnected(database):
    if database.is_connected:
        return lambda func: func
    return unittest.skip("База данных не подключена")

class TestDatabase(unittest.TestCase):
    db = Database(is_connected=False)

    @skipUnlessConnected(db)
    def test_query(self):
        self.assertTrue(True)
```
### 8. Пропуск теста на основе результата предыдущего теста

Иногда тест логически связан с результатом другого теста, и его выполнение имеет смысл только при успешном завершении первого.
```python
def skipUnlessPreviousTestPassed(test_case, method_name):
    if getattr(test_case, f"{method_name}_passed", False):
        return lambda func: func
    return unittest.skip(f"Предыдущий тест {method_name} не прошёл")

class TestSequence(unittest.TestCase):
    test_first_passed = False

    def test_first(self):
        self.test_first_passed = True
        self.assertTrue(True)

    @skipUnlessPreviousTestPassed(test_case=TestSequence, method_name="test_first")
    def test_second(self):
        self.assertTrue(True)
```

## переопределение декораторов `@expectedFailure`
Декоратор `@unittest.expectedFailure` используется, чтобы отметить тесты, которые ожидаются как заведомо провальные, например, из-за известных багов или несоответствия текущим требованиям. Он помогает не засорять тестовые отчёты ненужными ошибками, пока проблема не будет исправлена.

Переопределение` @expectedFailure` можно использовать для более сложных сценариев, чем просто отметка "этот тест провалится". Вот несколько более разносторонних кейсов:

### 1. Условный `expectedFailure` для определённых платформ

Иногда тест может проваливаться только на определённых платформах (например, Windows или macOS). Мы можем указать, что ошибка ожидается только в этих условиях.
```python
import unittest
import platform

def expectedFailureOnPlatform(target_platform):
    if platform.system() == target_platform:
        return unittest.expectedFailure
    return lambda func: func  # Обычный тест

class TestPlatformSpecific(unittest.TestCase):
    @expectedFailureOnPlatform("Windows")
    def test_feature(self):
        # Проваливается только на Windows
        self.assertEqual(1 + 1, 3)
```
### 2. Ожидаемый провал из-за определённой версии библиотеки

Если тест проваливается в определённой версии зависимости (например, `numpy` или `pandas`), его можно пропустить до исправления.
```python
import unittest
import numpy as np

def expectedFailureIfVersionLessThan(module, min_version):
    if tuple(map(int, module.__version__.split("."))) < min_version:
        return unittest.expectedFailure
    return lambda func: func  # Обычный тест

class TestLibraryFeature(unittest.TestCase):
    @expectedFailureIfVersionLessThan(np, (1, 21))
    def test_numpy_feature(self):
        # Провалится, если версия numpy < 1.21
        self.assertTrue(False, "Функция недоступна в старых версиях")
```
### 3. Ожидаемый провал на основе конфигурации окружения

Если тест зависит от состояния окружения (например, флаг DEBUG), можно указать, что ошибка ожидается только в этих условиях.
```python
import os
import unittest

def expectedFailureIfEnvVarSet(var_name):
    if os.getenv(var_name):
        return unittest.expectedFailure
    return lambda func: func

class TestEnvironment(unittest.TestCase):
    @expectedFailureIfEnvVarSet("DEBUG")
    def test_production_behavior(self):
        # Ожидаемый провал в режиме DEBUG
        self.assertTrue(False, "Ошибка ожидается в режиме DEBUG")
```
### 4. Ожидаемый провал из-за неготовой функциональности

Иногда функциональность ещё не реализована, но вы пишете тест заранее (Test-Driven Development). Вы можете пометить тест как ожидаемо провальный до завершения реализации.
```python
def expectedFailureUntilImplemented():
    # Удобный маркер для ожидаемого провала до реализации
    return unittest.expectedFailure

class TestFeatureDevelopment(unittest.TestCase):
    @expectedFailureUntilImplemented()
    def test_future_feature(self):
        # Этот тест провалится, пока фича не реализована
        self.assertEqual(1 + 2, 4)
```
### 5. Динамический expectedFailure на основе состояния базы данных

Например, если известно, что определённая таблица в базе данных недоступна, можно ожидать провал.
```python
import unittest
import sqlite3

def expectedFailureIfTableMissing(db_connection, table_name):
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    if not cursor.fetchone():
        return unittest.expectedFailure
    return lambda func: func

class TestDatabase(unittest.TestCase):
    connection = sqlite3.connect(":memory:")

    @classmethod
    def setUpClass(cls):
        cls.connection.execute("CREATE TABLE users (id INTEGER, name TEXT)")

    @expectedFailureIfTableMissing(connection, "non_existing_table")
    def test_missing_table(self):
        # Ожидается провал, так как таблицы нет
        self.connection.execute("SELECT * FROM non_existing_table")
```
### 6. Ожидаемый провал из-за экспериментальных функций

Если тест связан с экспериментальной функциональностью, его можно пометить как ожидаемо провальный, пока функция не будет протестирована и стабильна.
```python
def expectedFailureForExperimentalFeature():
    # Маркер для тестов, зависящих от нестабильных функций
    return unittest.expectedFailure

class TestExperimental(unittest.TestCase):
    @expectedFailureForExperimentalFeature()
    def test_experimental_logic(self):
        # Этот тест ожидаемо провалится
        self.assertEqual(1 / 0, 0)  # Функция нестабильна
```
### 7. Ожидаемый провал для редких граничных случаев

Если тест специально написан для проверки редкого бага, но он ещё не исправлен, его можно временно пометить.
```python
def expectedFailureForKnownBug(ticket_id):
    return unittest.expectedFailure

class TestKnownIssues(unittest.TestCase):
    @expectedFailureForKnownBug(ticket_id="BUG-1234")
    def test_known_edge_case(self):
        # Провал ожидается из-за известного бага
        self.assertEqual(1 / 3, 0.333)  # Ошибка округления
```
Принципы создания кастомных expectedFailure декораторов:

    Динамическая логика. Кастомный декоратор полезен, если условие провала теста  сложно или зависит от внешних факторов (платформы, версии библиотек, окружения).  
    Контроль обратной совместимости. Убедитесь, что условия "ожидаемого провала" чётко описаны, чтобы декоратор не помечал корректные тесты.  
    Переход к нормальному состоянию. Используйте @expectedFailure временно: по мере устранения известных причин провала убирайте декоратор.

## переопределение `@patch`
### Частые случаи
Переопределение: Возможно и часто бывает полезным.  
Причина: Патчи могут быть кастомизированы для определённых нужд, например, добавления логики, обработки исключений или интеграции с другими инструментами.  
Пример переопределения:
```python
from unittest.mock import patch

def my_patch(target, new=None):
    def decorator(test_func):
        @patch(target, new)
        def wrapper(*args, **kwargs):
            print(f"Патч применён к {target}")
            return test_func(*args, **kwargs)
        return wrapper
    return decorator
```
**`@unittest.mock.patch.multiple`**
Переопределение: Можно, но редко требуется.  
Причина: Обычно достаточно стандартного поведения, так как декоратор выполняет конкретную задачу — замену нескольких атрибутов.  
Пример: Включение дополнительной логики:
```python
def my_patch_multiple(target, **kwargs):
    def decorator(test_func):
        @patch.multiple(target, **kwargs)
        def wrapper(*args, **kwargs):
            print(f"Патч применён к {target} с атрибутами {kwargs}")
            return test_func(*args, **kwargs)
        return wrapper
    return decorator
```
### Разные варианты
Декоратор `@patch` из модуля `unittest.mock` используется для подмены объектов или функций во время тестирования. Он позволяет временно заменять зависимости, чтобы изолировать тестируемый код от внешних факторов, таких как вызовы API, базы данных или сложная логика.  
Примеры нестандартных или разносторонних кейсов переопределения `@patch`
#### 1. Динамическая подмена на основе конфигурации
Иногда нужно подменять объект или функцию только в определённых условиях, например, в зависимости от окружения.
```python
from unittest.mock import patch
import os

def patch_based_on_env(target, new_value, env_var):
    if os.getenv(env_var):
        return patch(target, new_value)
    return lambda func: func  # Оставляем без изменений

class TestEnvironmentSpecificPatch(unittest.TestCase):
    @patch_based_on_env('os.path.exists', lambda path: True, 'TEST_ENV')
    def test_feature(self):
        # os.path.exists всегда возвращает True в окружении TEST_ENV
        self.assertTrue(os.path.exists('/non/existing/path'))
```
#### 2. Подмена объекта только для определённых платформ

Если тестируемый код ведёт себя по-разному на Windows и Linux, можно подменять зависимости только для конкретной платформы.
```python
import platform
from unittest.mock import patch

def patch_on_platform(target, new_value, target_platform):
    if platform.system() == target_platform:
        return patch(target, new_value)
    return lambda func: func  # Без изменений

class TestPlatformSpecificPatch(unittest.TestCase):
    @patch_on_platform('os.name', 'posix', 'Windows')
    def test_windows_behavior(self):
        # os.name будет "posix" только на Windows
        self.assertEqual(os.name, 'posix' if platform.system() == 'Windows' else os.name)
```
#### 3. Подмена функций для экспериментального кода

Иногда функции или методы недоступны в текущей версии системы, но их можно замокать для тестирования новой логики.
```python
def patch_for_experimental(target, experimental_implementation):
    # Подмена функций только для экспериментов
    return patch(target, experimental_implementation)

class TestExperimentalFeature(unittest.TestCase):
    @patch_for_experimental('math.sqrt', lambda x: x ** 0.5)
    def test_new_sqrt_logic(self):
        # Используем экспериментальную реализацию math.sqrt
        self.assertEqual(math.sqrt(4), 2.0)
```
#### 4. Подмена методов для работы с устаревшими API

Если ваш тестируемый код зависит от устаревшего API, можно подменить метод, чтобы эмулировать его работу в текущей версии.
```python
def patch_deprecated_api(target, replacement):
    # Подмена устаревшего API
    return patch(target, replacement)

class TestDeprecatedAPI(unittest.TestCase):
    @patch_deprecated_api('os.getlogin', lambda: 'mock_user')
    def test_old_api(self):
        # Подмена os.getlogin для устаревшего вызова
        self.assertEqual(os.getlogin(), 'mock_user')
```
#### 5. Автоматическая подмена всех методов модуля

Если нужно подменить сразу несколько методов одного модуля, можно написать декоратор, который автоматизирует процесс.
```python
from unittest.mock import patch

def patch_multiple(targets):
    def decorator(func):
        patches = [patch(target, lambda *args: 'mocked') for target in targets]
        for p in patches:
            p.start()
        try:
            return func
        finally:
            for p in patches:
                p.stop()
    return decorator

class TestMultiplePatches(unittest.TestCase):
    @patch_multiple(['os.path.exists', 'os.path.isdir'])
    def test_multiple_patches(self):
        # os.path.exists и os.path.isdir возвращают 'mocked'
        self.assertEqual(os.path.exists('/any/path'), 'mocked')
        self.assertEqual(os.path.isdir('/any/path'), 'mocked')
```
#### 6. Подмена вызовов с динамическими параметрами

Если замена логики зависит от входных параметров, можно создать обёртку, которая определяет поведение на лету.
```python
from unittest.mock import patch

def patch_dynamic(target, behavior_func):
    # Замена функции на основе поведения
    return patch(target, behavior_func)

class TestDynamicBehavior(unittest.TestCase):
    @patch_dynamic('os.getenv', lambda var: 'mock_value' if var == 'TEST' else None)
    def test_dynamic_behavior(self):
        # os.getenv возвращает mock_value только для переменной TEST
        self.assertEqual(os.getenv('TEST'), 'mock_value')
        self.assertIsNone(os.getenv('OTHER'))
```
#### 7. Подмена для сложных асинхронных функций

Если тестируемый код использует асинхронные вызовы, можно замокать их поведение для различных сценариев.
```python
from unittest.mock import AsyncMock, patch

def patch_async(target, return_value):
    return patch(target, new_callable=lambda: AsyncMock(return_value=return_value))

class TestAsyncBehavior(unittest.TestCase):
    @patch_async('aiohttp.ClientSession.get', return_value='mock_response')
    async def test_async_patch(self):
        # aiohttp.ClientSession.get всегда возвращает mock_response
        response = await aiohttp.ClientSession().get('http://example.com')
        self.assertEqual(response, 'mock_response')
```
Принципы кастомизации `@patch`:

    **Динамические условия**: Добавляйте логику проверки перед подменой (например, текущая платформа или окружение).  
    **Управляемое поведение**: Создавайте предсказуемую подмену для случаев, где важна точная эмуляция.  
    **Изоляция**: Убедитесь, что замена сохраняет тестируемый код изолированным от внешних зависимостей.  
    **Поддержка асинхронности**: Используйте AsyncMock для эмуляции асинхронных функций.  

Эти сценарии позволяют более гибко подстраивать тесты к различным ситуациям, сохраняя их надёжность и независимость.

# Объединение тестов в TestSuite для создания сложных сценариев.
Объединение тестов в `TestSuite` позволяет запускать несколько тестов или групп тестов вместе. Это полезно, когда нужно организовать тесты в логические группы или создать сложные сценарии выполнения.

Пример объединения тестов в TestSuite
## 1. Тесты для объединения

Создадим два тестовых класса с разными наборами тестов.
```python
import unittest

class MathTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

class StringTests(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isupper(self):
        self.assertTrue("HELLO".isupper())
        self.assertFalse("Hello".isupper())
```
## 2. Объединение тестов в TestSuite

Создаём `TestSuite`, добавляем туда тесты вручную или используем загрузчик.
```python
if __name__ == "__main__":
    # Создание экземпляра TestSuite
    suite = unittest.TestSuite()

    # Добавление тестов вручную
    suite.addTest(MathTests("test_addition"))
    suite.addTest(MathTests("test_subtraction"))
    suite.addTest(StringTests("test_upper"))
    suite.addTest(StringTests("test_isupper"))

    # Запуск всех тестов в наборе
    runner = unittest.TextTestRunner()
    runner.run(suite)
```
## 3. Автоматическое добавление тестов с TestLoader

Вместо добавления тестов вручную, можно использовать `TestLoader` для автоматической загрузки всех тестов из класса или модуля.
```python
if __name__ == "__main__":
    # Создаём загрузчик тестов
    loader = unittest.TestLoader()

    # Загружаем тесты из классов
    math_tests = loader.loadTestsFromTestCase(MathTests)
    string_tests = loader.loadTestsFromTestCase(StringTests)

    # Объединяем тесты в TestSuite
    suite = unittest.TestSuite([math_tests, string_tests])

    # Запускаем все тесты
    runner = unittest.TextTestRunner()
    runner.run(suite)
```

## 4. Использование метода discover

`discover` автоматически находит все тесты в указанной директории.
```python
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern="test_*.py")  # Ищет файлы, начинающиеся с test_

    runner = unittest.TextTestRunner()
    runner.run(suite)
```
Зачем использовать `TestSuite`?

    Управление порядком выполнения тестов:
    Например, сначала запустить важные тесты, а затем менее критичные.

    Объединение по функциональным блокам:
    Например, тесты для базы данных, API, пользовательского интерфейса.

    Изолированные сценарии:
    Разделение больших наборов тестов на более мелкие, которые можно выполнять по отдельности.

    Оптимизация тестирования:
    Тесты можно сгруппировать для выполнения только тех, которые связаны с недавно изменённым кодом.

    Интеграция в CI/CD:
    В сложных системах можно запускать разные группы тестов на разных этапах сборки.

Этот подход позволяет гибко управлять тестами и их запуском, особенно в больших проектах с большим количеством тестовых сценариев.

# Патчеры в фикстурах
Есть юнит-тест коннектора к БД:
```python
class TestDataBaseFetcher(unittest.TestCase):
    
    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.sqlite'})
    def test_connect_success(self, mock_connect):
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        db_fetcher.connect()
        mock_connect.assert_called_once_with(db_fetcher.db_path)
        self.assertIsNotNone(db_fetcher.conn)

    @patch('datahub.fetcher.sqlite3.connect')
    @patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.sqlite'})
    def test_connect_failure(self, mock_connect):
        mock_connect.side_effect = Exception("Connection error")
        db_fetcher = DataBaseFetcher(db_name='test.db', db_table='test_table')
        db_fetcher.connect()
        self.assertIsNone(db_fetcher.conn)
```
Везде моки:
```python
@patch('datahub.fetcher.sqlite3.connect')
@patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.sqlite'})
```
Их можно вынести в фикстуры:
```python
class TestDataBaseFetcher(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Патчим переменные окружения
        cls.env_patcher = patch.dict(
            'os.environ',
            {'DB_PATH': '/test/path', 'DB_NAME': 'test.sqlite', 'DB_TABLE': 'test_table'}
        )
        cls.env_patcher.start()

        # Патчим sqlite3.connect
        cls.sqlite_patcher = patch('datahub.fetcher.sqlite3.connect')
        cls.mock_connect = cls.sqlite_patcher.start()

    @classmethod
    def tearDownClass(cls):
        # Останавливаем оба патчера
        cls.env_patcher.stop()
        cls.sqlite_patcher.stop()
    
    # остальной код - тесты
```
**Когда использовать фикстуру?**

Использование фикстуры оправдано, если:

    Все или большинство тестов в классе используют один и тот же мок.
    Настройка мока идентична для всех тестов.

**Когда лучше оставить @patch?**

Оставлять `@patch` следует, если:

    Разные тесты требуют уникальных настроек мока.
    Вы хотите минимизировать область действия подмены, чтобы избежать побочных эффектов.

Объяснение:

    `setUpClass` для объединения патчей:
        Переменные окружения патчатся через patch.dict и запускаются через start().
        Метод sqlite3.connect патчится через patch и также запускается через start().

    Хранение ссылок на патчеры:
        Ссылки на патчеры (`cls.env_patcher` и `cls.sqlite_patcher`) сохраняются, чтобы их можно было остановить через `stop()` в `tearDownClass`.

    Область действия моков:
        Оба мока (`os.environ` и `sqlite3.connect`) будут активны для всех тестов в этом классе.

    Изоляция тестов:
        Если требуется настройка мока для конкретного теста (например, `side_effect`), это можно сделать внутри теста, как в примере `test_connect_failure`.

Метод `tearDownClass` в классе тестов на основе `unittest` будет обязательно выполнен после завершения всех тестов в этом классе, если он переопределён. Это стандартный механизм библиотеки `unittest`, предназначенный для выполнения завершающих действий после выполнения всех тестов в данном классе.

**Ключевые моменты**:

    Обязательный вызов `tearDownClass`:
        `unittest` автоматически вызывает `tearDownClass`, если тесты выполнены, либо при возникновении исключений в тестах.

    Контекст выполнения:
        `tearDownClass` вызывается только один раз, после выполнения всех тестов, принадлежащих классу. Это позволяет очистить ресурсы или остановить глобальные моки, которые были настроены в `setUpClass`.

    Рекомендации:
        Убедитесь, что в методе `tearDownClass` вызываются все действия по очистке ресурсов, созданных в `setUpClass` (например, остановка всех патчеров).
        Если метод `tearDownClass` отсутствует, ресурсы, созданные в `setUpClass`, не будут автоматически очищены, что может привести к проблемам (например, утечке памяти, оставшимся мокам).

## Порядок старта патчеров
Порядок старта патчеров в `setUpClass` имеет значение, поскольку он влияет на то, как будут применяться моки и какие значения переменных или функций будут доступны. Если порядок старта патчеров изменён, это может изменить поведение кода внутри тестов.

Декораторы в Python применяются "снизу вверх", то есть для:
```python
@patch('datahub.fetcher.sqlite3.connect')
@patch.dict(os.environ, {'DB_PATH': '/test/path', 'DB_NAME': 'test.sqlite'})
```
Сначала применяется `patch.dict(os.environ, ...)`, а затем `patch('datahub.fetcher.sqlite3.connect')`

Это значит, что:

    Переменные окружения изменяются до того, как начнётся патчинг `sqlite3.connect`.
    Код, использующий `sqlite3.connect`, будет работать с уже изменённым окружением.

**Когда порядок критичен?**

    Взаимосвязь между моками: Если первый мок (os.environ) влияет на поведение второго (sqlite3.connect), то порядок их применения становится критически важным.

    Зависимости в тестируемом коде: Если sqlite3.connect напрямую зависит от переменных окружения, их изменение должно произойти до патчинга sqlite3.connect.

## Сброс моков в фикстурах

```python
def setUp(self):
    """
    Set up before each test method.

    Resets the mock sqlite3.connect instance and clears any side effects.
    """
    self.mock_connect.reset_mock()
    self.mock_connect.side_effect = None
```