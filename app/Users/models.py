from app import db
from app.Mixins import TimeStampMixin


class User(TimeStampMixin, db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<User username: %r email: %r >' % self.username, self.email
