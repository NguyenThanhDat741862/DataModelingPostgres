from .connection import execute_sql
from .queries import song_select

def select_song(conn, condition):
  result = execute_sql(conn, song_select, True, condition)

  conn.commit()

  return result
  