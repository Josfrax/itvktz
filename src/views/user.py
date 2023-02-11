"""
This module contains functions for handling requests from projects.
"""

from models import User
from schemas import UserSchema, UserWithProjectSchema

user = User()
schema = UserSchema()
uwp_schema = UserWithProjectSchema()

def get_all() -> list['User']:
    return schema.dump(user.fetch_all(), many=True), 200

def get_by_rut(rut:str) -> list:
    return uwp_schema.dump(user.fetch_by_rut(rut), many=True), 
    