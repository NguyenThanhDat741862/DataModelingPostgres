import math
import pandas as pd
from db import select_song, insert_db

def extract_log_file(path):
  df = pd.read_json(str(path), dtype={"userId": object, "sessionId": object}, lines=True)

  # get rows which have NextSong value  
  df = df[df['page']=='NextSong']

  return ( 
    pd.to_datetime(df['ts'], unit='ms'),
    list(df[['userId', 'firstName', 'lastName', 'gender', 'level']].to_records(index=False)),
    list(zip(df[['song', 'artist', 'length']].to_records(index=False), df[['ts', 'userId', 'level', 'sessionId', 'location', 'userAgent']].to_records(index=False)))
  )

def transform_time_data(times_series):
  return [(time, time.hour, time.day, time.week, time.month, time.year, time.day_name()) for time in times_series]

def transform_playsong_data(playsongs, conn):
  result = []

  for i, playsong in enumerate(playsongs):
    query_result = select_song(conn, playsong[0])
    song_id, artist_id = None, None
    
    if query_result:
      song_id, artist_id = query_result[0]

    result.append((i, pd.to_datetime(playsong[1][0], unit='ms'), *list(playsong[1])[1:3], song_id, artist_id, *list(playsong[1])[3:]))

  return result

def process_log_file(conn, path):
  
  # Extract
  time_data, user_data, playsong_data = extract_log_file(path)

  # Transform
  transformed_time_data     = transform_time_data(time_data)
  transformed_playsong_data = transform_playsong_data(playsong_data, conn)

  # Load
  insert_db(conn, 'time', transformed_time_data)
  insert_db(conn, 'user', user_data)
  insert_db(conn, 'songplay', transformed_playsong_data)

