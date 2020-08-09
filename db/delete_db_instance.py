import os
import time
import logging
import boto3
import botocore
import configparser


# Config
config = configparser.ConfigParser()
config.read_file(open(os.path.join(os.path.dirname(__file__), '../config.ini')))

LOG                  = config.get('LOG','LOG')

KEY                  = config.get('AWS','KEY')
SECRET               = config.get('AWS','SECRET')
REGION               = config.get('AWS','REGION')

DBINSTANCEIDENTIFIER = config.get('RDS','DBINSTANCEIDENTIFIER')


# Setup logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler(LOG)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger = logging.getLogger('SETUP-RDS')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


# Delete db func
def delete_db():
  rds = boto3.client(
    'rds',
    region_name=REGION,
    aws_access_key_id=KEY,
    aws_secret_access_key=SECRET
  )

  logger.info(f"Start delete RDS {DBINSTANCEIDENTIFIER} instance")
  
  try:
    response = rds.delete_db_instance(
      DBInstanceIdentifier=DBINSTANCEIDENTIFIER,
      SkipFinalSnapshot=True,
      DeleteAutomatedBackups=True
    )

    logger.info(f"Deleting RDS instance with ID: {DBINSTANCEIDENTIFIER}")

  except botocore.exceptions.ClientError as e:
    logger.error(e)
    raise

  while True:
    try:
      rds.describe_db_instances(DBInstanceIdentifier=DBINSTANCEIDENTIFIER)
      
      logger.info(f"RDS {DBINSTANCEIDENTIFIER} instance is deleting")
      
      time.sleep(10)
    except botocore.exceptions.ClientError as e:
      logger.info(f"RDS {DBINSTANCEIDENTIFIER} instance is deleted")

      break

  logger.info(f"Finish delete RDS {DBINSTANCEIDENTIFIER} instance" + 
  '\n------------------------------------------------------------------------------------------')


# Run
def main():
  delete_db()


#
if __name__ == '__main__':
  main()