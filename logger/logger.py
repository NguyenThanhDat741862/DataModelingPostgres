import os
import logging
import configparser


# Config
config = configparser.ConfigParser()
config.read_file(open(os.path.join(os.path.dirname(__file__), '../config.ini')))

LOG = os.path.join(os.path.dirname(__file__), f"../{config.get('LOG','LOG')}")

def get_logger(name):
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  handler = logging.FileHandler(LOG)
  handler.setLevel(logging.DEBUG)
  handler.setFormatter(formatter)
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)
  logger.addHandler(handler)

  return logger