from app.services.flask.flask_commands import apply_database_migrations


def configuration_flask_cli(app):
    @app.cli.group()
    def config():
        """Commands with project settings"""

    @config.command("migration")
    def config_apply_migrations():
        """
        Apply database migrations
        """
        apply_database_migrations()


