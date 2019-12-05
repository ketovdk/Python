from flask import Blueprint, jsonify

from models import SuperMen, db

index = Blueprint('index', __name__, url_prefix='/')
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/mens')
def get_mens():
    return jsonify([(lambda men:men.json()) (men) for men in SuperMen.query.all()])

@api.route('/men/id/<int:id>')
def get_men(id):
    men = SuperMen.query.get(id)
    return jsonify(men.json()) if men else ''

@api.route('/men/name/<string:name>/color/<string:color>')
def put_men(name, color):
    superMen = SuperMen(name=name, color=color)
    db.session.add(superMen)
    db.session.commit()
    return jsonify(superMen.json()) if superMen else ''

@index.route('/')
@index.route('/index')
def get_index():
    return '''
    <html>
    <title>
        supermen rest
    </title>
    <body>
        <h3>API:</h3>
        <a href="./api/mens">Mens</a>
    </body>
    </html>'''
