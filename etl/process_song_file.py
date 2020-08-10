import math
import pandas as pd
from db import insert_db

def extract_song_file(path):
  df = pd.read_json(path, lines=True)
  
  artist_data = []
  song_data   = []

  for value in df.values:
    num_songs, artist_id, artist_latitude, \
    artist_longitude, artist_location, \
    artist_name, song_id, \
    title, duration, year = value

    artist_data.append({
      "artist_id"        : artist_id,
      "artist_name"      : artist_name,
      "artist_location"  : artist_location,
      "artist_longitude" : artist_longitude,
      "artist_latitude"  : artist_latitude
    })

    song_data.append({
      "song_id"   : song_id,
      "title"     : title,
      "artist_id" : artist_id,
      "year"      : year,
      "duration"  : duration
    })

  return {
    "artist_data": artist_data,
    "song_data": song_data
  }

def transform_artist_data(artists):
  return [ \
    ( \
      str(artist['artist_id']), \
      str(artist['artist_name']), \
      str(artist['artist_location']) if artist['artist_location'] else None, \
      artist['artist_latitude'] \
        if not math.isnan(artist['artist_latitude']) and not math.isnan(artist['artist_longitude']) \
        else None, \
      artist['artist_longitude'] \
        if not math.isnan(artist['artist_latitude']) and not math.isnan(artist['artist_longitude']) \
        else None, \
    ) for artist in artists]

def transform_song_data(songs):
  return [ \
    ( \
      str(song['song_id']), \
      str(song['title']), \
      str(song['artist_id']), \
      song['year'] if song['year'] > 1900 else None, \
      song['duration'] \
    ) for song in songs]

def process_song_file(conn, path):
  df = pd.read_json(path, lines=True)
  
  # Extract
  artist_data, song_data  = extract_song_file(str(path)).values()
  
  # Transform
  transformed_artist_data = transform_artist_data(artist_data)
  transformed_song_data   = transform_song_data(song_data)
  
  # Load
  insert_db(conn, 'artist', transformed_artist_data)
  insert_db(conn, 'song', transformed_song_data)
