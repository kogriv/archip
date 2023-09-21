import logging

logging.basicConfig(level='INFO')

print('logging.getLogger info:',logging.getLogger())
print('logging.getLogger parent info:',logging.getLogger().parent)
print()

logger = logging.getLogger()
print('setting logger (root) level to INFO')
logger.setLevel('INFO')
print('logging.getLogger info:',logging.getLogger())
print('logging.getLogger parent info:',logging.getLogger().parent)
print()

print('logger info:',logger)
print('logger parent info:',logger.parent)
print()

app_logger = logging.getLogger('app_logger')
console_handler = logging.StreamHandler()
console_handler.setLevel('INFO')
app_logger.addHandler(console_handler)
print('app_logger info:',app_logger)
print('app_logger parent info:',app_logger.parent)
print('app_logger Handlers:',app_logger.handlers)

print()
print('root Handlers:',app_logger.parent.handlers)
print()

utils_logger = logging.getLogger('app_logger.utils')
utils_logger.setLevel('DEBUG')
# utils_logger.propagate = False
print('app.logger.utils info:',utils_logger)
print('app.logger.utils parent info:',utils_logger.parent)
print('utils_logger Handlers:',utils_logger.handlers)

def main():
    utils_logger.debug('Hellow world')


if __name__ == '__main__':
    main()