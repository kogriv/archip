import logging

# logging.basicConfig() # level='INFO'

app_logger = logging.getLogger('app_logger')
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')
app_logger.addHandler(console_handler)

f = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')
console_handler.setFormatter(f)

utils_logger = logging.getLogger('app_logger.utils')
utils_logger.setLevel('DEBUG')
# utils_logger.propagate = False

def main():
    utils_logger.debug('Hellow world')


if __name__ == '__main__':
    main()