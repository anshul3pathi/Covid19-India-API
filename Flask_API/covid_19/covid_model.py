from Flask_API.database import db

class CovidModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	state_name = db.Column(db.String(50), nullable=False)
	confirmed = db.Column(db.Integer, nullable=False)
	active = db.Column(db.Integer, nullable=False)
	recovered = db.Column(db.Integer, nullable=False)
	deceased = db.Column(db.Integer, nullable=False)
	tested = db.Column(db.Integer, nullable=False)
	vaccine_doses = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"State Name = {state_name},\
			Confirmed = {confirmed},\
			Active = {active}, \
			Recovered = {recovered},\
			Deceased = {deceased},\
			Tested = {tested},\
			Vaccine Dosses Administered = {vaccine_doses}."