"""logging setup presets"""



import logging
from logging.handlers import TimedRotatingFileHandler

import pathlib
from pathlib import Path

import os



def normal(name):
    """ALWAYS put __name__ as arg!!"""
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    file = Path(pathlib.Path.cwd(), 'logs', 'exc.log')
    logging.basicConfig(level=logging.WARNING, filename=file, filemode="a", format='%(asctime)s %(name)s %(levelname)s:%(message)s')
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")
    TimedRotatingFileHandler(filename=file, when='d', interval=1, backupCount=7)
    return logging.getLogger(name)

def debug(name):
    """ALWAYS put __name__ as arg!!"""
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    file = Path(pathlib.Path.cwd(), 'logs', 'full.log')
    logging.basicConfig(level=logging.DEBUG, filename=file, filemode="a", format='%(asctime)s %(name)s %(levelname)s:%(message)s')
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")
    TimedRotatingFileHandler(filename=file, when='d', interval=1, backupCount=7)
    return logging.getLogger(name)

def test(name):
    """ALWAYS put __name__ as arg!!"""
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    file = Path(pathlib.Path.cwd(), 'logs', 'test.log')
    logging.basicConfig(level=logging.INFO, filename=file, filemode="a", format='%(asctime)s %(name)s %(levelname)s:%(message)s')
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")
    TimedRotatingFileHandler(filename=file, when='d', interval=1, backupCount=7)
    return logging.getLogger(name)