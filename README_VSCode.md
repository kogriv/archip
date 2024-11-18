Below are various settings you can change in your workspace settings.json file (View > Command Palette... and run the "Preferences: Open Workspace Settings (JSON)" command) to disable potentially perf intensive Pylance features in VS Code.

# Настройка Pylance в VS Code контейнера

Определение рабочей области (папок для индексирования). Важно, если рабочая область задана корнем контейнера, что может привести к ошибкам при индексировании пилансом большого количества файлов.

1. Откройте настройки проекта

В контейнере VS Code создайте файл настроек для рабочего пространства, если его нет:  
Перейдите в папку .vscode в корне контейнера (вашего проекта) (если папки нет, создайте её).  
Создайте файл settings.json, если он отсутствует.

2. Настройте python.analysis.include и python.analysis.exclude  
Добавьте в файл .vscode/settings.json следующие настройки:
```json
{
  "python.analysis.include": ["/app/**/*"],
  "python.analysis.exclude": ["**/*", "!/app/**/*"],
  "python.analysis.autoSearchPaths": false,
  "python.analysis.diagnosticMode": "workspace",
  "python.analysis.useLibraryCodeForTypes": true
}
```
Объяснение:  
`"python.analysis.include": ["/app/**/*"]` — указывает Pylance включать только файлы внутри папки /app.  
`"python.analysis.exclude": ["**/*", "!/app/**/*"]` — исключает всё, кроме папки /app.  
`"python.analysis.autoSearchPaths": false` — отключает автоматическое сканирование дополнительных путей.  
`"python.analysis.diagnosticMode": "workspace"` — ограничивает анализ до указанной рабочей директории.  
`"python.analysis.useLibraryCodeForTypes": true` — включает анализ кода в подключенных библиотеках.

3. Перезагрузите VS Code  
После внесения изменений:  
Сохраните файл settings.json.  
В командной палитре (Ctrl+Shift+P) выполните Reload Window.

4. Дополнительно: Настройка extraPaths (при необходимости)  
Если ваш проект использует нестандартные пути для импорта модулей (например, сторонние библиотеки или модули в нестандартной структуре), добавьте их в extraPaths:
```json
{
  "python.analysis.extraPaths": ["/app/specific_folder"]
}
```
Теперь Pylance будет работать только с папкой /app, что существенно ускорит индексацию и устранит проблемы с автодополнением.

# Рекомендации по настройке Pylance
в VS Code для оптимизации производительности, особенно при работе с большими рабочими пространствами. Вот подробное объяснение ключевых пунктов  

**Workspace-wide settings (Настройки для всей рабочей области)**

    "python.analysis.exclude": ["**"]
        Исключает все файлы из рабочей области.
        IntelliSense (автодополнения и подсказки) будет работать только для открытых файлов.
        Полезно для очень больших проектов, чтобы избежать лишнего расхода ресурсов.

    "python.analysis.indexing": false
        Отключает индексацию рабочей области и сторонних библиотек.
        Индексация используется для поиска символов и автодополнений, но отключение ускоряет работу в больших проектах.

    "python.analysis.diagnosticMode": "openFilesOnly"
        Включает проверку проблем (ошибок, предупреждений) только для открытых файлов, а не всей рабочей области.
        Это снижает нагрузку на Pylance, особенно в больших проектах.

**Features with custom support (Функции с кастомной поддержкой)**

    "python.analysis.supportRestructuredText": false
        Отключает поддержку парсинга docstring в формате reStructuredText.
        Полезно, если вы не используете этот формат документации, для экономии ресурсов.

    "python.analysis.enablePytestSupport": false
        Отключает поддержку кастомных функций для pytest.
        Полезно, если вы не используете pytest для тестирования.

**Inlay hints (Подсказки внутри кода)**

    "python.analysis.inlayHints.callArgumentNames": "off"
        Отключает подсказки имен аргументов при вызове функции.

    "python.analysis.inlayHints.functionReturnTypes": false
        Отключает подсказки типов возвращаемых значений функций.

    "python.analysis.inlayHints.pytestParameters": false
        Отключает подсказки параметров для тестов в pytest.

    "python.analysis.inlayHints.variableTypes": false
        Отключает подсказки типов переменных.

**Type features (Функции, связанные с типами)**

    "python.analysis.typeCheckingMode": "off"
        Отключает проверку типов.
        Ускоряет работу, но IntelliSense может стать менее точным.

    "python.analysis.useLibraryCodeForTypes": false
        Отключает извлечение информации о типах из библиотек.
        Ускоряет работу, но автодополнения для сторонних библиотек могут быть менее точными.

**Editor features (Функции редактора)**

    "editor.semanticHighlighting.enabled": false
        Отключает семантическое выделение синтаксиса (цветовое выделение на основе типа данных, функций и т. д.).
        Это может уменьшить нагрузку на редактор.

    "editor.occurrencesHighlight": "off"
        Отключает подсветку всех вхождений символа при его выделении.
        Ускоряет работу в больших файлах.

**Less perf intensive features (Менее ресурсоёмкие функции)**

    "python.analysis.completeFunctionParens": false
        Отключает автоматическое добавление скобок при выборе функции из подсказок.

    "python.analysis.autoFormatStrings": false
        Отключает автоматическое преобразование строк в f-строки при добавлении {}.

    "python.analysis.autoImportCompletions": false
        Отключает подсказки для автозагрузки импортов.

    "python.analysis.gotoDefinitionInStringLiteral": false
        Отключает возможность перехода к определению, если строка выглядит как имя модуля.

# Ограничьте рабочую область

Если у вас всё ещё большая рабочая область, настройте файлы для наблюдения. Проверьте, что вы исключили ненужные каталоги и файлы (например, node_modules, .git и другие).
В settings.json можно добавить:
```json{
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/.git/**": true,
    "**/__pycache__/**": true,
    "**/build/**": true
  }
}
```
