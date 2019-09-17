from datetime import datetime


def get_today():
    today = datetime.now()
    return f'{today.year}_{today.month}_{today.day}'
