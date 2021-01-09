import logging

log_filepath = f"{__file__}.log"
with open(log_filepath, mode='w', encoding='utf-8'):
  logging.basicConfig(filename=log_filepath, level=logging.DEBUG)

# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)  # after Python3.9
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
