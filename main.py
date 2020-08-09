import os
import configparser
from aws import setup_db_instance

config = configparser.ConfigParser()
config.read_file(open(os.path.join(os.path.dirname(__file__), 'config.ini')))

LOG = config.get('LOG','LOG')

def main():
  # Reset file log
  open(LOG, 'w').close()

  setup_db_instance()

if __name__ == '__main__':
  main()