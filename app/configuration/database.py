from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def config_database(app):
    db.init_app(app)
    app.db = db
    app.sqlAlchemy = db

