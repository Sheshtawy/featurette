from flask import current_app
from app.db import db
from app.Mixins.CreateMixin import CreateMixin
from app.Mixins.TimeStampMixin import TimeStampMixin


class User(TimeStampMixin, CreateMixin, db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    id = db.Column(db.Integer, primary_key=True)

    feature_requests = db.relationship(
        'FeatureRequest', backref='creator', lazy='select')

    def __repr__(self):
        return '<User username: {} email: {} >'.format(self.username, self.email)
