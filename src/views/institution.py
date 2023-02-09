"""
This module contains functions for handling requests from institutes.
"""

from flask import request
from models import Institution
from schemas import InstitutionSchema

institution = Institution()
institution_schema = InstitutionSchema()

def create():
    institution_req_json = request.get_json()
    institution_data = institution_schema.load(institution_req_json)
    institution.create(institution_data)
    return institution_schema.dump(institution_data),201

def get_all():
    return institution_schema.dump(institution.fetch_all(), many=True), 200

def get(id:int):
    institution_data = institution.fetch_by_id(id)
    if institution_data:
        return institution_schema.dump(institution_data), 200
    return {'message': f'Item not found for id: {id}'}, 404

def update(id:int):
    institution_data = institution.fetch_by_id(id)
    institution_req_json = request.get_json()
    if institution_data:
        institution_data.name = institution_req_json['name']
        institution_data.description = institution_req_json['description']
        institution_data.address = institution_req_json['address']
        institution_data.date_created = institution_req_json['date_created']
        institution.update(institution_data)
        return institution_schema.dump(institution_data), 200
    return {'message': f'Item not found for id: {id}'}, 404

def delete(id:int):
    institution_data = institution.fetch_by_id(id)
    if institution_data:
        institution.delete(id)
        return {'message': 'Item deleted successfully'}, 200
    return {'message': f'Item not found for id: {id}'}, 404


