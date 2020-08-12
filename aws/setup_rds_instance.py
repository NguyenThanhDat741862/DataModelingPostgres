import time
import boto3
import botocore
from config import config
from logger import get_logger


# Config
KEY                     = config['AWS']['KEY']
SECRET                  = config['AWS']['SECRET']
REGION                  = config['AWS']['REGION']

DB_NAME                    = config['RDS']['DB_NAME']
DB_INSTANCE_IDENTIFIER     = config['RDS']['DB_INSTANCE_IDENTIFIER']
ALLOCATED_STORAGE          = config['RDS']['ALLOCATED_STORAGE']
DB_INSTANCE_CLASS          = config['RDS']['DB_INSTANCE_CLASS']
ENGINE                     = config['RDS']['ENGINE']
ENGINE_VERSION             = config['RDS']['ENGINE_VERSION']
MASTER_USERNAME            = config['RDS']['MASTER_USERNAME']
MASTER_USER_PASSWORD       = config['RDS']['MASTER_USER_PASSWORD']
VPC_SECURITY_GROUP_IDS     = config['RDS']['VPC_SECURITY_GROUP_IDS']
AVAILABILITY_ZONE          = config['RDS']['AVAILABILITY_ZONE']
BACKUP_RETENTION_PERIOD    = config['RDS']['BACKUP_RETENTION_PERIOD']
DB_PORT                    = config['RDS']['DB_PORT']
MULTI_AZ                   = config['RDS']['MULTI_AZ']
AUTO_MINOR_VERSION_UPGRADE = config['RDS']['AUTO_MINOR_VERSION_UPGRADE']
PUBLICLY_ACCESSIBLE        = config['RDS']['PUBLICLY_ACCESSIBLE']
STORAGE_TYPE               = config['RDS']['STORAGE_TYPE']


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

  logger.info(f"Start setting up RDS {DB_INSTANCE_IDENTIFIER} instance")
  
  try:
    response = rds.create_db_instance(
      DBName=DB_NAME,
      DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER,
      AllocatedStorage=ALLOCATED_STORAGE,
      DBInstanceClass=DB_INSTANCE_CLASS,
      Engine=ENGINE,
      EngineVersion=ENGINE_VERSION,
      MasterUsername=MASTER_USERNAME,
      MasterUserPassword=MASTER_USER_PASSWORD,
      VpcSecurityGroupIds=[VPC_SECURITY_GROUP_IDS],
      AvailabilityZone=AVAILABILITY_ZONE,
      BackupRetentionPeriod=BACKUP_RETENTION_PERIOD,
      Port=DB_PORT,
      MultiAZ=MULTI_AZ,
      AutoMinorVersionUpgrade=AUTO_MINOR_VERSION_UPGRADE,
      PubliclyAccessible=PUBLICLY_ACCESSIBLE,
      StorageType=STORAGE_TYPE,
      Tags=[{'Key': 'DB', 'Value': 'PostgreSQL'}]
    )

    logger.info(f"Starting RDS instance with ID: {DB_INSTANCE_IDENTIFIER}")

  except botocore.exceptions.ClientError as e:
    logger.error(e)
    raise

  while True:
    try:
      response = rds.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER)
      db_instance = response['DBInstances'][0]
      status = db_instance['DBInstanceStatus']

      logger.info(f"RDS {DB_INSTANCE_IDENTIFIER} instance is {status}")

      time.sleep(10)

      if status == 'available':
          host = db_instance['Endpoint']['Address']
          logger.info(f"RDS {DB_INSTANCE_IDENTIFIER} instance ready with host: {host}")
          logger.info(f"RDS {DB_INSTANCE_IDENTIFIER} instance info: {db_instance}")
          
          break

    except botocore.exceptions.ClientError as e:
      logger.error(e)
      raise

  logger.info(f"Finish setting up RDS {DB_INSTANCE_IDENTIFIER} instance")
