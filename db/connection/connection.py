import psycopg2
from config import config 
from logger import get_logger


# Config
DB_NAME     = config['DB']['DB_NAME']
DB_USERNAME = config['DB']['DB_USERNAME']
DB_PASSWORD = config['DB']['DB_PASSWORD']
DB_HOST     = config['DB']['DB_HOST']
DB_PORT     = config['DB']['DB_PORT']


# Setup logger
logger = get_logger('CONNECT-DB')


def connect_to_db(autocommit=True):
  try:
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    conn.set_session(autocommit=autocommit)

    logger.info(f"Successfully connect to {DB_NAME} DB")

    return conn
  except psycopg2.Error as e:
    logger.error(e)
    return None

def close_connection(conn):
  try:
    conn.close()
  except psycopg2.Error as e:
    logger.error(e)

  logger.info(f"Successfully close connection to {DB_NAME} DB")
  return None