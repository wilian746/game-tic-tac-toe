import time

from logzero import logger

import settings
from app import app
import random

if __name__ == "__main__":
    config = settings.load_config()

    logger.info(f"Server running in mode {config.__name__.lower()}")

    time.sleep(1)

    logger.info(f"DOCUMENTATION avaliable in http://{config.HOST}:{config.PORT}/docs")

    print(random.choice(["X", "O"]))

    app.run(host=config.HOST, port=int(config.PORT), debug=False)
