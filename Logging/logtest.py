import logging
import requests

logging.basicConfig(level='DEBUG')

logger = logging.getLogger()

def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')
    r = requests.get('https://www.google.ru')

    for key in logging.Logger.manager.loggerDict:
        print(key)


if __name__ == '__main__':
    main('func_name_specified')