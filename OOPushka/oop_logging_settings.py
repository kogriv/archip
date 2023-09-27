logger_config = {
    'version' : 1,
    'disable_existing_loggers' : True,

    'formatters' : {
        'std_format' : {
            'format' : '{asctime} - {levelname} - {name} - '
                       '{module}:{funcName}:{lineno} - '
                       '{message}',
            'style' : '{'
        },
        'short_format' : {
            'format' : '{module}:{funcName}:{lineno} - '
                       '{message}',
            'style' : '{'
        }
    },
    'handlers' : {
        'console' : {
            'class' : 'logging.StreamHandler',
            'level' : 'DEBUG',
            'formatter' : 'short_format'
        }
    },
    'loggers' : {
        'oopushka_logger' : {
            'level' : 'INFO',
            'handlers' : ['console'],
            # 'propagate' : False
        }
    },

    # 'filters' : {},
    # 'root' : {} # '' : {}
    # 'incremental' : True
}