from sqlalchemy import event
from models import

def update_client_priority(self):
        import pdb; pdb.set_trace()
        feature_requests = FeatureRequest.query.filter_by(client_id=self.client_id).filter_by(FeatureRequest.client_priority >= self.client_priority)

        if(feature_requests is not None):
            for fr in feature_requests:
                fr.client_priority += 1
                db.session.add(fr)

            db.session.commit()

event.listen(db.session, 'before_commit', FeatureRequest.update_client_priority)
