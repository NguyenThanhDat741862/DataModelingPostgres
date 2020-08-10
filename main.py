import os
import configparser
from aws import setup_rds_instance, delete_rds_instance
from db import create_db, create_schema

config = configparser.ConfigParser()
config.read_file(open(os.path.join(os.path.dirname(__file__), 'config.ini')))

LOG = config.get('LOG','LOG')
DBONCLOUD = config.get('OPT','DBONCLOUD')

def main():
  # Reset file log
  open(LOG, 'w').close()

  # if DBONCLOUD:
    # setup_rds_instance()
  
  # delete_rds_instance()

  create_db()
  create_schema()

if __name__ == '__main__':
  main()