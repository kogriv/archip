## Поиск версий Питон на хост-машине (винда)
Используем путь к исполняемому файлу Python:
```python
import os
import sys

def get_host_installed_python_versions():
    python_versions = {}

    # Получаем путь к исполняемому файлу Python
    python_executable_path = sys.executable
    print("python_executable_path: ",python_executable_path)

    # Получаем каталог, содержащий исполняемый файл Python
    python_installation_path = os.path.dirname(os.path.dirname(python_executable_path))
    print("python_installation_path: ",python_installation_path)

    # Получаем список всех папок в каталоге установки Python
    python_folders = os.listdir(python_installation_path)

    for folder in python_folders:
        # Проверяем, является ли папка версией Python
        if folder.startswith('Python'):
            python_version = folder.replace('Python', '')
            python_version_path = os.path.join(python_installation_path, folder)
            python_executable = os.path.join(python_version_path, 'python.exe')

            if os.path.isfile(python_executable):
                python_versions[python_version] = python_executable

    return python_versions

# Пример использования:
installed_python_versions = get_host_installed_python_versions()
print("Установленные версии Python:")
print(installed_python_versions)
```

Получаем:
```cmd
Установленные версии Python:
{'311': 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python311\\python.exe', '37': 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python37\\python.exe', '39': 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'}
```
В данном случае корректная работа скрипта зависит от того какие пути выирались при установке разных версий питона. По умолчанию путь текущей версии, которую можно узначть через `sys.executable` должен совпадать с путями других версий.


## Поиск версий Питон в докер-контейнере
В контейнере структура папок другая. Используем скрипт:
```python
import os

def find_python_executables():
    python_executables = []

    # Пути, где могут быть установлены Python
    search_paths = ['/usr/bin', '/usr/local/bin', '/opt/conda/bin', '/usr/lib']

    for path in search_paths:
        if os.path.isdir(path):
            for filename in os.listdir(path):
                full_path = os.path.join(path, filename)
                # Проверяем, является ли файл исполняемым и начинается ли с "python"
                if os.path.isfile(full_path) and os.access(full_path, os.X_OK) and 'python' in filename:
                    python_executables.append(full_path)

    return python_executables

# Получаем и выводим список всех установленных Python-интерпретаторов
python_executables = find_python_executables()
if python_executables:
    print("Установленные Python-интерпретаторы:")
    for exe in python_executables:
        print(exe)
else:
    print("Python-интерпретаторы не найдены.")
```

получим вывод:
```cmd
Установленные Python-интерпретаторы:
/usr/bin/python3
/usr/bin/python3.10
/opt/conda/bin/python3
/opt/conda/bin/python3.11
/opt/conda/bin/python
/opt/conda/bin/python3.11-config
/opt/conda/bin/python3.1
/opt/conda/bin/python3-config
/opt/conda/bin/grpc_python_plugin
/opt/conda/bin/ipython
/opt/conda/bin/ipython3
```

Необходимо отметить, что в Linux расширение файла не обязательно для определения его типа исполняемого файла. Это связано с тем, что в Linux файлы выполняются на основе их прав доступа (permissions). Если у файла установлен бит исполнения (execute bit), то система Linux будет считать его исполняемым, независимо от наличия расширения в его имени.

## Символическая ссылка Python 3.x
Файлы `/usr/bin/python3` и `/usr/bin/python3.10` представляют собой два разных исполняемых файла Python.

**/usr/bin/python3:**  
Это символическая ссылка на конкретную версию Python 3.x. В системах Linux часто используется символическая ссылка `/usr/bin/python3`, чтобы указывать на последнюю (по умолчанию) версию Python 3.x в системе. Это удобно для того, чтобы приложения и скрипты, написанные на Python 3, могли запускаться, не зависимо от точной версии Python.

**/usr/bin/python3.10:**  
Это конкретная версия Python 3.10. В отличие от символической ссылки, это конкретный исполняемый файл Python 3.10. Он может быть использован явно для запуска скриптов, которым требуется именно эта версия Python.

В целом, символическая ссылка `/usr/bin/python3` предоставляет удобный способ обращения к последней версии Python 3 на вашей системе, тогда как конкретные исполняемые файлы вида `/usr/bin/python3.10`, `/usr/bin/python3.9`, и так далее, представляют конкретные версии Python.

В данном контейнере выполнение в терминале команды `/usr/bin/python3` запустит последнюю и единственную версию конкретную python3.10 в папке `/usr/bin`.

## Файлы python3.x-config
Файл `python3.11-config` в директории `/opt/conda/bin/` является скриптом, который предоставляет информацию о настройках и параметрах сборки Python 3.11, установленного в вашем окружении Conda.

Этот скрипт обычно используется в процессе сборки и установки дополнительных модулей или пакетов Python, особенно тех, которые требуют компиляции или настройки перед установкой.

Например, он может предоставлять информацию о путях к заголовочным файлам, библиотекам или другим параметрам, которые необходимы для успешной сборки и установки дополнительных библиотек Python.

Вы можете выполнить этот скрипт с различными опциями, чтобы получить информацию о различных аспектах конфигурации Python, таких как версия, пути, опции компиляции и т. д. Для получения справки о доступных опциях вы можете выполнить:
```bash
/opt/conda/bin/python3.11-config --help
```
## Файлы grpc_python_plugin
Файл `grpc_python_plugin` в директории `/opt/conda/bin/` представляет собой исполняемый файл, который является частью фреймворка **gRPC**.

**gRPC (gRPC Remote Procedure Call)** - это высокопроизводительный RPC (Remote Procedure Call) фреймворк, разработанный компанией Google. Он использует протокол HTTP/2 для обмена данными и протокол сериализации `Protobuf` для определения формата сообщений.

`grpc_python_plugin` используется в процессе компиляции Protobuf файлов для генерации кода на языке Python, который позволяет клиентам и серверам взаимодействовать через gRPC.

Как правило, при разработке распределенных систем, основанных на gRPC, разработчики описывают структуру своих сервисов с использованием Protobuf, а затем используют grpc_python_plugin для генерации Python-кода, который обеспечивает взаимодействие с этими сервисами.

В целом, grpc_python_plugin является важным инструментом для разработки клиент-серверных приложений, основанных на gRPC, в среде Python.

## ipython
Файл `/opt/conda/bin/ipython` представляет собой исполняемый файл для запуска интерактивной оболочки IPython в среде Python. IPython - это улучшенная интерактивная оболочка для Python, которая предоставляет множество дополнительных функций и возможностей по сравнению с стандартной интерпретатором Python.

Вот некоторые из основных возможностей IPython:

**Автодополнение (Tab Completion):** IPython позволяет автоматически дополнять имена переменных, атрибуты и методы при нажатии клавиши Tab, что делает интерактивную разработку более продуктивной.

**Подсказки и документация:** IPython предоставляет подсказки и документацию о модулях, функциях и методах, что помогает быстрее понимать и использовать Python API.

**Магические команды (Magic Commands):** IPython поддерживает специальные "магические" команды, которые расширяют функциональность оболочки, позволяя делать вещи такие как измерение времени выполнения, работа с файловой системой, отладка и многое другое.

**Интерактивная визуализация:** IPython интегрирует мощные инструменты для визуализации данных, включая интеграцию с библиотеками визуализации, такими как `Matplotlib`.

Поддержка различных оболочек: IPython может использоваться как в классической командной строковой оболочке, так и в браузере с использованием интерактивной HTML-оболочки (Jupyter Notebook).

Файл `/opt/conda/bin/ipython` позволяет запускать IPython в среде, где используется дистрибутив Anaconda или Miniconda. Anaconda предоставляет широкий набор пакетов для научных вычислений и анализа данных, а IPython является одним из инструментов, включенных в этот дистрибутив для улучшенного взаимодействия с Python.

## Определение версии по умолчанию.
Чтобы сделать версию Python 3.10, которая находится в /usr/bin/python3.10, версией по умолчанию, вы можете воспользоваться утилитой update-alternatives, которая позволяет управлять альтернативами для исполняемых файлов в системе.

Вот как это можно сделать:  
Откройте терминал. Выполните следующую команду для добавления альтернативы `Python 3.10`:
```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
```
Это команда добавляет альтернативу python3, указывающую на /usr/bin/python3.10, с приоритетом 1.  
Если вы хотите изменить версию Python по умолчанию, выполните следующую команду:
```bash
sudo update-alternatives --config python3
```

Это покажет список альтернатив Python 3.x в вашей системе и позволит вам выбрать нужную версию, указав соответствующий номер.  
Выберите версию Python 3.10 из списка, и это сделает ее версией по умолчанию.  
После этого, когда вы запускаете python3 --version, система будет использовать версию Python 3.10, указанную по умолчанию.

В Docker контейнерах могут быть особенности в работе с альтернативами и установленными пакетами. Возможно, нужно явно явно вызывать Python 3.10, используя его полный путь, до тех пор пока он не станет версией по умолчанию.

## Запуск скриптов в Linux с помощью определенной версии Питон.
Если у вас установлены несколько версий Python на вашей системе, есть несколько способов запуска скриптов с использованием определенной версии Python:

**Явное указание пути к интерпретатору Python:**  
Вы можете указать путь к конкретному исполняемому файлу Python при запуске скрипта. Например:
```bash
/usr/bin/python3.10 script.py
```

**Использование символических ссылок:**  
Вы можете создать символическую ссылку на нужную версию Python и использовать ее для запуска скриптов. Например, если вы хотите использовать Python 3.10 по умолчанию, вы можете создать ссылку следующим образом:
```bash
sudo ln -s /usr/bin/python3.10 /usr/local/bin/python
```
**Использование виртуальных сред:**  
Использование виртуальных сред Python (например, venv или virtualenv) позволяет создавать изолированные окружения Python с определенными версиями и пакетами. Вы можете создать виртуальную среду с нужной версией Python и активировать ее перед запуском скрипта.

**Использование скриптовых оболочек:**  
Вы можете написать скриптную оболочку, которая будет запускать скрипты с использованием определенной версии Python. Например, создайте скрипт run_script.sh следующего содержания:
```bash
#!/bin/bash
/usr/bin/python3.10 script.py
```
И затем запускайте этот скрипт вместо самого Python скрипта.

## Запуск скриптов в Windows с помощью py.
В Windows, когда у вас установлены несколько версий Python, вы можете использовать утилиту py для запуска скриптов с определенной версией Python.

Откройте командную строку (cmd) или PowerShell.  
Для запуска скрипта с использованием Python 3.10 введите:
```cmd
py -3.10 script.py
```
Метод **py** автоматически выбирает подходящую версию Python на основе вашей установки и настроек среды. Вам не нужно заботиться о полном пути к исполняемому файлу Python, py сделает это за вас.  
Утилита **py** (`Python Launcher`) доступна только в операционных системах семейства Windows.  
Для других операционных систем, таких как Linux и macOS, вам придется использовать полные пути к исполняемым файлам Python или другие методы управления версиями Python, такие как символические ссылки, виртуальные окружения и т. д.

## Запуск интерпритатора определенной версии
Если вы хотите запустить например Python 3.7 из оболочки Bash, просто укажите полный путь к исполняемому файлу Python.
```bash
/C/Users/user/AppData/Local/Programs/Python/Python37/python
```
Если на вашем компьютере под управлением Windows установлен Python 3.7 и добавлен в переменную среды PATH, то в командной строке Bash (в Linux или macOS) вы не сможете просто написать python3.7, чтобы запустить его, так как это ожидает, что Python будет доступен в системных путях, что не так для Windows.
