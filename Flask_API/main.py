from flask import Flask 
from flask_restful import Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)

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

db.drop_all()
db.create_all()

resource_fields = {
	'state_name': fields.String,
	'confirmed': fields.Integer,
	'active': fields.Integer,
	'recovered': fields.Integer,
	'deceased': fields.Integer,
	'tested': fields.Integer,
	'vaccine_doses': fields.Integer,
}

fake_data = CovidModel(
		state_name="imaginaryState",
		confirmed=10000,
		active=1092,
		recovered=9989,
		deceased=69,
		tested=2000000,
		vaccine_doses=200000000
	)

fake_data2 = CovidModel(
		state_name="imaginaryState2",
		confirmed=10000,
		active=1092,
		recovered=9989,
		deceased=69,
		tested=2000000,
		vaccine_doses=200000000
	)

fake_data3 = CovidModel(
		state_name="imaginaryState3",
		confirmed=10000,
		active=1092,
		recovered=9989,
		deceased=69,
		tested=2000000,
		vaccine_doses=200000000
	)

# db.session.add(fake_data)
# db.session.add(fake_data2)
db.session.add_all([fake_data, fake_data2, fake_data3])
db.session.commit()

class CovidData(Resource):
	@marshal_with(resource_fields)
	def get(self):
		result = CovidModel.query.all()
		return result

api.add_resource(CovidData, "/statecoviddata")

if __name__ == "__main__":
	app.run(debug=True)