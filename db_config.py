import os
from ensembl_prodinf.config import load_yaml


config_file_path = os.environ.get('DBCOPY_CONFIG_PATH')
if config_file_path:
    file_config = load_yaml(config_file_path)
else:
    file_config = {}

DEBUG = str(os.environ.get("DEBUG", file_config.get('debug', 'False')))
if DEBUG.lower() in ("f", "false"):
    DEBUG = False
elif DEBUG.lower() in ("t", "true"):
    DEBUG = True

HIVE_ANALYSIS = os.environ.get("HIVE_ANALYSIS",
                               file_config.get('hive_analysis', 'copy_database'))

HIVE_URI = os.environ.get("HIVE_URI",
                          file_config.get('hive_uri'))

SERVER_URIS_FILE = os.environ.get("SERVER_URIS_FILE",
                                  file_config.get('server_uris_file', './server_uris.json'))
