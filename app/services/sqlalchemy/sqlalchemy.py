from settings import load_config

import sqlalchemy
from logzero import logger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
_Session = sessionmaker()


def __execute_command(connection, command):
    results_founds = connection.execute(command)
    for _result in results_founds:
        if str(_result[0]) is not None and str(_result[0]) != "":
            break
        else:
            raise Exception("ERROR -> Database life")


def _create_engine(config):
    return sqlalchemy.create_engine(config.SQLALCHEMY_DATABASE_URI, echo=config.DEBUG)


def get_database_connection(config):
    engine = _create_engine(config)
    connection = engine.connect()
    return connection


def initialize_database(config):
    try:
        logger.info("Creating database...")

        command = "select date('now');"
        connection = get_database_connection(config)
        __execute_command(connection, command)
        connection.close()
    except KeyboardInterrupt:
        logger.info("Command canceled")
    except Exception as e:
        logger.info(f"Could not create database. Reason: {str(e)}")


def get_session():
    engine = _create_engine(load_config())
    Base.metadata.create_all(engine)
    _Session = sessionmaker(bind=engine)
    return _Session()
