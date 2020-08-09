import sys
sys.path.append('../')
from logger import get_logger
from helper import connect_to_db, close_connection, execute_sql
from queries import database_drop, database_create, \
                    songplay_table_drop, \
                    user_table_drop, \
                    song_table_drop, \
                    artist_table_drop, \
                    time_table_drop, \
                    songplay_table_create, \
                    user_table_create, \
                    song_table_create, \
                    artist_table_create, \
                    time_table_create

import psycopg2

# Setup logger
logger = get_logger('CREATE-SCHEMA')

def create_db_schema():
  logger.info(f"Start creating DB schema")

  conn = connect_to_db()

  execute_sql(conn, database_drop, False)
  execute_sql(conn, database_create, False)

  execute_sql(conn, user_table_drop, False)
  execute_sql(conn, song_table_drop, False)
  execute_sql(conn, artist_table_drop, False)
  execute_sql(conn, time_table_drop, False)
  execute_sql(conn, songplay_table_drop, False)

  execute_sql(conn, time_table_create, False)
  execute_sql(conn, user_table_create, False)
  execute_sql(conn, artist_table_create, False)
  execute_sql(conn, song_table_create, False)
  execute_sql(conn, songplay_table_create, False)

  close_connection(conn)

  logger.info(f"Finish creating DB schema" +
  '\n------------------------------------------------------------------------------------------')

create_db_schema()