import enum
from app import db
from app.Mixins import TimeStampMixin


class ProductArea(enum.Enum):
    POLICIES = 'Policies'
    BILLING = 'Billing'
    CLAIMS = 'Claims'
    REPORTS = 'Reports'


class FeatureRequest(TimeStampMixin, db.Model):
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)
    # client = db.Column(db.String, db.ForeignKey('client.name'), nullable=False)
    client_priority = ''
    target_date = db.Column(db.DateTime, nullable=False)
    product_area = db.Column(db.Enum(ProductArea))

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<FeatureRequest title: %r email: %r >' % self.username, self.email
