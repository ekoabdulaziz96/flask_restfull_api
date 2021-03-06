from flask import Flask
from settings.extensions import (db, migrate)
from models import (users, books)


def create_app(config_object="settings.env"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_shellcontext(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    return None

def register_shellcontext(app):
    """Register shell context objects."""

    shell_context = {
        'db': db,
        "Users": users.Users,
        "Books": books.Books
    }

    app.shell_context_processor(shell_context)
