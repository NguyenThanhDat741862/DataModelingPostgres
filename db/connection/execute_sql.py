import psycopg2
from logger import get_logger


# Setup logger
logger = get_logger('EXECUTE-SQL')


def execute_sql(conn, sql, is_fetchable, data=None):
  try:
    cur = conn.cursor()
    
    if data:
      cur.execute(sql, data)
    else:
      cur.execute(sql)
  except psycopg2.Error as e:
    logger.error(e)

    return None

  result = cur.fetchall() if is_fetchable else None
  cur.close()

  logged_sql = sql.replace("\n", " ").strip()

  logger.info(f'Executing: "{logged_sql}" "{data if data else ""}"')

  return result