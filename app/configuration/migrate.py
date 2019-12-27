from flask_migrate import Migrate


def config_migration(app, db):
    Migrate(app, db)
