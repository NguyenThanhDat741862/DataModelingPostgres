# Fact table
songplay_table_create = ("""
  CREATE TABLE IF NOT EXISTS songplays
  (songplay_id int PRIMARY KEY, 
  start_time date REFERENCES time(start_time), 
  user_id int NOT NULL REFERENCES users(user_id), 
  level text, 
  song_id text REFERENCES songs(song_id), 
  artist_id text REFERENCES artists(artist_id), 
  session_id int, 
  location text, 
  user_agent text)
""")

# Dimension table
user_table_create = ("""
  CREATE TABLE IF NOT EXISTS users
  (user_id int PRIMARY KEY, 
  first_name text NOT NULL, 
  last_name text NOT NULL, 
  gender text, 
  level text)
""")

song_table_create = ("""
  CREATE TABLE IF NOT EXISTS songs
  (song_id text PRIMARY KEY, 
  title text NOT NULL, 
  artist_id text NOT NULL REFERENCES artists(artist_id), 
  year int, 
  duration float NOT NULL)
""")

artist_table_create = ("""
  CREATE TABLE IF NOT EXISTS artists
  (artist_id text PRIMARY KEY,
    name text NOT NULL, 
    location text, 
    lattitude float, 
    longitude float)
""")

time_table_create = ("""
  CREATE TABLE IF NOT EXISTS time
  (start_time date PRIMARY KEY,
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday text)
""")