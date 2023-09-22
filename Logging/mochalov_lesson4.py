import logging.config
from mochalov_lesson3_settings import  logger_config

logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')


words = ['new house','apple','ice cream', 3]

def main():
    for item in words:
        try:
            print(item.split(' '))
        except:
            logger.debug(
                f'D_Exception here, item = {item}',
                exc_info=True)
            logger.exception(f'E_Exception here, item = {item}')
            pass


if __name__ == '__main__':
    main()