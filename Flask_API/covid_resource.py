from flask_restful import Resource, marshal_with, fields
from .covid_repository import CovidRepository

repository = CovidRepository()


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
        """
        this method provides the api with the get endpoint
        """
        result = repository.get_covid_data()
        return result


if __name__ == '__main__':
    print(repository.get_covid_data())