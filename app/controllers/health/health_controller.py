from datetime import datetime

from logzero import logger

import settings
from app import app


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

    @staticmethod
    def _ping_database() -> str:
        try:
            command = "select date('now')"
            results = app.db.engine.execute(command)
            for _result in results:
                return _result[0]
        except Exception as e:
            logger.error(f"Failed to check sql alchemy: {str(e)}")
            raise Exception(f"Failed to check database")
        finally:
            app.db.close()
