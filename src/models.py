"""
This conteins the models or entities of DB.
"""

from db import db
from typing import List


class Institution(db.Model):
    __tablename__ = "institution"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    address = db.Column(db.String(80))
    date_created = db.Column(db.Date())

    # Functions to model
    def create(self, institution:dict) -> None:
        db.session.add(institution)
        db.session.commit()

    def fetch_by_id(self, _id:int) -> 'Institution':
        return db.session.query(Institution).filter_by(id=_id).first()

    def fetch_all(self) -> List['Institution']:
        return db.session.query(Institution).all()

    def update(self, institution:dict) -> None:
        db.session.merge(institution)
        db.session.commit()

    def delete(self, _id:int) -> None:
        institution= db.session.query(Institution).filter_by(id=_id).first()
        db.session.delete(institution)
        db.session.commit()