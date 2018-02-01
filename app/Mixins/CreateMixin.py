from app.db import db
class CreateMixin(object):
    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit() 
        return obj
