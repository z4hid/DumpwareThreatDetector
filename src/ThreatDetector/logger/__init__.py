import logging
import os
from from_root import from_root
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log'
logs_path = os.path.join(from_root(), 'logs', LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
)