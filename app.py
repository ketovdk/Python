from flask import Flask

from models import db, SuperMen, Planet, Power, Villian
from routes import index
from planets import planetsApi
from villians import villiansApi
from powers import powersApi
from superMens import superMensApi

app= Flask(__name__)
app.register_blueprint(planetsApi)
app.register_blueprint(villiansApi)
app.register_blueprint(superMensApi)
app.register_blueprint(powersApi)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    planet = Planet(name='crypton')
    laserPower = Power(name='laser eyes', strength=10)
    inteligencePower=Power(name='super smart', strength = 5)
    db.session.add(inteligencePower)
    db.session.add(laserPower)
    db.session.add(planet)
    db.session.commit()
    villian=Villian(name='Lex luthor', power_id= inteligencePower.id)
    db.session.add(villian)
    db.session.commit()
    db.session.add(SuperMen(name = 'Superman', color='blue', planet_id=planet.id, power_id=laserPower.id, villian_id=villian.id))
    db.session.add(SuperMen(name = 'Bizzaro', color = 'red', planet_id=planet.id, power_id=laserPower.id, villian_id=villian.id))
    db.session.commit()

if __name__ == "__main__":
    app.run()
