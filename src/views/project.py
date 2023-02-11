"""
This module contains functions for handling requests from projects.
"""

from flask import request
from models import Project
from schemas import ProjectSchema, ProjectDayLefSchema
from utils import Daysleft

project = Project()
project_schema = ProjectSchema()
project_dl_schema = ProjectDayLefSchema()

def get_all():
    return project_schema.dump(project.fetch_all(), many=True), 200

def day_left():
    projects = project.fetch_all()
    pdl = list() # Projects with days left
    for _project in projects:
        days:int = Daysleft(_project.date_close)
        pdl.append({'name': _project.name, 'dayleft': days})
    return project_dl_schema.dump(pdl, many=True), 200
