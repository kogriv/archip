import  logging
from pprint import pprint

class NewFunctionFilter(logging.Filter):
    def filter(self, record):
        pprint(dir(record), width=60, compact=True)
        print(record.some_variable_name)
        return record.funcName == 'new_function'

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
            'formatter' : 'std_format',
            'filters' : ['new_filter']
        }
    },
    'loggers' : {
        'app_logger' : {
            'level' : 'DEBUG',
            'handlers' : ['console'],
            # 'propagate' : False
        }
    },

    'filters' : {
        'new_filter' : {
            '()' : NewFunctionFilter
        }
    },
    # 'root' : {} # '' : {}
    # 'incremental' : True
}