
В powershell:

```powershell
gh auth login
>>>
gh : Имя "gh" не распознано как имя командлета, функции, файла сценария или выполняемой программы. Проверьте правильность написания имени, а также наличие и правильность пути, после чего повто
рите попытку.
строка:1 знак:1
+ gh auth login
+ ~~
    + CategoryInfo          : ObjectNotFound: (gh:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```
Сообщение об ошибке указывает на то, что команда gh (GitHub CLI) не распознается в вашей среде PowerShell. Это может возникнуть, если GitHub CLI не установлен или не добавлен в вашу переменную среды PATH. Давайте убедимся, что GitHub CLI установлен и настроен правильно.

    Убедитесь, что GitHub CLI установлен:
    Перейдите на официальный сайт GitHub CLI (https://cli.github.com/) и следуйте инструкциям для вашей операционной системы, чтобы установить GitHub CLI. После установки перезапустите вашу сессию PowerShell или откройте новое окно терминала.

    Убедитесь, что путь к исполняемому файлу GitHub CLI добавлен в переменную среды PATH:
    После установки GitHub CLI, убедитесь, что путь к исполняемому файлу gh добавлен в вашу переменную среды PATH. Вы можете сделать это следующим образом:
        Откройте PowerShell.
        Выполните команду для получения местоположения исполняемого файла gh:
```powershell
Get-Command gh
```
        Проверьте вывод и убедитесь, что он указывает на верное местоположение исполняемого файла GitHub CLI.

    После завершения шагов 1 и 2, повторите команду gh auth login, и она должна успешно открыть окно аутентификации GitHub.

--------------------------------
gh auth login

```powershell
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Paste an authentication token
Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
The minimum required scopes are 'repo', 'read:org', 'workflow'.
? Paste your authentication token:
X Sorry, your reply was invalid: Value is required
? Paste your authentication token: *
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as kogriv
PS C:\Users\user\documents\pro\archip> gh repo create
? What would you like to do? Push an existing local repository to GitHub
? Path to local repository (.)

? Path to local repository .
? Repository name (archip)

? Repository name archip
? Description sysf'one

? Description sysf'one
? Visibility Public
✓ Created repository kogriv/archip on GitHub
? Add a remote? Yes
? What should the new remote be called? (origin) master

? What should the new remote be called? master
```

Для авторизации с использованием токена, созданного ранее на GitHub, выберите протокол "HTTPS". Токен можно использовать в URL-адресе для аутентификации при выполнении операций Git через HTTPS.

Authenticate Git with your GitHub credentials? (Y/n)
...хотите ли вы аутентифицироваться в Git с помощью ваших учетных данных GitHub. Если у вас есть аккаунт GitHub, и вы хотите использовать свои учетные данные для аутентификации при выполнении операций Git (например, git push), то вам нужно будет ввести "Y" и нажать Enter. Это позволит Git использовать ваши учетные данные GitHub для доступа к вашим репозиториям.

----------------------------------

После успешной авторизации с помощью gh auth login ваш токен GitHub будет сохранен на вашем компьютере и будет использоваться автоматически при выполнении операций, которые требуют аутентификации на GitHub.

Это означает, что после перезагрузки PowerShell или закрытия и повторного открытия окна терминала вам не нужно будет снова вводить учетные данные или токен. GitHub CLI будет использовать сохраненные учетные данные или токен для выполнения авторизованных операций.

----------------------------------
Чтобы удаленно создать репозиторий на GitHub и загрузить в него существующий локальный репозиторий (клонировать его на GitHub), вы можете использовать команды Git и GitHub CLI (Command Line Interface). Вот как это сделать:

    Убедитесь, что у вас установлен Git и GitHub CLI на вашем компьютере.

    Откройте терминал или командную строку.

    Войдите в свой аккаунт GitHub через командную строку, если вы ещё этого не сделали, используя команду gh auth login и следуя инструкциям.

    Перейдите в локальный репозиторий, который вы хотите загрузить на GitHub, с помощью команды cd:
```powershell
cd /путь/к/вашему/репозиторию
```

    Создайте удаленный репозиторий на GitHub с помощью команды
```powershell
gh repo create:
```
GitHub CLI запросит у вас название репозитория, описание и другие параметры. Вы можете ввести их или просто нажать Enter, чтобы использовать значения по умолчанию.

GitHub CLI создаст удаленный репозиторий на GitHub и настроит его для связи с вашим локальным репозиторием. После этого он покажет вам URL удаленного репозитория.

Теперь, чтобы загрузить содержимое вашего локального репозитория на GitHub, выполните команду git push:
```powershell
git push origin master
```
    Это отправит вашу локальную ветку master на удаленный репозиторий на GitHub. Если у вас другая ветка, замените master на имя вашей ветки.

Теперь ваш локальный репозиторий успешно клонирован на GitHub, и вы можете управлять им через командную строку, не заходя на сайт GitHub.
-----------------------------

Чтобы посмотреть удаленные репозитории, привязанные к текущему локальному репозиторию с использованием Git, вы можете выполнить следующую команду в командной строке (в вашем случае в PowerShell):
```powershell
git remote -v
```

    Вы увидите результат, подобный этому:
```powershell
origin  https://github.com/username/repo.git (fetch)
origin  https://github.com/username/repo.git (push)
```
    Здесь "origin" - это стандартное имя для удаленного репозитория, который был склонирован из исходного репозитория. У вас может быть несколько удаленных репозиториев, и вы увидите их все в этом списке, если они были добавлены к вашему локальному репозиторию.

-----------------------------------

имею:
```powershell
git remote -v
master  https://github.com/kogriv/archip.git (fetch)
master  https://github.com/kogriv/archip.git (push)
```

как переименовать master в origin?

Чтобы переименовать удаленный репозиторий с именем "master" на "origin", выполните следующие команды:

    Сначала удалите удаленный репозиторий с именем "origin" (если он уже существует), чтобы избежать конфликта имен:
```powershell
git remote remove origin
```

    Затем переименуйте удаленный репозиторий "master" на "origin" с помощью следующей команды:
```powershell
git remote rename master origin
```

Имя "origin" в контексте Git - это локальное имя, которое вы используете для ссылки на удаленный репозиторий на вашем компьютере. Это не влияет на сам удаленный репозиторий на GitHub или другом хостинге кода.

Когда вы переименовываете "origin" на своем компьютере, это просто переименовывает локальную ссылку на удаленный репозиторий. Название "origin" является просто соглашением о наименовании по умолчанию для удаленного репозитория, и его изменение не влияет на удаленный репозиторий на GitHub. Удаленный репозиторий на GitHub остается без изменений и сохраняет свое имя (например, "kogriv/archip.git" в вашем случае).

Иными словами, изменение имени "origin" на вашем компьютере не затрагивает удаленный репозиторий на GitHub и не вносит изменений в его структуру или настройки. Это просто изменение имени для удобства управления удаленными репозиториями на вашем локальном компьютере.

---------------------------------------------



