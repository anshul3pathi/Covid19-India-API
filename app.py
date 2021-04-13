from flask_restful import Api
from flask import Flask
from Flask_API import CovidResource

app = Flask(__name__)
api = Api(app)
api.add_resource(CovidResource, "/statecoviddata")

if __name__ == '__main__':
	app.run(debug=False, use_debugger=False)