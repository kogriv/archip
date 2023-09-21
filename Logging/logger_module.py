import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_example.out'
LOG_FILENAME_ROTATING = 'logging_rotatingfile_example.out'


def logger_common_docstring():
    """
Система журналирования состоит из 4-х взимодействующих
типов объектов. Каждый модуль или приложение, которому
необходимо протоколировать некоторые события, использует
экземпляр Logger для добавления информации в журналы.
Его вызов создает объект LogRecord, который сохраняет
информацию в памяти до тех пор, пока она не будет обработана.
Экземпляр Logger может иметь ряд объектов Handler,
сконфигурированных для получения и обработки записей
журнала. Для преобразования записей журнала в выводимые
сообщения объект Handler использует объект Formatter.

Все обработчики, использующие для протоколирования
журнальных сообщений файлы, расположения HTTP GET/POST,
почтовые адреса, доступные через протокол SMTP, типолые
сокеты и специфические для ОС системы журналирования,
включены в модуль logging.

:return: LOG_FILENAME
"""
    pass


def logger_file_writing(message_arg):
    """
Большинство приложений конфигурируются для записи журнала
в файл. Используйте функцию basicConfig() для установки
обработчика по умолчанию, чтобы отладочные сообщения
записывались в файл.

:param message_arg:
:return: LOG_FILENAME
    """

    logging.basicConfig(
        filename=LOG_FILENAME,
        level=logging.DEBUG,
    )

    logging.debug(message_arg)

    with open(LOG_FILENAME, 'rt') as f:
        body = f.read()

    print('FILE:')
    print(body)
    return LOG_FILENAME


def logger_rotatingfile_writing():
    """
Повторное выполнение logger_file_writing(message_arg)
приведет к добавлению сообщений в существующий файл.
Чтобы при каждом запуске программы создавался новый файл,
можно указать строку 'w' в качестве аргумента filemode
при вызове функции basicConfig(). Однако более эффективное
управление этим процессом обеспечивает класс RotatingFileHandler,
который автоматически создает новый файл журнала и при этом
сохраняет его предыдущую версию.

Самой последней версией журнала будет logging_rotatingfile_example.out
Т.е. без индексов

:return:
    """
    # Set up a specific logger with our desired output level
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME_ROTATING,
        maxBytes=20,
        backupCount=5,
    )
    my_logger.addHandler(handler)

    # Log some messages
    for i in range(20):
        my_logger.debug('i = %d' % i)

    # See what files are created
    logfiles = glob.glob('%s*' % LOG_FILENAME_ROTATING)
    for filename in sorted(logfiles):
        print(filename)


def logger_levels():
    """
API модуля logging предлагает генерацию сообщений, относящихся
к разным уровням важности (уровням протоколирования). Т.е. можно
установить порог протоколирования (например, чтобы отладочные
сообщения не записывались в проде).
Журнальное сообщение отображается лишь в том случае, если обработчик
и регистратор настроены для генерирования этого или более высокого
уровня.

:return:
    """
    LEVELS = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL,
    }

    initial_level = logging.getLogger().getEffectiveLevel()  # Получим начальный уровень журналирования

    for level_name, level_value in LEVELS.items():
        logging.getLogger().setLevel(level_value)
        level = '=====LEVEL====::' + str(level_value)
        logging.critical(level)
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical error message')

    logging.getLogger().setLevel(initial_level)  # Восстановим начальный уровень журналирования


def logger_parent_child(config_loglevel=logging.DEBUG,
                        parent_loglevel=logging.DEBUG,
                        child_loglevel=logging.DEBUG):
    """
При работе с нерутовыми логгерами необходимо использовать
logging.basicConfig(level=config_loglevel)
поскольку some_logger.setLevel(logging.some_logger_level)
без .basicConfig не устанавливает уровень

.getEffectiveLevel() возвращает уровень журналирования, который
будет применяться для данного логгера, учитывая текущее
наследование уровня от родительских логгеров. Это полезно,
чтобы определить, будут ли записи логгера видны в данный момент,
и, если да, то на каком уровне.

Уровень журналирования по умолчанию для корневого логгера
(root logger) установлен на logging.WARNING

по умолчанию все созданные логгеры, которые не наследуются
явным образом от других ранее созданных логгеров, будут
наследовать от корневого логгера (root logger). Корневой
логгер- это верхний уровень в иерархии логгеров в библиотеке
logging в Python. Если вы не устанавливаете уровень
журналирования для созданного логгера явно, он будет
наследовать уровень от корневого логгера.

Инструкции
logger.setLevel(logging.INFO) и logging.root.setLevel(logging.INFO)
являются эквивалентными. Обе инструкции устанавливают уровень
журналирования для корневого логгера (root logger) на INFO.
Обратите внимание, что logging.root - это ссылка на корневой
логгер, поэтому оба способа приведут к одному и тому же
результату.

:return:
    """

    # Устанавливаем уровень журналирования для корневого логгера
    # logging.root.setLevel(logging.INFO)

    logging.basicConfig(level=config_loglevel)

    # Создаем родительский логгер и устанавливаем его уровень
    parent_logger = logging.getLogger('parent_logger')
    parent_logger.setLevel(parent_loglevel)

    # Создаем наследуемый логгер как подлоггер родительского логгера
    child_logger = parent_logger.getChild('child_logger')
    child_logger.setLevel(child_loglevel)
    # child_logger.propagate = False

    # Уровень журналирования наследуемого логгера будет унаследован от родительского
    child_effective_level = child_logger.getEffectiveLevel()

    print(f"Effective Level for child_logger: {child_effective_level}")

    parent_effective_level = parent_logger.getEffectiveLevel()
    print(f"Effective Level for parent_logger: {parent_effective_level}")

    # Попробуем зарегистрировать сообщения на разных уровнях
    child_logger.debug("child_logger:: This is a debug message")
    child_logger.info("child_logger:: This is an info message")
    child_logger.warning("child_logger:: This is an warning message")
    child_logger.error("child_logger:: This is an error message")
    child_logger.critical("child_logger:: This is an critical message")

    parent_logger.debug("parent_logger:: This is a debug message")
    parent_logger.info("parent_logger:: This is an info message")
    parent_logger.warning("parent_logger:: This is an warning message")
    parent_logger.error("parent_logger:: This is an error message")
    parent_logger.critical("parent_logger:: This is an critical message")


def logger_submodule_example(config_loglevel=logging.DEBUG):
    # logging.basicConfig(level=config_loglevel)

    import auxiliary_module

    # create logger with 'spam_application'
    logger = logging.getLogger('spam_application')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('creating an instance of auxiliary_module.Auxiliary')
    a = auxiliary_module.Auxiliary()
    logger.info('created an instance of auxiliary_module.Auxiliary')
    logger.info('calling auxiliary_module.Auxiliary.do_something')
    a.do_something()
    logger.info('finished auxiliary_module.Auxiliary.do_something')
    logger.info('calling auxiliary_module.some_function()')
    auxiliary_module.some_function()
    logger.info('done with auxiliary_module.some_function()')


def logger_multiple_destin():
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='logger_multiple_destin.log',
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    # Now, we can log to the root logger, or any other logger. First the root...
    logging.info('Jackdaws love my big sphinx of quartz.')

    # Now, define a couple of other loggers which might represent areas in your
    # application:

    logger1 = logging.getLogger('myapp.area1')
    logger2 = logging.getLogger('myapp.area2')

    logger1.debug('Quick zephyrs blow, vexing daft Jim.')
    logger1.info('How quickly daft jumping zebras vex.')
    logger2.warning('Jail zesty vixen who grabbed pay from quack.')
    logger2.error('The five boxing wizards jump quickly.')

if __name__ == '__main__':
    # message = 'This message should go to the log file'
    # message = logger_file_writing.__doc__
    # logger_file_writing(message)
    # logger_rotatingfile_writing()
    # logger_levels()
    # logger_parent_child(logging.DEBUG,logging.INFO,logging.DEBUG)
    # logger_submodule_example()
    logger_multiple_destin()
