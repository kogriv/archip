обновление пипа <возможно только определенных модулей>
pip install -U pip <module_name1 module_name2 setuptools> 

установка библиотек
pip install <lib_name1 lib_name2 ...>

удаление библиотек
pip uninstall <lib_name> -y
-y флаг подтверждения

вывод установленных библиотек (зависимостей)
pip freeze

запись списка в файл
pip freeze > requiremens.txt

