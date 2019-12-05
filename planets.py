from flask import Blueprint, jsonify

from models import Planet, db

planetsApi = Blueprint('planetsApi', __name__, url_prefix='/api/planets')

@planetsApi.route('/')
def all():
    return jsonify([(lambda planet:planet.json()) (planet) for planet in Planet.query.all()])

@planetsApi.route('/id/<int:id>')
def byId(id):
    planet = Planet.query.get(id)
    return jsonify(planet.json()) if planet else ''

@planetsApi.route('/name/<string:name>')
def put(name):
    planet = Planet(name=name)
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.json()) if planet else ''
