import os
import configparser

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

parser = configparser.ConfigParser()
parser.read_file(open(os.path.join(ROOT_DIR, './config.ini')))

config = {
  "ROOT_DIR": ROOT_DIR,
  "DB": {
    "DBNAME"     : parser.get('DB', 'DBNAME'),
    "DBUSERNAME" : parser.get('DB', 'DBUSERNAME'),
    "DBPASSWORD" : parser.get('DB', 'DBPASSWORD'),
    "DBHOST"     : parser.get('DB', 'DBHOST'),
    "DBPORT"     : parser.getint('DB','DBPORT')
  },

  "DATA": {
    "DATACSV"  : os.path.join(ROOT_DIR, f"./{parser.get('DATA', 'DATACSV')}"),
    "DATAJSON" : os.path.join(ROOT_DIR, f"./{parser.get('DATA', 'DATAJSON')}")
  },

  "LOG": {
    "LOG" : os.path.join(ROOT_DIR, f"./{parser.get('LOG','LOG')}")
  },

  "OPT": {
    "DBONCLOUD" : parser.get('OPT','DBONCLOUD')
  },

  "AWS": {
    "KEY"    : parser.get('AWS','KEY'),
    "SECRET" : parser.get('AWS','SECRET'),
    "REGION" : parser.get('AWS','REGION')
  },

  "RDS": {
    "DBNAME"                  : parser.get('RDS','DBNAME'),
    "DBINSTANCEIDENTIFIER"    : parser.get('RDS','DBINSTANCEIDENTIFIER'),
    "ALLOCATEDSTORAGE"        : parser.getint('RDS','ALLOCATEDSTORAGE'),
    "DBINSTANCECLASS"         : parser.get('RDS','DBINSTANCECLASS'),
    "ENGINE"                  : parser.get('RDS','ENGINE'),
    "ENGINEVERSION"           : parser.get('RDS','ENGINEVERSION'),
    "MASTERUSERNAME"          : parser.get('RDS','MASTERUSERNAME'),
    "MASTERUSERPASSWORD"      : parser.get('RDS','MASTERUSERPASSWORD'),
    "VPCSECURITYGROUPIDS"     : parser.get('RDS','VPCSECURITYGROUPIDS'),
    "AVAILABILITYZONE"        : parser.get('RDS','AVAILABILITYZONE'),
    "BACKUPRETENTIONPERIOD"   : parser.getint('RDS', 'BACKUPRETENTIONPERIOD'),
    "DBPORT"                  : parser.getint('RDS','DBPORT'),
    "MULTIAZ"                 : parser.getboolean('RDS', 'MULTIAZ'),
    "AUTOMINORVERSIONUPGRADE" : parser.getboolean('RDS','AUTOMINORVERSIONUPGRADE'),
    "PUBLICLYACCESSIBLE"      : parser.getboolean('RDS','PUBLICLYACCESSIBLE'),
    "STORAGETYPE"             : parser.get('RDS','STORAGETYPE')
  }
}
