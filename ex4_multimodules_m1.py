import logging
from ex4_multimodules_m2 import sleep

def main():
    logging.basicConfig(filename=f'{__file__}.log', level=logging.DEBUG, filemode='w')
    logging.debug('Started')
    sleep()
    logging.debug('Finished')

if __name__ == '__main__':
    main()
