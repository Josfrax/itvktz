"""
This conteins the models or entities of DB.
"""

from db import db
from typing import List
from utils import Daysleft

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


class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    date_start = db.Column(db.Date())
    date_close = db.Column(db.Date())

    # Functions to model
    def fetch_all(self) -> List['Project']:
        return db.session.query(Project).all()
    

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(9))
    name = db.Column(db.String(80))
    l_name = db.Column(db.String(80))
    birthdate = db.Column(db.Date())
    position = db.Column(db.String(80))
    age = db.Column(db.Integer)

    # Functions to model
    def fetch_all(self) -> List['User']:
        return db.session.query(User).all()