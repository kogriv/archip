import logging.config
from oop_logging_settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('oopushka_logger')
logger.info('**** 002  methods sample *******')

class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        logger.info('Вызов метода set_coord, self value: '+str(self))
        self.x = x
        self.y = y
        logger.info('set_coord установил координаты, x: '
                     +str(self.x)+' y:'+str(self.y))


    def get_coords(self):
        logger.info('Вызов метода get_coord, self value: '+str(self))
        return (self.x, self.y)

def main():
    pt = Point()
    pt.set_coords(1, 2)
    logger.info('property list for object: '+str(pt.__dict__))
    x, y = pt.get_coords()
    logger.info('get_coord вернул координаты, x: '
                + str(x) + ' y:' + str(y))
    f = getattr(pt, 'get_coords')
    logger.info('attr: get_coords is:'+str(f))
    logger.info('get_coords call result:'+str(f()))


if __name__ == '__main__':
    main()