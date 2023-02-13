"""
This modules conteins the Shamas or Serializers.
"""

from ma import ma
from marshmallow import fields
from models import Institution, Project, User

""" Institution Schemas """
class InstitutionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Institution
        load_instance = True


""" Project Schemas """
class ProjectSchema(ma.Schema):
    class Meta:
        model = Project
        fields = ('id', 'name', 'date_start', 'date_close', 'inst_id', 'user_id')


class ProjectDayLefSchema(ma.Schema):
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
    projects = ma.List(fields.Nested(ProjectSchema, exclude=('user_id',)))


class InstWithProjSchema(ma.Schema): 
    id = fields.Integer()
    name = fields.String()
    projects = ma.List(fields.Nested(ProjectSchema, exclude=('inst_id',)))

    