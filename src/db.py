from pymongo import MongoClient, errors
from loguru import logger
from functools import wraps

from .setup import is_production, db_name, collection_name, max_timeout
from .errors import FailedDatabaseConnection


def connect_to_db():
    try:
        logger.info(f'Connecting to db...')
        mongo_client_location = 'db' if is_production else 'localhost'

        client = MongoClient(mongo_client_location, 27017,
                             serverSelectionTimeoutMS=max_timeout)
        client.server_info()

        logger.info(
            f'...success! Now connected to {db_name}:{collection_name}')

        db = client[db_name]
        collection = db[collection_name]

        return collection, db

    except errors.ServerSelectionTimeoutError as err:
        logger.error(
            f'... connection timed out with the db, is it running? {err}')

        return None, None


def assert_db(collection):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if collection is None:
                raise FailedDatabaseConnection(
                    'Failed to ensablish db connection')

            return f(*args, **kwargs)

        return wrapped
    return decorator
