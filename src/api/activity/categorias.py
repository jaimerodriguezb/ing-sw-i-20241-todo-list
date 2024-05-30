#!/usr/bin/python

from flask import request, jsonify
from flask_restx import Resource, Namespace
from flask_accepts import accepts
from marshmallow import ValidationError

from .schema import CategoriaSchema
from src.domain.transfer_objects import CreateCategoriaTransferObject
from src.application.services.creating_categorias import CreatingCategoriaApplicationService
from ..config import uow, categoria_repo

api = Namespace("categoria", description="Exposes the categories management services.")

@api.route('/')
class CategoriaApi(Resource):

    @accepts(schema=CategoriaSchema, api=api)
    def post(self):
        try:
            # Valida y deserializa el objeto
            categoria_data = request.parsed_obj
            create_categoria_to = CreateCategoriaTransferObject(
                name=categoria_data['cate_name']
            )
            with uow:
                categoria_service = CreatingCategoriaApplicationService(categoria_repo, uow)
                categoria_service.create_categoria(create_categoria_to)
                uow.commit()

            return jsonify(dict(status="Success", message="Category created successfully"))

        except ValidationError as err:
            return jsonify(dict(status="Error", errors=err.messages)), 400

        except Exception as e:
            return jsonify(dict(status="Error", message=str(e))), 500
    def get(self):
        try:
            # Aquí deberías obtener los datos de alguna manera
            # data = obtener_datos()
            data = []
            # Devolver los datos serializados
            return jsonify(data)
        except Exception as e:
            return jsonify(dict(status="Error", message=str(e))), 500
@api.route('/<int:cate_id>')
class CategoriaApi(Resource):

    @accepts(schema=CategoriaSchema, api=api)
    def put(self, cate_id):
        try:
            categoria_data = request.parsed_obj
            update_categoria_to = UpdateCategoriaTransferObject(
                id=cate_id,
                name=categoria_data['cate_name']
            )
            with uow:
                categoria_service = UpdatingCategoriaApplicationService(categoria_repo, uow)
                categoria_service.update_categoria(update_categoria_to)
                uow.commit()

            return jsonify(dict(status="Success", message="Category updated successfully"))

        except ValidationError as err:
            return jsonify(dict(status="Error", errors=err.messages)), 400

        except Exception as e:
            return jsonify(dict(status="Error", message=str(e))), 500


