import os
import configparser
from db import setup_db

config = configparser.ConfigParser()
config.read_file(open(os.path.join(os.path.dirname(__file__), 'config.ini')))

LOG = config.get('LOG','LOG')

def main():
  # Reset file log
  open(LOG, 'w').close()

  setup_db()

if __name__ == '__main__':
  main()