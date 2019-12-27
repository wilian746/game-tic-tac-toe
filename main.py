from logzero import logger
import settings

from app.services.flask.flask_commands import apply_database_migrations
from app import app

if __name__ == "__main__":
    config = settings.load_config()

    logger.info(f"Server running in mode {config.__name__.lower()}")

    apply_database_migrations()

    logger.info(f"DOCUMENTATION avaliable in http://{config.HOST}:{config.PORT}/docs")

    app.run(host=config.HOST, port=int(config.PORT), debug=False)
