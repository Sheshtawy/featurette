import enum
from app.db import db
from app.Mixins.CreateMixin import CreateMixin
from app.Mixins.TimeStampMixin import TimeStampMixin

from sqlalchemy import event


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
    
    @classmethod
    def update_client_priority(cls, instance):
        feature_requests = cls.query \
            .filter_by(client_id=instance.client_id) \
            .filter(cls.client_priority >= instance.client_priority) \
            .filter(cls.id != instance.id)
        
        if(feature_requests.all() is not None):
            for fr in feature_requests:
                fr.client_priority += 1
                import pdb; pdb.set_trace()
                db.session.add(fr)
            
            db.session.commit()
