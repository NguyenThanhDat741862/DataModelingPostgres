import time
import boto3
import botocore
from config import config
from logger import get_logger


# Config
KEY                     = config['AWS']['KEY']
SECRET                  = config['AWS']['SECRET']
REGION                  = config['AWS']['REGION']

DBNAME                  = config['RDS']['DBNAME']
DBINSTANCEIDENTIFIER    = config['RDS']['DBINSTANCEIDENTIFIER']
ALLOCATEDSTORAGE        = config['RDS']['ALLOCATEDSTORAGE']
DBINSTANCECLASS         = config['RDS']['DBINSTANCECLASS']
ENGINE                  = config['RDS']['ENGINE']
ENGINEVERSION           = config['RDS']['ENGINEVERSION']
MASTERUSERNAME          = config['RDS']['MASTERUSERNAME']
MASTERUSERPASSWORD      = config['RDS']['MASTERUSERPASSWORD']
VPCSECURITYGROUPIDS     = config['RDS']['VPCSECURITYGROUPIDS']
AVAILABILITYZONE        = config['RDS']['AVAILABILITYZONE']
BACKUPRETENTIONPERIOD   = config['RDS']['BACKUPRETENTIONPERIOD']
DBPORT                  = config['RDS']['DBPORT']
MULTIAZ                 = config['RDS']['MULTIAZ']
AUTOMINORVERSIONUPGRADE = config['RDS']['AUTOMINORVERSIONUPGRADE']
PUBLICLYACCESSIBLE      = config['RDS']['PUBLICLYACCESSIBLE']
STORAGETYPE             = config['RDS']['STORAGETYPE']


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
