from flask import Blueprint, jsonify

from models import Power, db

powersApi = Blueprint('powersApi', __name__, url_prefix='/api/powers')

@powersApi.route('/')
def all():
    return jsonify([(lambda power:power.json()) (power) for power in Power.query.all()])

@powersApi.route('/id/<int:id>')
def byId(id):
    power = Power.query.get(id)
    return jsonify(power.json()) if power else ''

@powersApi.route('/name/<string:name>/strength/<int:strength>')
def put(name, strength):
    power = Power(name=name, strength=strength)
    db.session.add(power)
    db.session.commit()
    return jsonify(power.json()) if power else ''
