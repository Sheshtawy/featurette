from app.FeatureRequests.serializers import FeatureRequestSchema
from app.Clients.models import Client
from app.Users.models import User
from app.FeatureRequests.models import FeatureRequest
from datetime import datetime
import json

class TestFeatureRequestsViewsGetById(object):
    def test_not_found(self, app, db, session):
        client = app.test_client()
        response = client.get('/feature_requests/10000000')
        assert response.status_code == 404
    
    def test_get_by_id(self, app, db, session, feature_request):
        id = feature_request.id
        client = app.test_client()
        response = client.get('/feature_requests/{}'.format(id))
        schema = FeatureRequestSchema()
        assert response.status_code == 200
        assert schema.dump(feature_request).data == json.loads(response.get_data())


class TestFeatureRequestsViewsGet(object):
    def test_get_not_found(self, app, db, session):
        client = app.test_client()
        response = client.get('/feature_requests/')
        assert response.status_code == 404

    def test_get(self, app, db, session, feature_request):
        client = app.test_client()
        response = client.get('/feature_requests/')
        schema = FeatureRequestSchema()
        data = json.loads(response.get_data())        

        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0] == schema.dump(feature_request).data

    

class TestFeatureRequestsViewsPost(object):
    
    def test_post(self, app, db, session):
        client = app.test_client()
        client_john = Client.create(name='client John')
        john = User.create(username='john', email='h@g.com')
        response = client.post('/feature_requests/', 
            data=json.dumps({
                'title':'a feature request',
                'description':'a description',
                'client_id':client_john.id,
                'client_priority':1,
                'user_id':john.id,
                'target_date':str(datetime.utcnow()),
                'product_area':'Policies'}
            ),
            headers={'Content-Type':'application/json'}
        )

        data = json.loads(response.get_data())
        instance = FeatureRequest.query.get(data['id'])
        
        assert response.status_code == 200
        assert instance.title == data['title']
        assert instance.client_priority == data['client_priority']
        assert instance.product_area.value == data['product_area']
    
    def test_post_non_json(self, app, db, session):
        client = app.test_client()
        response = client.post('/feature_requests/', 
            data={
                'title':'a feature request',
                'description':'a description',
                'client_id':1,
                'client_priority':1,
                'user_id':1,
                'target_date':str(datetime.utcnow()),
                'product_area':'Policies'
            })
        
        assert response.status_code == 200
        data = json.loads(response.get_data())
        assert data['status'] == 400
        

    def test_put(self, app, db, session):
        pass

    def test_delete(self, app, db, session):
        pass
