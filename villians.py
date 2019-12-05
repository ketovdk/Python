from flask import Blueprint, jsonify, request

from models import Villian, db

villiansApi = Blueprint('villiansApi', __name__, url_prefix='/api/villians')

@villiansApi.route('/')
def all():
    return jsonify([(lambda villian:villian.json()) (villian) for villian in Villian.query.all()])

@villiansApi.route('/id/<int:id>')
def byId(id):
    villian = Villian.query.get(id)
    return jsonify(villian.json()) if villian else ''

@villiansApi.route('/name/<string:name>/power_id/<int:power_id>')
def put(name, power_id):
    villian = Villian(name=name, power_id=power_id)
    db.session.add(villian)
    db.session.commit()
    return jsonify(villian.json()) if villian else ''
