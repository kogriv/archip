import logging

logging.basicConfig(level='DEBUG',
                    filename='mochalov_lesson1.log')

logger = logging.getLogger()
print(logger)
print()

# logger.setLevel('DEBUG') # 10 / logging.DEBUG
print(logger.level)

print()
print(logger.handlers)

def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')


if __name__ == '__main__':
    main('gk')