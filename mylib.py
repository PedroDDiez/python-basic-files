# mylib.py
import logging

def do_something():
    logger = logging.getLogger(__name__)
    logger.info('Doing something')
