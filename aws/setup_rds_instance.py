import os
import time
import boto3
import botocore
import configparser
from logger import get_logger


# Config
config = configparser.ConfigParser()
config.read_file(open(os.path.join(os.path.dirname(__file__), '../config.ini')))

KEY                     = config.get('AWS','KEY')
SECRET                  = config.get('AWS','SECRET')
REGION                  = config.get('AWS','REGION')

DBNAME                  = config.get('RDS','DBNAME')
DBINSTANCEIDENTIFIER    = config.get('RDS','DBINSTANCEIDENTIFIER')
ALLOCATEDSTORAGE        = config.getint('RDS','ALLOCATEDSTORAGE')
DBINSTANCECLASS         = config.get('RDS','DBINSTANCECLASS')
ENGINE                  = config.get('RDS','ENGINE')
ENGINEVERSION           = config.get('RDS','ENGINEVERSION')
MASTERUSERNAME          = config.get('RDS','MASTERUSERNAME')
MASTERUSERPASSWORD      = config.get('RDS','MASTERUSERPASSWORD')
VPCSECURITYGROUPIDS     = config.get('RDS','VPCSECURITYGROUPIDS')
AVAILABILITYZONE        = config.get('RDS','AVAILABILITYZONE')
BACKUPRETENTIONPERIOD   = config.getint('RDS', 'BACKUPRETENTIONPERIOD')
DBPORT                  = config.getint('RDS','DBPORT')
MULTIAZ                 = config.getboolean('RDS', 'MULTIAZ')
AUTOMINORVERSIONUPGRADE = config.getboolean('RDS','AUTOMINORVERSIONUPGRADE')
PUBLICLYACCESSIBLE      = config.getboolean('RDS','PUBLICLYACCESSIBLE')
STORAGETYPE             = config.get('RDS','STORAGETYPE')


# Setup logger
logger = get_logger('SETUP-RDS')


# Setup db
def setup_rds_instance():
  rds = boto3.client(
    'rds',
    region_name=REGION,
    aws_access_key_id=KEY,
    aws_secret_access_key=SECRET
  )

  logger.info(f"Start setting up RDS {DBINSTANCEIDENTIFIER} instance")
  
  try:
    response = rds.create_db_instance(
      DBName=DBNAME,
      DBInstanceIdentifier=DBINSTANCEIDENTIFIER,
      AllocatedStorage=ALLOCATEDSTORAGE,
      DBInstanceClass=DBINSTANCECLASS,
      Engine=ENGINE,
      EngineVersion=ENGINEVERSION,
      MasterUsername=MASTERUSERNAME,
      MasterUserPassword=MASTERUSERPASSWORD,
      VpcSecurityGroupIds=[VPCSECURITYGROUPIDS],
      AvailabilityZone=AVAILABILITYZONE,
      BackupRetentionPeriod=BACKUPRETENTIONPERIOD,
      Port=DBPORT,
      MultiAZ=MULTIAZ,
      AutoMinorVersionUpgrade=AUTOMINORVERSIONUPGRADE,
      PubliclyAccessible=PUBLICLYACCESSIBLE,
      StorageType=STORAGETYPE,
      Tags=[{'Key': 'DB', 'Value': 'PostgreSQL'}]
    )

    logger.info(f"Starting RDS instance with ID: {DBINSTANCEIDENTIFIER}")

  except botocore.exceptions.ClientError as e:
    if 'DBInstanceAlreadyExists' in e.message:
      logger.error(f"DB instance {DBINSTANCEIDENTIFIER} exists already, continuing to poll ...")
    else:
      raise

  while True:
    try:
      response = rds.describe_db_instances(DBInstanceIdentifier=DBINSTANCEIDENTIFIER)
      db_instance = response['DBInstances'][0]
      status = db_instance['DBInstanceStatus']

      logger.info(f"RDS {DBINSTANCEIDENTIFIER} instance is {status}")

      time.sleep(10)

      if status == 'available':
          host = db_instance['Endpoint']['Address']
          logger.info(f"RDS {DBINSTANCEIDENTIFIER} instance ready with host: {host}")
          logger.info(f"RDS {DBINSTANCEIDENTIFIER} instance info: {db_instance}")
          
          break

    except botocore.exceptions.ClientError as e:
      logger.error(e)
      raise

  logger.info(f"Finish setting up RDS {DBINSTANCEIDENTIFIER} instance" +
  '\n------------------------------------------------------------------------------------------')
