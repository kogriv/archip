import logging.config
from oop_logging_settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('oopushka_logger')
logger.info('**** 003  init sample *******')


class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        logger.info('Вызов __init__')
        self.x = x
        self.y = y

    def __del__(self):
        logger.info('удаление объекта'+str(self))

    def set_coords(self, x, y):
        logger.info('Вызов метода set_coord, self value: ' + str(self))
        self.x = x
        self.y = y
        logger.info('set_coord установил координаты, x: '
                    + str(self.x) + ' y:' + str(self.y))

    def get_coords(self):
        logger.info('Вызов метода get_coord, self value: ' + str(self))
        return (self.x, self.y)


pt = Point(1,3)
logger.info(pt.__dict__)
# logger.info('Присвоим другое значение переменной')
# pt = 2
logger.info('**********|| END ||***************')
