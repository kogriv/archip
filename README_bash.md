## Стартовый скрипт Bash (де/активация виртуального окружения)
Для изменения или отключения скрипта, который автоматически активирует виртуальное окружение Conda при запуске терминала в Bash, вам необходимо отредактировать конфигурационный файл вашего shell. Обычно это .bashrc или .bash_profile для пользователя.

Откройте терминал и введите команду для редактирования файла .bashrc или .bash_profile. Обычно это делается с помощью редактора, такого как nano или vim:
```bash
nano ~/.bashrc
```
или:
```bash
nano ~/.bash_profile
```
Найдите в файле строку, которая активирует Conda. Это обычно что-то вроде:
```bash
source /path/to/conda.sh
conda activate some_environment
```
или строка, начинающаяся с `conda activate`.  
Пример из жизни:
```bash
eval "$(command conda shell.bash hook 2> /dev/null)"
```
Закомментируйте соответствующие строки, добавив `#` в начале каждой из них.  
После внесения изменений сохраните файл и закройте редактор. Например, в nano это делается через `Ctrl+O`, затем `Enter` и `Ctrl+X`.

Чтобы применить изменения, либо перезапустите терминал, либо введите команду source ~/.bashrc или source ~/.bash_profile (в зависимости от того, какой файл вы редактировали).

## Стартовый скрипт в контейнере Докер
Контейнеры Docker в Windows не используют Bash или другие настройки напрямую из вашей установки WSL (Windows Subsystem for Linux). Вот как это устроено:

Docker в Windows: Docker может работать в Windows через WSL 2 (Windows Subsystem for Linux версии 2) или через Docker Desktop. Однако Docker контейнеры — это изолированные среды, и они не зависят от настроек вашей основной операционной системы или WSL.

Операционная система контейнера: Каждый Docker контейнер запускается на базе своего собственного образа, который включает в себя необходимую операционную систему (например, Ubuntu, Alpine Linux и т.д.) и необходимое программное обеспечение. Этот образ определяет, какая версия и конфигурация Bash (или другой оболочки) будет использоваться в контейнере.

**Конфигурация Bash в контейнере**: Конфигурация Bash в Docker контейнере определяется его образом. Файл `~/.bashrc` или другие конфигурационные файлы оболочки в контейнере не связаны с файлами в вашей основной системе Windows или WSL. Они могут быть преднастроены в базовом образе или настроены вами через Dockerfile или при входе в контейнер.

WSL как среда для Docker: Если вы используете WSL 2 для работы с Docker в Windows, WSL 2 действует как гостевая система для Docker. Однако это не означает, что настройки WSL напрямую влияют на контейнеры Docker. WSL помогает запустить Docker Daemon и обеспечивает совместимость с Linux, но каждый контейнер запускается изолированно со своими собственными настройками.

Таким образом, конфигурации вашей системы Windows или WSL не влияют на конфигурацию Bash внутри контейнера Docker.

## Монтирование кастомного стартового скрипта в контейнер
Если вы не хотите изменять Dockerfile и нуждаетесь в использовании своего конкретного файла в качестве `~/.bashrc` для контейнера например `jupyter_lab`, вы можете использовать механизм монтирования файлов Docker. Это позволит вам "подключить" локальный файл скрипта Bash напрямую в контейнер.

Вот как это можно сделать:  
**Создайте скрипт Bash** на вашем локальном компьютере, который вы хотите использовать в качестве `~/.bashrc` в контейнере. Предположим, что ваш скрипт находится по пути `/path/to/your/custom_bashrc`.

**Измените скрипт запуска** кластера для монтирования файла:  
В вашем скрипте запуска кластера измените команду `docker run` для контейнера `jupyter_lab`, добавив том (volume) для монтирования вашего скрипта в контейнер. Вы должны заменить `/path/to/your/custom_bashrc` на абсолютный путь к вашему файлу.

**Пример** с использованием функции `run_container`, созданной на основе `docker run` (в проекте chicago_spark) отдельно:
```bash
run_container "jupyter_lab" \
  "-d --name jupyter_lab -p 10000:8888 --network spark_network --user root \
  -v $PATH_TO_PROJECT_DIR:/work:rw \
  -v /path/to/your/custom_bashrc:/home/jovyan/.bashrc \
  -e SPARK_MASTER_IP=$SPARK_MASTER_IP \
  -e SPARK_MASTER=spark://$SPARK_MASTER_IP:7077 \
  jupyter/pyspark-notebook start-notebook.sh \
  --NotebookApp.token='' --NotebookApp.notebook_dir='/work'"
```

**Перезапустите контейнер**:  
Убедитесь, что вы остановили и удалили предыдущий контейнер jupyter_lab, если он был запущен, а затем запустите его заново с обновленной командой запуска.

Этот метод позволяет вам использовать любой локальный файл Bash скрипта в качестве ~/.bashrc в вашем контейнере jupyter_lab. Учитывайте, что если ваш скрипт содержит ссылки на другие локальные файлы или предполагает наличие **определенной структуры каталогов**, эти файлы или каталоги также нужно будет соответствующим образом монтировать в контейнер.

## Монтирование в контейнер при наличии кастомного стартового скрипта на хост-машине
Пример из проекта `chicago_spark`:
```bash
PATH_TO_BASH_START=/mnt/c/Users/user/Documents/Pro/chicago_spark/scripts/bash_start.sh

echo "Container jupyter_lab creating/starting..."
# local custom_bashrc=$PATH_TO_BASH_START
# Проверяем, существует ли кастомный скрипт Bash
mount_custom_bashrc=""
if [ -f "$PATH_TO_BASH_START" ]; then
  # Если файл существует, добавляем параметр монтирования к команде
  echo "Custom .bashrc exists"
  mount_custom_bashrc="-v $PATH_TO_BASH_START:/home/jovyan/.bashrc"
else
  echo "Custom .bashrc NOT exists"
  #mount_custom_bashrc=""
fi

# Run Jupyter Lab
run_jupyter_command="-d --name jupyter_lab -p 10000:8888 --network spark_network --user root \
-v $PATH_TO_PROJECT_DIR:/work:rw \
$mount_custom_bashrc \
-e SPARK_MASTER_IP=$SPARK_MASTER_IP \
-e SPARK_MASTER=spark://$SPARK_MASTER_IP:7077 \
-e PYTHONPATH=/work \
jupyter/pyspark-notebook start-notebook.sh \
--NotebookApp.token='' --NotebookApp.notebook_dir='/work'"

echo "Jupyter container run command:"
echo "$run_jupyter_command"
# echo "After printing Jupyter container run command:"
run_container "jupyter_lab" "$run_jupyter_command"
```

## Скрипт-проверка наличия указанного файла
Скрипт, который просто проверит наличие файла по указанному пути и выведет соответствующее сообщение.

```bash
#!/bin/bash

# Путь к файлу или просто имя файла
file_path="sync.sh" # или "/c/Users/user/Documents/Pro/chicago_spark/scripts/sync.sh"

# Проверяем, является ли путь абсолютным
if [[ "$file_path" = /* ]]; then
    full_path="$file_path"
else
    # Получаем полный путь к файлу в текущей директории
    full_path="$(pwd)/$file_path"
fi

# Проверка наличия файла
if [ -f "$full_path" ]; then
    echo "Файл найден: $full_path"
else
    echo "Файл не найден: $full_path"
fi
```

То же самое, в диалоговом режиме:
```bash
#!/bin/bash

# Выводим подробное сообщение с примерами ввода
echo "Введите имя файла или полный путь к файлу. Например, это может быть:"
echo "- sync.sh - любое имя файла"
echo "- /c/Users/user/Documents/Pro/chicago_spark/scripts/bash_start.sh - полный путь Windows"
echo "- /mnt/c/Users/user/Documents/Pro/chicago_spark/scripts/bash_start.sh - полный путь Container"
# Запрашиваем у пользователя ввод
read file_path


# Проверяем, является ли путь абсолютным
if [[ "$file_path" = /* ]]; then
    full_path="$file_path"
else
    # Получаем полный путь к файлу в текущей директории
    full_path="$(pwd)/$file_path"
fi

# Проверка наличия файла
if [ -f "$full_path" ]; then
    echo "Файл найден: $full_path"
else
    echo "Файл не найден: $full_path"
fi
```

## Cохранение многострочных текстов в переменных
В Bash вы можете сохранять многострочные тексты в переменных. Для этого используйте конструкцию cat с использованием heredoc-синтаксиса (<<) или присвойте многострочный текст переменной напрямую, используя кавычки. Вот примеры обоих методов:
```bash
#!/bin/bash

mona_lisa=$(cat <<'EOF'
      ____  
    o8%8888,    
  o88%8888888.  
 8'-    -:8888b   
8'         8888  
d8.-=.  ==-.:888b  
>8 '~'  '~'  d8888   
88      \    ,88888   
88b.  `-~   ':88888  
888b ~==~ .:88888  
88888o--:':::8888      
`88888| :::' 8888b  
8888^^'       8888b  
d888           ,%888b.   
d88%            %%%8--'-.  
/88:.__ ,       _%-' ---  -  
    '''::===..-'   =  --.  ` 
EOF
)

other_art=$(cat <<'EOF'
  ,--./,-.
 / #      \
|   P*     |
 \   I    / 
  `._,.P.+' 
EOF
)

echo "$mona_lisa"
echo "$other_art"
```

Прямое присваивание многострочного текста переменной:
```bash
#!/bin/bash

mona_lisa="
    ...  
    ...
    ... 
"

other_art="
  ...
  ...
"

echo "$mona_lisa"
echo "$other_art"
```
В обоих примерах переменные mona_lisa и other_art содержат многострочный текст. В первом примере используется heredoc-синтаксис, который удобен для сохранения текста с сохранением форматирования и без необходимости экранирования специальных символов. Во втором примере текст просто заключается в кавычки, что также сохраняет форматирование, но требует внимания к специальным символам.

## Кастомный стартовый скрипт с запросом активации Conda
К стоковому скрипту (копипаст результата команды `cat ~/.bashrc` c локальной (хост) машины) добавлен запрос на активацию базового окружения менеджером пакетов Conda:
```bash
#...стоковый скрипт...

mona_lisa=$(cat <<'EOF'
        ...
EOF
)

other_art=$(cat <<'EOF'
        ...
EOF
)


# A prompt for activating Conda
read -p "Activate Conda base? (y/n): " activate_conda
if [[ $activate_conda == 'y' || $activate_conda == 'Y' ]]; then
    # Check if Conda is installed
    if command -v conda >/dev/null 2>&1; then
        # Conda is installed, activate it
        echo "$mona_lisa"
        eval "$(command conda shell.bash hook 2> /dev/null)"
    else
        # Conda is not installed, display a message
        echo "Conda is not installed, use PIP."
    fi
else
    echo "$other_art"
fi
```

