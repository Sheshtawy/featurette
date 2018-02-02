from app.FeatureRequests.serializers import FeatureRequestSchema
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

    

class TestFeatureRequestsViews(object):
    
    def test_post(self, app, db, session):
        pass

    def test_put(self, app, db, session):
        pass

    def test_delete(self, app, db, session):
        pass
