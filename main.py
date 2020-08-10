import os
from config import config
from aws import setup_rds_instance, delete_rds_instance
from db import create_db, create_schema

LOG       = config['LOG']['LOG']
DBONCLOUD = config['OPT']['DBONCLOUD']

def main():
  # if DBONCLOUD:
  #   setup_rds_instance()
  
  # delete_rds_instance()

  create_db()
  create_schema()

if __name__ == '__main__':
  # Reset file log
  open(LOG, 'w').close()
  
  main()