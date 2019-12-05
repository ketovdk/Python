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
    power_id=db.Column(db.Integer, ForeignKey('powers.id'))
    power=relationship('Power')
    villian_id=db.Column(db.Integer, ForeignKey('villians.id'))
    villian = relationship('Villian')
    def json(self):
        return {'id': self.id, 'name': self.name, 'color': self.color, 'planet':self.planet.json(), 'villian':self.villian.json(), 'power':self.power.json()}

class Planet(db.Model):
    __tablename__='planets'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    def json(self):
        return {'id': self.id, 'name': self.name}

class Villian(db.Model):
    __tablename__='villians'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    power_id=db.Column(db.Integer, ForeignKey('powers.id'))
    power=relationship('Power')
    def json(self):
        return {'id': self.id, 'name': self.name, 'power': self.power.json()}

class Power(db.Model):
    __tablename__='powers'
    id=db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.Integer)
    name=db.Column(db.String(120))
    def json(self):
        return {'id': self.id, 'name': self.name, 'strength':self.strength}
