from app.Users.models import User
from app.FeatureRequests.models import FeatureRequest
from app.Clients.models import Client
class TestUser(object):

    def test_create(self, db, app, session):
        john = User.create(username='john', email='h@g.com')
        # db.session.add(john)
        # db.session.commit()
        print(john)
        assert john.id == 1
