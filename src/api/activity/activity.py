#!/usr/bin/python

from flask import request
from flask_restx import Resource, Namespace
from flask_accepts import accepts
from flask import jsonify

from .schema import ActivitySchema

from src.domain.transfer_objects import CreateActivityTransferObject
from src.application.services.creating_activity import CreatingActivityApplicationService
from ..config import uow, activity_repo, user_repo
   
api = Namespace("activity", description="Exposes the activities management services.")

@api.route('/')
class ActivityApi(Resource):

    @accepts(schema=ActivitySchema, api=api)
    def post(self):
        create_activity_to = CreateActivityTransferObject(
            name = request.parsed_obj['name'],
            hour = request.parsed_obj['hour'],
            date = request.parsed_obj['date'],
            user_id = request.parsed_obj['user_id']
            )
        with uow:
            activity_service = CreatingActivityApplicationService(activity_repo, user_repo, uow)
            activity_service.create_activity(create_activity_to)

        return jsonify(dict(status="Success"))
    
    def get(self):
        with uow:
            activities = activity_repo.all()
            activities_schema = ActivitySchema(many=True)
            result = activities_schema.dump(activities)
            
        return jsonify(result)


@api.route('/<int:id>')
class ActivityDetailApi(Resource):

    def get(self, id):
        with uow:
            activity = activity_repo.get(id)
            if not activity:
                return jsonify(dict(status="Not Found", message="Activity not found")), 404
            activity_schema = ActivitySchema()
            result = activity_schema.dump(activity)
        return jsonify(result)
