import math
import pandas as pd
from db import insert_db

def extract_log_file(path):
  df = pd.read_json(path, lines=True)

  time_data     = []
  user_data     = []
  playsong_data = []