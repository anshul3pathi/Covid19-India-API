from Flask_API.database import db, delete_all_records, init_database
from Flask_API.covid_19.covid_model import CovidModel
from Flask_API.covid_19.covid_resource import CovidResource
from flask import Flask

def create_app():
	from Flask_API.database import init_database
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	init_database(app)
	return app
