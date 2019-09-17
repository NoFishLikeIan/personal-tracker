import os

from datetime import datetime
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from loguru import logger
from lenses import lens

from .errors import InvalidArguments, FailedDatabaseConnection, error_handler

from .setup import set_logger_path, is_production, port
from .auth import auth
from .db import connect_to_db, assert_db
from .utils.update_parser import keyword_mapping, get_message
from .utils.date_utils import get_today
from .utils.db_utils import is_ok

# db init
collection, db = connect_to_db()

# app init
app_config = {
    'port': port,
    'debug': not is_production,
}
app = Flask(__name__)


app.errorhandler(InvalidArguments)(error_handler)
app.errorhandler(FailedDatabaseConnection)(error_handler)


# routes
@app.route('/')
def home():
    return "Maronnn, I'm running!"


@app.route('/auth')
@auth.login_required
def handshake():
    return f'Hello there, {auth.username()}'


@app.route('/get_daily')
@auth.login_required
@assert_db(collection)
def get_daily_data():
    today_id = get_today()
    data_today = collection.find_one({'date': today_id})

    parsed_data = lens['_id'].modify(str)(data_today)

    return {
        'succ': 1. if data_today else 0.,
        'data': parsed_data
    }


@app.route('/daily_data', methods=['POST'])
@auth.login_required
@assert_db(collection)
def handle_daily_data():
    today_id = get_today()
    message = get_message(request.data)
    data_today = collection.find_one({'date': today_id}) or {}

    if len(message) == 0:
        raise InvalidArguments('No message passed')

    _, update = keyword_mapping(message)
    updated = update(data_today)
    updated['date'] = today_id

    result = collection.replace_one({'date': today_id}, updated, upsert=True)
    succ = is_ok(result.raw_result)

    return jsonify({
        'ok': succ,
        'updated': today_id
    })
