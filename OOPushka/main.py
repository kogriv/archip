import logging.config
from oop_logging_settings import logger_config

from  SB_000_Param_polymorph import AsymmetricEllipse, Figure

logging.config.dictConfig(logger_config)
logger = logging.getLogger('oopushka_logger')
logger.debug('logging in main module started')

def main():
    # Создаем экземпляр
    asym_ellipse = AsymmetricEllipse(40, 40, "green", 3)
    asym_ellipse.draw()
    msg = f'Type of figure: {type(asym_ellipse)}'
    logger.debug(msg)
    figure = Figure(40, 40, "green", 3)
    figure.draw()
    msg = f'Type of figure: {type(figure)}'
    logger.debug(msg)

def adding(x,y):
    return x + y

if __name__ == '__main__':
    # msg = 'in __main__ way started'
    # print(msg)
    # logger.debug(msg)
    # main()
    x,y = 32, 41
    msg = f'adding of int x: {x} and y: {y}='+str(adding(x,y))
    logger.debug(msg)
    x,y = '32', '41'
    msg = f'adding of str x: {x} and y: {y}=' + str(adding(x, y))
    logger.debug(msg)
    x,y = [32],[41]
    msg = f'adding of lists x: {x} and y: {y}=' + str(adding(x, y))
    logger.debug(msg)


