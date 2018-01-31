from app import db
from app.Mixins import TimeStampMixin


class Client(TimeStampMixin, db.Model):
    name = db.Columnt(db.String(120), nullable=False, unique=True)

    id = db.Column(db.Integer, primary_key=True)

    feature_requests = db.relationship('FeatureRequest',
                                       backref=db.backref(
                                           'client', lazy='select'),
                                       uselist=False
                                       )

    def __repr__(self):
        return '<Client name: %r id: %r >' % self.name, self.id
