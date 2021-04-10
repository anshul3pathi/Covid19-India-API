from Flask_API import db, CovidModel, CovidResource, create_app
from flask_restful import Api
from Scrapper import CovidScrapper

app = create_app()
api = Api(app)

api.add_resource(CovidResource, "/statecoviddata")


# scrapper = CovidScrapper()
# state_data = scrapper.get_covid_data()

# final_data_list = []

# for state in state_data:
# 	data = CovidModel(
# 			state_name=state["state_name"],
# 			confirmed=state["Confirmed"],
# 			active=state["Active"],
# 			recovered=state["Recovered"],
# 			deceased=state["Deceased"],
# 			tested=state["Tested"],
# 			vaccine_doses=state["Vaccine Doses Administered"]
# 		)
# 	final_data_list.append(data)

# with app.app_context():
# 	# db.drop_all()
# 	db.session.add_all(final_data_list)
# 	db.session.commit()



if __name__ == '__main__':
	app.run(debug=True)