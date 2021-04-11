from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 

def init_database(app):
	with app.app_context():
		db.init_app(app)
		# db.drop_all()
		db.create_all()

def delete_all_records(app):
	meta = db.metadata
	for table in reversed(meta.sorted_tables):
		with app.app_context():
			db.session.execute(table.delete())
	with app.app_context():
		db.session.commit()
