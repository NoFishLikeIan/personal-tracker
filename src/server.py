import os

from flask import Flask
from dotenv import load_dotenv
from loguru import logger

from .setup import set_logger_path
from .auth import auth

# logger
logger_path = set_logger_path()
logger.add(os.path.join(logger_path, 'server.log'),
           format="{time:YYYY-MM-DD at HH:mm:ss} {level} - {message}", level='INFO', retention='1 day')
logger.add(os.path.join(logger_path, 'error.log'),
           format='{time:YYYY-MM-DD at HH:mm:ss} {level} - {message}', level='ERROR', retention='10 days')

# .env variables
load_dotenv()
PORT = os.getenv('PORT', 5000)
DEBUG = os.getenv('DEBUG', False)
HOST = os.getenv('HOST', '0.0.0.0')
THREADED = os.getenv('THREADED', False)

app_config = {
    'port': PORT,
    'debug': DEBUG,
    'host': HOST,
    'threaded': THREADED
}
# app
app = Flask(__name__)

# routes


@app.route('/')
def nothing():
    return 'nothing here'


@app.route('/home')
@auth.login_required
def home():
    return f'Hello there, {auth.username()}'
