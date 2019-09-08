import os
import flask_httpauth

from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()
PASS = os.getenv('PASS', '')
ADMIN = os.getenv('ADMIN', 'admin')

auth = flask_httpauth.HTTPBasicAuth()

users = {ADMIN: generate_password_hash(PASS)}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    else:
        return False
