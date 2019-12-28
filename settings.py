import os

from dotenv import load_dotenv

load_dotenv(verbose=True)
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ENVIRONMENT = "development"
    NAME_SERVICE_RUN = "flask"

    # Flask
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 9000))
    if str.lower(os.getenv("DEBUG")) == "true":
        DEBUG = True
    else:
        DEBUG = False

    # Restplus
    SWAGGER_TITLE = "Tic-Tac-Toe Documentation"
    SWAGGER_DESCRIPTION = "This game aims to be the practical test of the company DTI Digital. Your goal is a tic-tac-toe game with some scenarios see more in Readme.md"
    SWAGGER_UI_DOC_EXPANSION = None
    RESTPLUS_VALIDATE = False
    RESTPLUS_MASK_SWAGGER = False
    ERROR_INCLUDE_MESSAGE = False
    ERROR_404_HELP = False

    # Sql Alchemy
    SQLALCHEMY_DATABASE_NAME = os.getenv("SQLALCHEMY_DATABASE_NAME", "tic-tac-toe")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", f"sqlite:///{SQLALCHEMY_DATABASE_NAME}.db")


class Development(Config):
    SWAGGER_VISIBLE = os.getenv("SWAGGER_VISIBLE", True)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", True)
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", True)
    TESTING = os.getenv("TESTING", False)
    FLASK_ENV = os.getenv("FLASK_ENV", "development")



def load_config():
    envs = {
        "development": Development,
    }

    return envs.get(Config.ENVIRONMENT, Development)
