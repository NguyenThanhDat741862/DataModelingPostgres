song_select = ("""
  SELECT song_id, artists.artist_id
  FROM songs JOIN artists ON songs.artist_id = artists.artist_id
  WHERE songs.title = %s
  AND artists.name = %s
  AND songs.duration = %s
""")