from flask import Flask
from utils import db
from flask_migrate import Migrate

from routes.api import api

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

MIGRATE = Migrate(app, db)

db.init_app(app)

with app.app_context():
    db.create_all()
    
app.register_blueprint(api, url_prefix = '/api')

    
@app.route("/")
def hello():
    return "Working"

app.run(host='0.0.0.0')