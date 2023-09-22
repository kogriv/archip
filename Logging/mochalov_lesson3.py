import logging
from mochalov_lesson3_settings import  logger_config


logger = logging.getLogger('app_logger')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

file_handler = logging.FileHandler(
'molchanov_lesson3_debug.log', mode='a')
logger.addHandler(file_handler)

std_format = logging.Formatter(
fmt='{asctime} - {levelname} - {name} - {message}',
style='{'
# fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
# style='%'
)
console_handler.setFormatter(std_format)
file_handler.setFormatter(std_format)

def main():
    logger.debug('Enter in the main()')


if __name__ == '__main__':
    main()