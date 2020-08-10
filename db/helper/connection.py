import psycopg2
from config import config 
from logger import get_logger


# Config
DBNAME     = config['DB']['DBNAME']
DBUSERNAME = config['DB']['DBUSERNAME']
DBPASSWORD = config['DB']['DBPASSWORD']
DBHOST     = config['DB']['DBHOST']
DBPORT     = config['DB']['DBPORT']


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