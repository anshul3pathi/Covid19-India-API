from flask_restful import Resource, marshal_with, fields
from .covid_model import CovidModel


RESOURCE_FIELDS = {
	'state_name': fields.String,
	'confirmed': fields.Integer,
	'active': fields.Integer,
	'recovered': fields.Integer,
	'deceased': fields.Integer,
	'tested': fields.Integer,
	'vaccine_doses': fields.Integer,
}

class CovidResource(Resource):
	@marshal_with(RESOURCE_FIELDS)
	def get(self):
		result = CovidModel.query.all()
		return result