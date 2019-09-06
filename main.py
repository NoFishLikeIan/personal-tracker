from loguru import logger

from src.server import app, app_config

if __name__ == '__main__':
    port = app_config['port']
    host = app_config['host']
    logger.info(f'Running on {host}:{port}')
    app.run(**app_config)
