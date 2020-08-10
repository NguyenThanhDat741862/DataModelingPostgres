from logger import get_logger
from .helper import connect_to_db, close_connection, execute_sql
from .queries import database_drop, database_create

# Setup logger
logger = get_logger('CREATE-DB')

def create_db():
  logger.info(f"Start creating DB")

  conn = connect_to_db(True)

  execute_sql(conn, database_drop, False)
  execute_sql(conn, database_create, False)

  close_connection(conn)

  logger.info(f"Finish creating DB" +
  '\n------------------------------------------------------------------------------------------')