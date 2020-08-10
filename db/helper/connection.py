import sys
sys.path.append('../')
from logger import get_logger

import os
import logging
import psycopg2
import configparser


# Config
config = configparser.ConfigParser()
config.read_file(open(os.path.join(os.path.dirname(__file__), '../../config.ini')))

DBNAME     = config.get('DB', 'DBNAME')
DBUSERNAME = config.get('DB','DBUSERNAME')
DBPASSWORD = config.get('DB','DBPASSWORD')
DBHOST     = config.get('DB','DBHOST')
DBPORT     = config.getint('DB','DBPORT')


# Setup logger
logger = get_logger('CONNECT-DB')


def connect_to_db(autocommit=True):
  logger.info(f"Start connecting to {DBNAME} DB")

  try:
    conn = psycopg2.connect(
        database=DBNAME,
        user=DBUSERNAME,
        password=DBPASSWORD,
        host=DBHOST,
        port=DBPORT
    )

    conn.set_session(autocommit=autocommit)

    logger.info(f"Successfully connect to {DBNAME} DB")

    return conn
  except psycopg2.Error as e:
    logger.error(e)
    return None

def close_connection(conn):
  logger.info(f"Start closing connection to {DBNAME} DB")

  try:
    conn.close()
  except psycopg2.Error as e:
    logger.error(e)

  logger.info(f"Successfully close connection to {DBNAME} DB")
  return None