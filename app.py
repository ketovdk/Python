from flask import Flask

from models import db, SuperMen, Planet
from routes import api, index

app= Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    planet = Planet(name='crypton')
    db.session.add(planet)
    db.session.commit()
    db.session.add(SuperMen(name = 'Superman', color='blue', planet_id=planet.id))
    db.session.add(SuperMen(name = 'Bizzaro', color = 'red', planet_id=planet.id))
    db.session.commit()

if __name__ == "__main__":
    app.run()
