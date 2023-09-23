import logging

class MegaHandler(logging.Handler):
    def __init__(self, filename):
        # Инициализация класса Handler
        logging.Handler.__init__(self)
        self.filename = filename

    # Реализация метода emit()
    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'w') as file:
            file.write(message + '\n')


logger_config = {
    'version' : 1,
    'disable_existing_loggers' : False,

    'formatters' : {
        'std_format' : {
            'format' : '{asctime} - {levelname} - {name} - '
                       '{module}:{funcName}:{lineno} - '
                       '{message}',
            'style' : '{'
        }
    },
    'handlers' : {
        'console' : {
            'class' : 'logging.StreamHandler',
            'level' : 'DEBUG',
            'formatter' : 'std_format'
        },
        'file' : {
            '()' : MegaHandler,
            'level' : 'DEBUG',
            'filename' : 'mochalov_lesson6_debug.log',
            'formatter' : 'std_format'
        }
    },
    'loggers' : {
        'app_logger' : {
            'level' : 'DEBUG',
            'handlers' : ['console', 'file'],
            # 'propagate' : False
        }
    },

    # 'filters' : {},
    # 'root' : {} # '' : {}
    # 'incremental' : True
}