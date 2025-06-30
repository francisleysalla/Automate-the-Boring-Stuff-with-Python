import logging

logging.basicConfig(level = logging.DEBUG, 
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug('Some minor code or debugging details')
logging.info('An event happened')
logging.warning("Something could go wrong")
logging.error("An error occurred")
logging.critical("The program is unable to recover from the error")