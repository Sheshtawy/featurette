from app.ma import ma
from app.Clients.models import Client
from app.FeatureRequests.models import FeatureRequest


class ClientSchema(ma.ModelSchema):
    class Meta:
        model = Client
