'''
@author: dstaines
'''
import os
from ensembl_prodinf.config import load_yaml


config_file_path = os.environ.get('EVENT_CONFIG_PATH')
if config_file_path:
    file_config = load_yaml(config_file_path)
else:
    file_config = {}

event_lookup = os.environ.get("EVENT_LOOKUP_FILE",
                              file_config.get('event_lookup_file', "./event_lookup.json"))
process_lookup = os.environ.get("PROCESS_LOOKUP_FILE",
                                file_config.get('process_lookup_file', "./process_lookup.json"))
report_server = os.environ.get("REPORT_SERVER",
                               file_config.get('report_server', "amqp://guest:guest@localhost:5672/%2F"))
report_exchange = os.environ.get("REPORT_EXCHANGE",
                                 file_config.get('report_exchange', 'report_exchange'))
event_uri = os.environ.get("EVENT_URI",
                           file_config.get('event_uri', 'http://127.0.0.1:5004/'))
