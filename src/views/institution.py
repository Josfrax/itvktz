"""
This module contains functions for handling requests from institutes.
"""

from flask import request
from models import Institution
from schemas import InstitutionSchema, InstWithProjSchema

institution = Institution()
institution_schema = InstitutionSchema()
inst_proj_schema = InstWithProjSchema()

def create():
    institution_req_json = request.get_json()
    institution_data = institution_schema.load(institution_req_json)
    institution.create(institution_data)
    return institution_schema.dump(institution_data), 201

def get_all():
    return institution_schema.dump(institution.fetch(), many=True), 200

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
    return {'success': f'Item not found for id: {id}'}, 404

def delete(id:int):
    institution_data = institution.fetch_by_id(id)
    if institution_data:
        institution.delete(id)
        return {'success': 'Item deleted successfully'}, 200
    return {'error': f'Item not found for id: {id}'}, 404

def get_by_id(id:int):
    institution_data = institution.fetch_by_id(id)
    if institution_data:
        print(institution_data)
        return inst_proj_schema.dump(institution_data, many=True), 200
    return {'error': f'Item not found for id: {id}'}, 404
    


