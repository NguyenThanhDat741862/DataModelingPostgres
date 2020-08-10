from logger import get_logger
from .connection import connect_to_db, close_connection, execute_sql
from .queries import songplay_table_drop, \
                      user_table_drop, \
                      song_table_drop, \
                      artist_table_drop, \
                      time_table_drop, \
                      songplay_table_create, \
                      user_table_create, \
                      song_table_create, \
                      artist_table_create, \
                      time_table_create


# Setup logger
logger = get_logger('CREATE-SCHEMA')


def create_schema():
  logger.info(f"Start creating Schema")

  conn = connect_to_db(False)

  execute_sql(conn, user_table_drop, False)
  execute_sql(conn, song_table_drop, False)
  execute_sql(conn, artist_table_drop, False)
  execute_sql(conn, time_table_drop, False)
  execute_sql(conn, songplay_table_drop, False)
  conn.commit()

  execute_sql(conn, time_table_create, False)
  execute_sql(conn, user_table_create, False)
  execute_sql(conn, artist_table_create, False)
  execute_sql(conn, song_table_create, False)
  execute_sql(conn, songplay_table_create, False)
  conn.commit()

  close_connection(conn)

  logger.info(f"Finish creating Schema")
