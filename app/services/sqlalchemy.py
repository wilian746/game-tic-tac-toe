import sqlalchemy
from logzero import logger


def initialize_database(config):
    try:
        logger.info("Creating database...")

        command = "select date('now')"

        engine = sqlalchemy.create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
        connection = engine.connect()
        results_founds = connection.execute(command)
        for _result in results_founds:
            logger.info(f"Result found: {str(_result)}")
        connection.close()
        return connection
    except KeyboardInterrupt:
        logger.info("Command canceled")
    except Exception as e:
        logger.info(f"Could not create database. Reason: {str(e)}")
