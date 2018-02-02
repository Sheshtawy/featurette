from app.ma import ma
from app.FeatureRequests.models import FeatureRequest, ProductArea
from app.Clients.serializers import ClientSchema
from marshmallow import fields
from marshmallow_enum import EnumField
        
class FeatureRequestSchema(ma.ModelSchema):
    client = fields.Nested(ClientSchema)
    product_area = EnumField(ProductArea, by_value=True)
        
    class Meta:
        model = FeatureRequest
