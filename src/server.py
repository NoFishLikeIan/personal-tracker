import os

from flask import Flask
from dotenv import load_dotenv
from loguru import logger

from .setup import set_logger_path, is_production, port
from .auth import auth
from .db import connect_to_db

# db init
collection, db = connect_to_db()

# app init
app_config = {
    'port': port,
    'debug': not is_production,
}
app = Flask(__name__)

# routes
@app.route('/')
def home():
    return "Maronnn, I'm running!"


@app.route('/auth')
@auth.login_required
def handshake():
    return f'Hello there, {auth.username()}'


@app.route('/daily_data', method=['POST', 'GET', 'DELETE'])
@auth.login_required
def handle_daily_data():
    pass
