from app.Users.models import User
class TestUser(object):

    def test_create(self, db, app, session):
        john = User.create(username='john', email='h@g.com')
        print(john)
        assert john.id == 1
