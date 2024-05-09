#!/usr/bin/python

from flask import Flask
from flask import request
from flask_restx import Api, Resource, Namespace
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
