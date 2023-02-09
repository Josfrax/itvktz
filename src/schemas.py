"""
This modules conteins the Shamas or Serializers.
"""

from ma import ma
from models import Institution

class InstitutionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Institution
        load_instance = True