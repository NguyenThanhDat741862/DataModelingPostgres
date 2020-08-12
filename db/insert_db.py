from .connection import execute_sql
from .queries import songplay_table_insert, \
                      song_table_insert, \
                      artist_table_insert, \
                      time_table_insert, \
                      user_table_insert


table_insert_sql = {
  "songplay" : songplay_table_insert,
  "song"     : song_table_insert,
  "artist"   : artist_table_insert,
  "time"     : time_table_insert,
  "user"     : user_table_insert,
}

def insert_db(conn, table, rows):
  sql = table_insert_sql[table]

  for row in rows:
    execute_sql(conn, sql, False, row)

  conn.commit()
