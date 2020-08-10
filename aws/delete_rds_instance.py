import time
import boto3
import botocore
from config import config
from logger import get_logger


# Config
KEY                  = config['AWS']['KEY']
SECRET               = config['AWS']['SECRET']
REGION               = config['AWS']['REGION']

DBINSTANCEIDENTIFIER = config['RDS']['DBINSTANCEIDENTIFIER']


# Setup logger
logger = get_logger('DELETE-RDS')


# Delete db func
def delete_rds_instance():
  rds = boto3.client(
    'rds',
    region_name=REGION,
    aws_access_key_id=KEY,
    aws_secret_access_key=SECRET
  )

  logger.info(f"Start deleting RDS {DBINSTANCEIDENTIFIER} instance")
  
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

  logger.info(f"Finish deleting RDS {DBINSTANCEIDENTIFIER} instance" + 
  '\n------------------------------------------------------------------------------------------')


# Run
def main():
  delete_db()


#
if __name__ == '__main__':
  main()