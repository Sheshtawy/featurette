from flask import Flask
from flask import _app_ctx_stack, url_for, render_template
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask_sqlalchemy import BaseQuery
from app.db import db
from app.ma import ma

from app.FeatureRequests.views import FeatureRequestsViews
from app.Users.models import User
from app.Clients.models import Client
from app.FeatureRequests.models import FeatureRequest
# def create_app(name, config, config_type):
#     """
#     App factory
#     :param name: Application name
#     :param config: Application config
#     :param config_type: is the config param object, mapping, pyfile, envvar or json
#     """

DbSession = db.create_scoped_session()
# DbSession = scoped_session(sessionmaker(), scopefunc=_app_ctx_stack.__ident_func__)

def register_api(app, view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])


def create_app(name_handler, config_object):
    """
    Application factory

    :param name_handler: name of the application.
    :param config_object: the configuration object.
    """
    app = Flask(name_handler)
    app.config.from_object(config_object)
    app.engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

    register_api(app, FeatureRequestsViews, 'feature_request_api', '/feature_requests/', 'id')
    
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    
    @app.route('/')
    def root():
        return render_template('index.html')

    @app.teardown_appcontext
    def teardown(exception=None):
        global DbSession
        if DbSession:
            DbSession.remove()

    return app
