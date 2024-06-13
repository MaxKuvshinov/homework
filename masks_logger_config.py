import os
import logging


log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)
logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
log_filename = os.path.join(log_dir, 'masks.log')
file_handler = logging.FileHandler(log_filename, mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)