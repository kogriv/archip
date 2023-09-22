import logging.config
from mochalov_lesson3_settings import  logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def main():
    logger.debug('Enter in the main()')


if __name__ == '__main__':
    main()