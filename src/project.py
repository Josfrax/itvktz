"""
This module contains functions for handling requests from projects.
"""

from flask import request
from models import Project
from schemas import ProjectSchema

project = Project()
project_schema = ProjectSchema()

def get_all():
    return project_schema.dump(project.fetch_all(), many=True), 200