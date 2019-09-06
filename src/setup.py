import os


def set_logger_path():
    log_path = os.getenv('LOG_PATH')

    if log_path is None:
        if not os.path.isdir('logs/'):
            os.makedirs('logs/')
        log_path = 'logs/'
    return log_path
