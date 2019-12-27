import subprocess
from logzero import logger


def apply_database_migrations():
    try:
        logger.info("Applying migrations...")
        subprocess.run(["flask", "db", "upgrade"])
    except KeyboardInterrupt:
        logger.info("Command canceled")
    except Exception as e:
        logger.info(f"Could not apply migrations. Reason: {str(e)}")
