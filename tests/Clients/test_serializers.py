from app.Clients.serializers import ClientSchema
from app.Clients.models import Client


class TestClientSchema(object):
    def test_init(self, app, db, session):
        johnClient = Client.create(name='john the client')
        client_schema = ClientSchema()
        result = client_schema.dump(johnClient).data

        assert result['id'] == johnClient.id
        assert result['name'] == johnClient.name
