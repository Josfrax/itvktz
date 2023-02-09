"""
This modules conteins the Shamas or Serializers.
"""

from ma import ma
from marshmallow import fields, Schema, post_load
from models import Institution, Project, User

class InstitutionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Institution
        load_instance = True


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        load_instance = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class ProjectDayLefSchema(Schema):
    name = fields.String(required=True)
    daysleft = fields.Integer(required=True)

    class Meta:
        fields = ('name', 'dayleft')
