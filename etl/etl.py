import os
from config import config
from logger import get_logger
from db import connect_to_db, close_connection
from .process_song_file import process_song_file


# Config
DATASONG = config['DATA']['DATASONG']


# Setup logger
logger = get_logger('PROCESS-DATA')


def process_data(path, func):
  logger.info(f"Start processing '{path}' data")

  files = [os.path.join(dirpath, filename) for (dirpath, dirnames, filenames) in os.walk(path) for filename in filenames if filenames]
  file_amount = len(files)

  logger.info(f"'{file_amount}' files found in '{path}'")

  conn = connect_to_db()

  for i, file in enumerate(files, 1):
    func(conn, file)
    
    logger.info(f'{i}/{file_amount} files processed.')

  close_connection(conn)
  logger.info(f"Finish processing '{path}' data")

def etl():
  process_data(DATASONG, process_song_file)
  