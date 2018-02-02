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
        pass

    def delete(self, id):
        pass

    def _list(self):
        query_result=FeatureRequest.query.all()
        if query_result is None or len(query_result) == 0:
            abort(404)
        return self.many_serializer.jsonify(query_result)
