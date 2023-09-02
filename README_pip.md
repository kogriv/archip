обновление пипа <возможно только определенных модулей>
```powershell
pip install -U pip <module_name1 module_name2 setuptools>
```

установка библиотек
```powershell
pip install <lib_name1 lib_name2 ...>
```

удаление библиотек
```powershell
pip uninstall <lib_name> -y
```
-y флаг подтверждения

вывод установленных библиотек (зависимостей)
```powershell
pip freeze
```

запись списка в файл
```powershell
pip freeze > requiremens.txt
```

