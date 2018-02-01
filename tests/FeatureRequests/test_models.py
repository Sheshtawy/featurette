from datetime import datetime

from app.Users.models import User
from app.Clients.models import Client
from app.FeatureRequests.models import FeatureRequest, ProductArea

class TestFeatureRequest(object):

    def test_create(self, app, db, session):
        clientJohn = Client.create(name='client John')
        john = User.create(username='john', email='h@g.com')
        feature = FeatureRequest.create(
            title="some feature",
            description="some description of course",
            client_id=clientJohn.id,
            client_priority=1,
            user_id=john.id,
            target_date=datetime(2018, 2, 10),
            product_area=ProductArea.POLICIES
        )

        assert feature.id == 1

    def test_update_client_priority(self, app, db, session):
        clientJohn = Client.create(name='client John')
        john = User.create(username='john', email='h@g.com')
        feature = FeatureRequest.create(
            title="some feature",
            description="some description of course",
            client_id=clientJohn.id,
            client_priority=1,
            user_id=john.id,
            target_date=datetime(2018, 2, 10),
            product_area=ProductArea.POLICIES
        )

        assert feature.id == 1
        assert feature.client_priority == 1
        another_feature = FeatureRequest.create(
            title="some feature",
            description="some description of course",
            client_id=clientJohn.id,
            client_priority=1,
            user_id=john.id,
            target_date=datetime(2018, 2, 10),
            product_area=ProductArea.POLICIES
        )

        FeatureRequest.update_client_priority(another_feature)
        assert another_feature.id == 2
        assert another_feature.client_priority == 1
        assert feature.client_priority == 2

