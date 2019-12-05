from flask import Blueprint, jsonify

from models import SuperMen, db

superMensApi = Blueprint('superMensApi', __name__, url_prefix='/api/superMens')

@superMensApi.route('/')
def all():
    return jsonify([(lambda superMen:superMen.json()) (superMen) for superMen in SuperMen.query.all()])

@superMensApi.route('/id/<int:id>')
def byId(id):
    superMen = SuperMen.query.get(id)
    return jsonify(superMen.json()) if superMen else ''

@superMensApi.route('/men/name/<string:name>/color/<string:color>/planet_id/<int:planet_id>/villian_id/<int:villian_id>/power_id/<int:power_id>')
def put(name, color, planet_id, villian_id, power_id):
    superMen = SuperMen(name=name, color=color, power_id=power_id, villian_id=villian_id, planet_id=planet_id)
    db.session.add(superMen)
    db.session.commit()
    return jsonify(superMen.json()) if superMen else ''
