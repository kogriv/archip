import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel('DEBUG')
logger.debug('test logrecord DEBUG')
logger.warning('test logrecord WARNING')