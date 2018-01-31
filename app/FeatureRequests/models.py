import enum
from app import db
from app.Mixins.CreateMixin import CreateMixin
from app.Mixins.TimeStampMixin import TimestampMixin


class ProductArea(enum.Enum):
    POLICIES = 'Policies'
    BILLING = 'Billing'
    CLAIMS = 'Claims'
    REPORTS = 'Reports'


class FeatureRequest(TimeStampMixin, CreateMixin, db.Model):
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)
    # client = db.Column(db.String, db.ForeignKey('client.name'), nullable=False)
    client_priority = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    target_date = db.Column(db.DateTime, nullable=False)
    product_area = db.Column(db.Enum(ProductArea))

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<FeatureRequest title: %r >' % self.title

    def update_client_priority(self):
        feature_requests = FeatureRequest.query
            .filter(FeatureRequest.client_id=self.client_id)
            .filter_by(FeatureRequest.client_priority >= self.client_priority)

        if(feature_requests is not None):
            for fr in feature_requests:
                fr.client_priority += 1
                db.session.add(fr)

            db.session.commit()
