import logging
from config import config


# Config
LOG = config['LOG']['LOG']


def get_logger(name):
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  handler = logging.FileHandler(LOG)
  handler.setLevel(logging.DEBUG)
  handler.setFormatter(formatter)
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)
  logger.addHandler(handler)

  return logger