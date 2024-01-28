## Переменные окружения. Описание
Переменные окружения (`Environment Variables`):  
Переменные окружения представляют собой способ хранения конфигурационной информации (о **среде выполнения процессов**) в операционной системе, доступной для процессов и приложений. Они используются для передачи информации, такой как пути к исполняемым файлам, настройки языковой среды, и другие параметры, которые влияют на поведение программ. Процессы и приложения получают доступ к значениям переменных окружения **для настройки своего поведения**.

**Реализация в Windows:**
*Как установить:* В системе Windows переменные окружения можно установить через системные настройки:  
Правой кнопкой мыши по "Пуск" -> "Система" -> "Дополнительные параметры системы" -> "Переменные среды".  
*Как использовать:* В командной строке команда `%VAR_NAME%` используется для получения значения переменной окружения.

**Реализация в Linux:**
*Как установить:* В Linux переменные окружения устанавливаются через команды в терминале. Например:
```bash
export VAR_NAME=value
```
*Как использовать:* В командной строке используется `$VAR_NAME` для получения значения переменной окружения.

**Пример использования:**  
Например, переменная `PATH` содержит список директорий, в которых операционная система ищет исполняемые файлы.
Применение в программировании: Программы могут использовать переменные окружения для определения различного поведения в зависимости от конфигурации окружения.

**Ограничения:** Длина значения переменной окружения обычно ограничена, и некоторые переменные могут быть доступны только для чтения.

## Доступ в питон.
В Python для работы с переменными окружения используется модуль os. Вот простой пример кода, который выводит информацию о переменных окружения:
```python
import os
import platform

def print_environment_variables():
    # Получаем словарь с переменными окружения
    env_vars = os.environ

    # Выводим информацию о платформе
    print(f"Информация о платформе: {platform.system()} {platform.release()}")

    # Выводим информацию о каждой переменной окружения
    print("\nИнформация о переменных окружения:")
    for key, value in env_vars.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print_environment_variables()
```
Пример переменных для Виндоус и Докер-контейнера можно посмотреть в пдф файлах в папке environ репозитория.

## Идентификация работы внутри контейнера
В контейнере разработки проекта `chicago_spark` нет переменных окружения явно указывющих на то, что программа запущена внутри контейнера и переменных с идентификатором контейнера.  
При этом есть ряд переменных окружения косвенно указывающих на работу в контейнере. Например:  
`PATH = /home/jovyan/....`  
`REMOTE_CONTAINERS = true`  

Наличие определенных файлов и директорий, а также использование специфических команд, могут служить индикаторами того, что программа выполняется в контейнере. Вот несколько признаков, на которые можно обратить внимание:
```bash
cat /proc/1/cgroup
```
Если вы видите строки, связанные с контейнерами, это может быть признаком работы в контейнере.
```bash
/var/run/docker.sock:
```
Наличие файла /var/run/docker.sock также может указывать на то, что программа выполняется в контейнере Docker.

Проверьте наличие утилит, связанных с управлением контейнерами, таких как docker, podman, rkt, или других, в зависимости от используемой технологии контейнеризации.
```bash
which docker
```

Контейнеры также могут включать специфические файлы или директории, которые указывают на их принадлежность к контейнеру. Например, `/run/secrets/kubernetes.io/serviceaccount/token` может свидетельствовать о работе в Kubernetes.

Пример скрипта на Python, который может выполнять несколько проверок для определения того, выполняется ли программа в контейнере. А также выводить в консоль / сохранять в файл нужный список переменных:
```python
import os
import platform


def print_environment_variables(selected_vars=None, save_to_file=False):
    if selected_vars is not None:
        full_list = True if "FULL_ENVIRON_LIST" in selected_vars else False
    else:
        full_list = False
    # Получаем словарь с переменными окружения
    env_vars = os.environ

    # Выводим информацию о платформе
    print(f"Информация о платформе: {platform.system()} {platform.release()}")

    container_id = check_in_container()

    # Выбираем переменные для вывода (по умолчанию - _HOME_SPARK_MASTER)
    if selected_vars is None:
        selected_vars = ["_", "HOME", "SPARK_MASTER"]
    elif full_list: selected_vars = env_vars

    # Выводим информацию о каждой переменной окружения из списка
    print("\nИнформация о переменных окружения:")
    for key in selected_vars:
        if key in env_vars:
            print(f"{key}: {env_vars[key]}")
        else:
            print(f"{key}: Не найдено")

    # Сохраняем в файл, если указано
    if save_to_file:
        save_env_to_file(env_vars, selected_vars, container_id)


def check_in_container():
    # Проверка наличия /proc/1/cgroup
    cgroup_path = '/proc/1/cgroup'
    if os.path.exists(cgroup_path):
        with open(cgroup_path, 'r') as cgroup_file:
            for line in cgroup_file:
                if "docker" in line:
                    # Ищем строку, содержащую "docker" и извлекаем идентификатор контейнера
                    parts = line.split(":")
                    if len(parts) >= 3:
                        container_id_full = parts[2].strip()
                        container_id = container_id_full.split("/")[-1]
                        print(f"Программа выполняется в контейнере: {container_id}")
                        return container_id

    # Проверка наличия /var/run/docker.sock
    docker_sock_path = '/var/run/docker.sock'
    if os.path.exists(docker_sock_path):
        return True

    print("Программа не выполняется в контейнере.")
    return False


def save_env_to_file(env_vars, selected_vars, container_id):
    # Формируем строку для сохранения
    lines_to_save = [
        f"{key}={value}" for key,
        value in env_vars.items()
        if key in selected_vars
    ]
    print("строку для сохранения")
    print(lines_to_save)
    # Добавляем информацию о контейнере, если есть
    if container_id:
        lines_to_save.append(f"CONTAINER_ID={container_id}")

    # Путь для сохранения файла
    home_path = os.path.expanduser("/")
    save_folder_path = os.path.join(home_path, "work", "environ")

    # Создаем папку, если не существует
    os.makedirs(save_folder_path, exist_ok=True)

    # Формируем путь для сохранения файла
    save_path = os.path.join(save_folder_path, ".env_list_full")

    # Сохраняем в файл
    with open(save_path, 'w') as save_file:
        save_file.write("\n".join(lines_to_save))

    print(f"Переменные окружения сохранены в файл: {save_path}")


if __name__ == "__main__":
    # Примеры использования:

    # 1. Вывести переменные по умолчанию
    # print_environment_variables()

    # 2. Вывести только выбранные переменные и сохранить в файл
    selected_vars = ["TERM_PROGRAM", "HOME", "SPARK_MASTER"]
    # selected_vars = ["FULL_ENVIRON_LIST"]
    print_environment_variables(selected_vars, save_to_file=True)
```
