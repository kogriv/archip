import logging.config
from oop_logging_settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('oopushka_logger')
logger.debug('**** 001  parametric polymorphism sample *******')

class Figure:
    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        # print('Figure __init__')
        logger.debug('Figure __init__')

    def draw(self):
        # print('Figure draw pass')
        logger.debug('Figure draw pass')
        pass


class Ellipse(Figure):
    def draw(self):
        msg = f"Drawing an ellipse from ({self.x}, {self.y}) with color {self.color} and width {self.width}"
        # print(msg)
        logger.debug(msg)

class AsymmetricEllipse(Ellipse):
    def draw(self):
        msg = f"Drawing an asymmetric ellipse from ({self.x}, {self.y}) with color {self.color} and width {self.width}"
        # print(msg)
        logger.debug(msg)

