import logging.config
from mochalov_lesson5_settings import  logger_config

logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')

def new_function():
    variable = 'variable_value'
    logger.debug('Enter in to the new_function()',
                 extra={'some_variable_name' : variable})

def main():
    logger.debug('Enter in to the main()')


if __name__ == '__main__':
    # main()
    new_function()