"""
This modules conteins the Shamas or Serializers.
"""

from ma import ma
from marshmallow import fields
from models import Institution, Project, User

""" Institution Schemas """
class InstitutionSchema(ma.Schema):
    class Meta:
        model = Institution
        fields = ('id', 'name', 'description', 'address', 'date_created'
        )


""" Project Schemas """
class ProjectSchema(ma.Schema):
    class Meta:
        model = Project
        fields = ('id', 'name', 'date_start', 'date_close', 'user_id')


class ProjectDayLefSchema(ma.Schema):
    name = fields.String()
    daysleft = fields.Integer()

    class Meta:
        fields = ('name', 'dayleft')


""" User Schemas """
class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'rut', 'name', 'l_name', 'birthdate', 'position', 'age')


class UserWithProjectSchema(ma.Schema): 
    id = fields.Integer()
    f_name = fields.String()
    Project = fields.Nested(ProjectSchema, exclude=('user_id',))

