"""
This module contains functions for handling requests from projects.
"""

from flask import request
from models import User
from schemas import UserSchema

user = User()
user_schema = UserSchema()

def get_all():
    return user_schema.dump(user.fetch_all(), many=True), 200