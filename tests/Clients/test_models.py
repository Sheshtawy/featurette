from app.Clients.models import Client

class TestClient(object):

    def test_create(self, db, app, session):
        clientJohn = Client.create(name='client John')
        # db.session.add(john)
        # db.session.commit()
        print(clientJohn)
        assert clientJohn.id == 1
