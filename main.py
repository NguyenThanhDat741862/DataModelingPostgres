import os
from config import config
from aws import setup_rds_instance, delete_rds_instance
from db import create_db, create_schema
from etl import etl

LOG         = config['LOG']['LOG']
DB_ON_CLOUD = config['OPT']['DB_ON_CLOUD']

def main():
  # delete_rds_instance()

  # if DB_ON_CLOUD:
  #   setup_rds_instance()

  create_db()
  create_schema()

  etl()

if __name__ == '__main__':
  # Reset file log
  open(LOG, 'w').close()
  
  main()