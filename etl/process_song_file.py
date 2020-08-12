import math
import pandas as pd
from db import insert_db

def extract_song_file(path):
  df = pd.read_json(str(path), lines=True)
  
  artist_data = []
  song_data   = []

  for value in df.values:
    num_songs, artist_id, artist_latitude, \
    artist_longitude, artist_location, \
    artist_name, song_id, \
    title, duration, year = value

    artist_data.append((artist_id, artist_name, artist_location, artist_latitude, artist_longitude))
    song_data.append((song_id, title, artist_id, year, duration))

  return (artist_data, song_data)

def transform_artist_data(artists):
  return [
    (
      str(artist[0]), str(artist[1]),
      str(artist[2]) if artist[2] else None,
      artist[3]
        if not math.isnan(artist[3]) and not math.isnan(artist[4])
        else None,
      artist[4]
        if not math.isnan(artist[3]) and not math.isnan(artist[4])
        else None
    ) for artist in artists]

def transform_song_data(songs):
  return [
    (
      str(song[0]), str(song[1]), str(song[2]),
      song[3] if song[3] > 1900 else None,
      song[4]
    ) for song in songs]

def process_song_file(conn, path):
  
  # Extract
  artist_data, song_data  = extract_song_file(path)

  # Transform
  transformed_artist_data = transform_artist_data(artist_data)
  transformed_song_data   = transform_song_data(song_data)
  
  # Load
  insert_db(conn, 'artist', transformed_artist_data)
  insert_db(conn, 'song', transformed_song_data)
