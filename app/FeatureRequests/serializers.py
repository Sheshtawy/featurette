from app.ma import ma
from app.FeatureRequests.models import FeatureRequest
from app.Clients.serializers import ClientSchema
from marshmallow import fields


class FeatureRequestSchema(ma.ModelSchema):
    client = fields.Nested(ClientSchema)

    class Meta:
        model = FeatureRequest
