from Flask_API import db, CovidModel, CovidResource
from Flask_API import create_app, delete_all_records
from flask_restful import Api
from Scrapper import CovidScrapper
from datetime import datetime

FORMAT = '%Y-%m-%d %H:%M:%S.%f'

app = create_app()
api = Api(app)

def write_to_should_fetch():
	with open("should_fetch.txt", 'w') as file:
		file.write(str(datetime.now()))

def should_fetch():
	try:
		with open("should_fetch.txt", 'r') as file:
			written_time = file.read()
			try:
				written_time = datetime.strptime(written_time, FORMAT)
				delta_time = (datetime.now() - written_time).total_seconds() / 60
				if delta_time >= 2:
					return True
				else:
					False
			except ValueError:
				return True
	except FileNotFoundError:
		db.create_all()
		with open("should_fetch.txt", 'w') as file:
			file.write(str(datetime.now()))
		return True

if should_fetch():

	with app.app_context():
		db.drop_all()
		db.create_all()

	scrapper = CovidScrapper()
	state_data = scrapper.get_covid_data()
	scrapper.tear_driver()

	final_data_list = []

	for state in state_data:
		data = CovidModel(
				state_name=state["state_name"],
				confirmed=state["Confirmed"],
				active=state["Active"],
				recovered=state["Recovered"],
				deceased=state["Deceased"],
				tested=state["Tested"],
				vaccine_doses=state["Vaccine Doses Administered"]
			)
		final_data_list.append(data)

	write_to_should_fetch()
	
	with app.app_context():
		# db.drop_all()
		db.session.add_all(final_data_list)
		db.session.commit()

api.add_resource(CovidResource, "/statecoviddata")

if __name__ == '__main__':
	app.run(debug=False, use_debugger=False)