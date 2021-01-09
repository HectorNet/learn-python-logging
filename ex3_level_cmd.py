import argparse
import logging


parser = argparse.ArgumentParser()
parser.add_argument('--loglevel', default='WARNING')
# parser.add_argument('--loglevel', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='WARNING')
args = parser.parse_args()

numeric_level = getattr(logging, args.loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError(f'Invalid log level: {args.loglevel}')
logging.basicConfig(level=numeric_level)

logging.debug('debug log')
logging.info('info log')
logging.warning('warning log')
logging.error('error log')
