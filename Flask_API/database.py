from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 

def init_database(app):
	with app.app_context():
		db.init_app(app)
		# db.drop_all()
		db.create_all()
