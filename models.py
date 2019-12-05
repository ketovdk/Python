from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class SuperMen(db.Model):
    __tablename__ = 'mens'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    color = db.Column(db.String(120))
    planet_id=db.Column(db.Integer, ForeignKey('planets.id'))
    planet=relationship('Planet')
    def json(self):
        return {'id': self.id, 'name': self.name, 'color': self.color, 'planet':self.planet.json()}

class Planet(db.Model):
    __tablename__='planets'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    def json(self):
        return {'id': self.id, 'name': self.name}
