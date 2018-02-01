from flask import Flask
from flask import _app_ctx_stack
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask_sqlalchemy import BaseQuery
from app.db import db
from app.ma import ma

# def create_app(name, config, config_type):
#     """
#     App factory
#     :param name: Application name
#     :param config: Application config
#     :param config_type: is the config param object, mapping, pyfile, envvar or json
#     """

DbSession = db.create_scoped_session()
# DbSession = scoped_session(sessionmaker(), scopefunc=_app_ctx_stack.__ident_func__)


def create_app(name_handler, config_object):
    """
    Application factory

    :param name_handler: name of the application.
    :param config_object: the configuration object.
    """
    app = Flask(name_handler)
    app.config.from_object(config_object)
    app.engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

    # global DbSession
    # # BaseQuery class provides some additional methods like
    # # first_or_404() or get_or_404() -- borrowed from
    # # mitsuhiko's Flask-SQLAlchemy
    # DbSession.configure(bind=app.engine, query_cls=BaseQuery)
    db.init_app(app)
    ma.init_app(app)

    @app.teardown_appcontext
    def teardown(exception=None):
        global DbSession
        if DbSession:
            DbSession.remove()

    return app
