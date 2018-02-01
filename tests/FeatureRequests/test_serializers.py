from datetime import datetime
from app.FeatureRequests.serializers import FeatureRequestSchema
from app.Users.models import User
from app.Clients.models import Client
from app.FeatureRequests.models import FeatureRequest, ProductArea


class TestFeatureRequestSchema(object):
    """
    sanity check test
    """

    def test_init(self, app, db, session):
        client_john = Client.create(name='client John')
        john = User.create(username='john', email='h@g.com')
        feature = FeatureRequest.create(
            title="some feature",
            description="some description of course",
            client_id=client_john.id,
            client_priority=1,
            user_id=john.id,
            target_date=datetime(2018, 2, 10),
            product_area=ProductArea.POLICIES
        )

        feature_request_schema = FeatureRequestSchema()
        result = feature_request_schema.dump(feature).data

        assert result['id'] == feature.id
        assert result['client']['id'] == client_john.id
