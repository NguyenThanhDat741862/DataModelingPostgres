songplay_table_insert = ("""
  INSERT INTO songplays
  (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
  ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
  INSERT INTO users
  (user_id, first_name, last_name, gender, level)
  VALUES (%s, %s, %s, %s, %s)
  ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""
  INSERT INTO songs
  (song_id, title, artist_id, year, duration)
  VALUES (%s, %s, %s, %s, %s)
  ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
  INSERT INTO artists
  (artist_id, name, location, lattitude, longitude)
  VALUES (%s, %s, %s, %s, %s)
  ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_insert = ("""
  INSERT INTO time
  (start_time, hour, day, week, month, year, weekday)
  VALUES (%s, %s, %s, %s, %s, %s, %s)
  ON CONFLICT (start_time) DO NOTHING;
""")