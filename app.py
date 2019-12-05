from flask import Flask

from models import db, SuperMen
from routes import api, index

app= Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.add(SuperMen(name = 'Superman', color='blue'))
    db.session.add(SuperMen(name = 'Bizzaro', color = 'red'))
    db.session.commit()


if __name__ == "__main__":
    app.run()
