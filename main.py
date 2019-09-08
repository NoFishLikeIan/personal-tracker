from loguru import logger

from src.server import app, app_config
from src.setup import is_production, port

startup_message = f'Running with {"production" if is_production else "developement"} environment, on http://0.0.0.0:{port}'

if __name__ == '__main__':
    logger.info(startup_message)
    app.run(**app_config)
