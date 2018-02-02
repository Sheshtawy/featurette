from flask.views import MethodView
from flask import abort, request, Response
from app.db import db
from app.ma import ma
from app.FeatureRequests.models import FeatureRequest, ProductArea
from app.FeatureRequests.serializers import FeatureRequestSchema
import json

class FeatureRequestsViews(MethodView):
    serializer = FeatureRequestSchema()
    many_serializer = FeatureRequestSchema(many=True)

    def get(self, id=None):
        if id is None:
            return self._list()
        instance = FeatureRequest.query.get_or_404(id)
        return self.serializer.jsonify(instance)

    def post(self):
        if not request.is_json:
            return Response(json.dumps(
                {
                    'status': 400,
                    'error': 'Accepts only json content type',
                }), 200)
    
        instance = self.serializer.make_instance(request.get_json())
        instance.product_area = ProductArea(instance.product_area)
        db.session.add(instance)
        db.session.commit()
        return self.serializer.jsonify(instance)

    def put(self, id):
        if id is None:
            return Response(json.dumps(
                {
                    'status': 400,
                    'error': 'Feature request id is missing',
                }), 200)
                
        if not request.is_json:
            return Response(json.dumps(
                {
                    'status': 400,
                    'error': 'Accepts only json content type',
                }), 200)
        
        instance = FeatureRequest.query.get(id)
        if instance is None:
            return Response(json.dumps(
                {
                    'status': 404,
                    'error': 'Instance is not found',
                }), 200)

        instance.title = request.get_json().get('title', instance.title)
        instance.description = request.get_json().get('description', instance.description)
        if instance.client_priority != request.get_json().get('client_priority'):
            instance.client_priority = request.get_json().get('client_priority', instance.client_priority)
            FeatureRequest.update_client_priority(instance)
        instance.target_date = request.get_json().get('target_date', instance.target_date)
        instance.product_area = request.get_json().get('product_area', instance.product_area)
        instance.product_area = ProductArea(instance.product_area)
        db.session.commit()
        return self.serializer.jsonify(instance)

    def delete(self, id):
        if id is None:
            return Response(json.dumps(
                {
                    'status': 400,
                    'error': 'Feature request id is missing',
                }), 200)
        
        instance = FeatureRequest.query.get(id)
        if instance is None:
            return Response(json.dumps(
                {
                    'status': 404,
                    'error': 'Instance is not found',
                }), 200)

        db.session.delete(instance)
        db.session.commit()
        return Response({
                'status': '202',
                'message': 'Feature request deleted successfully '
            }, 202)

    def _list(self):
        query_result = FeatureRequest.query.all()
        if not query_result:
            return Response(json.dumps(
                {
                    'status': 404,
                    'error': 'No feature requests found',
                }), 200)
        return self.many_serializer.jsonify(query_result)
