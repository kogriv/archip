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