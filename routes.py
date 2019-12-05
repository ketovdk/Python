from flask import Blueprint


index = Blueprint('index', __name__, url_prefix='/')

@index.route('/')
@index.route('/index')
def get_index():
    return '''
    <html>
    <title>
        supermen rest
    </title>
    <body>
        <h3>Api:</h3>
        <a href="./api/superMens">Mens</a>
        <a href="./api/villians">Villians</a>
        <a href="./api/powers">Powers</a>
        <a href="./api/planets">Planets</a>        
    </body>
    </html>'''
