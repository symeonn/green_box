import logging
import os

logging.basicConfig(format='%(asctime)s :: %(levelname)s: %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.warning('And this, too')

logging.info(os.path.basename(__file__))
logging.info(os.path.basename(__name__))
