from datetime import datetime

from logzero import logger

import settings
from app.services.sqlalchemy.sqlalchemy import get_database_connection


class HealthController:
    def __init__(self):
        self._config = settings.load_config()

    def verify(self):
        try:
            self._ping_database()

            data = {
                "environment": self._config.ENVIRONMENT,
                "datetime_server": datetime.now().isoformat(),
            }

            return data
        except Exception as e:
            raise Exception(e)

    def _ping_database(self) -> str:
        try:
            command = "select date('now');"
            connection = get_database_connection(self._config)
            results = connection.execute(command)
            for _result in results:
                return _result
            connection.close()
        except Exception as e:
            logger.error(f"Failed to check sql alchemy: {str(e)}")
            raise Exception(f"Failed to check database")
