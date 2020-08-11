import os
import configparser

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

parser = configparser.ConfigParser()
parser.read_file(open(os.path.join(ROOT_DIR, './config.ini')))

config = {
  "ROOT_DIR": ROOT_DIR,
  "DB": {
    "DB_NAME"     : parser.get('DB', 'DB_NAME'),
    "DB_USERNAME" : parser.get('DB', 'DB_USERNAME'),
    "DB_PASSWORD" : parser.get('DB', 'DB_PASSWORD'),
    "DB_HOST"     : parser.get('DB', 'DB_HOST'),
    "DB_PORT"     : parser.getint('DB','DB_PORT')
  },

  "DATA": {
    "DATA_SONG" : os.path.join(ROOT_DIR, f"./{parser.get('DATA', 'DATA_SONG')}"),
    "DATA_LOG"  : os.path.join(ROOT_DIR, f"./{parser.get('DATA', 'DATA_LOG')}")
  },

  "LOG": {
    "LOG" : os.path.join(ROOT_DIR, f"./{parser.get('LOG','LOG')}")
  },

  "OPT": {
    "DB_ON_CLOUD" : parser.get('OPT','DB_ON_CLOUD')
  },

  "AWS": {
    "KEY"    : parser.get('AWS','KEY'),
    "SECRET" : parser.get('AWS','SECRET'),
    "REGION" : parser.get('AWS','REGION')
  },

  "RDS": {
    "DB_NAME"                  : parser.get('RDS','DB_NAME'),
    "DB_INSTANCE_IDENTIFIER"    : parser.get('RDS','DB_INSTANCE_IDENTIFIER'),
    "ALLOCATED_STORAGE"        : parser.getint('RDS','ALLOCATED_STORAGE'),
    "DB_INSTANCE_CLASS"         : parser.get('RDS','DB_INSTANCE_CLASS'),
    "ENGINE"                  : parser.get('RDS','ENGINE'),
    "ENGINE_VERSION"           : parser.get('RDS','ENGINE_VERSION'),
    "MASTER_USERNAME"          : parser.get('RDS','MASTER_USERNAME'),
    "MASTER_USER_PASSWORD"      : parser.get('RDS','MASTER_USER_PASSWORD'),
    "VPC_SECURITY_GROUP_IDS"     : parser.get('RDS','VPC_SECURITY_GROUP_IDS'),
    "AVAILABILITY_ZONE"        : parser.get('RDS','AVAILABILITY_ZONE'),
    "BACKUP_RETENTION_PERIOD"   : parser.getint('RDS', 'BACKUP_RETENTION_PERIOD'),
    "DB_PORT"                  : parser.getint('RDS','DB_PORT'),
    "MULTI_AZ"                 : parser.getboolean('RDS', 'MULTI_AZ'),
    "AUTO_MINOR_VERSION_UPGRADE" : parser.getboolean('RDS','AUTO_MINOR_VERSION_UPGRADE'),
    "PUBLICLY_ACCESSIBLE"      : parser.getboolean('RDS','PUBLICLY_ACCESSIBLE'),
    "STORAGE_TYPE"             : parser.get('RDS','STORAGE_TYPE')
  }
}
