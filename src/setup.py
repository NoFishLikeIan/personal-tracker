import os
from dotenv import load_dotenv
from loguru import logger


def set_logger_path():
    log_path = os.getenv('LOG_PATH')

    if log_path is None:
        if not os.path.isdir('logs/'):
            os.makedirs('logs/')
        log_path = 'logs/'
    return log_path


load_dotenv()
# logger
logger_path = set_logger_path()
logger.add(os.path.join(logger_path, 'server.log'),
           format="{time:YYYY-MM-DD at HH:mm:ss} {level} - {message}", level='INFO', retention='1 day')
logger.add(os.path.join(logger_path, 'error.log'),
           format='{time:YYYY-MM-DD at HH:mm:ss} {level} - {message}', level='ERROR', retention='10 days')

is_production = int(os.getenv('PROD', 0)) > 0
port = os.getenv('PORT', 4000)
db_name = os.getenv('DB', 'tracker_db')
collection_name = os.getenv('COLL', 'tracker_collection')
max_timeout = 30 if is_production else 5
