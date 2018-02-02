from datetime import datetime
import pytest
from app import create_app, DbSession
from sqlalchemy.ext.declarative import declarative_base
import settings
from app.db import db as _db
from app.Users.models import User
from app.Clients.models import Client
from app.FeatureRequests.models import FeatureRequest, ProductArea

@pytest.yield_fixture(scope='session')
def app():
    """
    Creates a new Flask application for a test duration.
    Uses application factory `create_app`.
    """
    _app = create_app("testingsession", config_object=settings)
    _app.connection = _app.engine.connect()

    DbSession.configure(bind=_app.connection)

    yield _app

    _app.connection.close()



@pytest.yield_fixture(scope='function')
def db(app):
    _db.init_app(app)
    with app.app_context():
        _db.drop_all()
        _db.create_all()
        print('cleaned the db for a new test case')

        yield _db
        _db.drop_all()


@pytest.yield_fixture(scope="function")
def session(app):
    """
    Creates a new database session (with working transaction)
    for a test duration.
    """
    app.transaction = app.connection.begin()

    ctx = app.app_context()
    ctx.push()

    session = DbSession()

    yield session

    app.transaction.close()
    session.close()
    ctx.pop()


@pytest.fixture(scope='function')
def feature_request(app, db, session):
    clientJohn = Client.create(name='client John')
    john = User.create(username='john', email='h@g.com')
    return FeatureRequest.create(
        title="some feature",
        description="some description of course",
        client_id=clientJohn.id,
        client_priority=1,
        user_id=john.id,
        target_date=datetime(2018, 2, 10),
        product_area=ProductArea.POLICIES
    )
