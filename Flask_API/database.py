import sqlite3
from .covid_model import CovidModel

class Database:
	
	def __init__(self):
		self.conn = sqlite3.connect("./Flask_API/covid_database.db", check_same_thread=False)
		self.cur = self.conn.cursor()
		self.create_table()

	def create_table(self):
		self.cur.execute(
			"CREATE TABLE IF NOT EXISTS covid_data \
		(id INTEGER PRIMARY KEY, state_name TEXT, \
		confirmed INTEGER, active INTEGER, recovered INTEGER, \
		deceased INTEGER, tested INTEGER, vaccine_doses INTEGER)"
		)
		self.conn.commit()
		
	def insert(self, covid_model):
		if isinstance(covid_model, CovidModel):
			self.cur.execute(
				"INSERT INTO covid_data VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)",
				(
					covid_model.state_name,
					covid_model.confirmed,
					covid_model.active,
					covid_model.recovered,
					covid_model.deceased,
					covid_model.tested, 
					covid_model.vaccine_doses 
				)
			)
			self.conn.commit()
		else:
			raise TypeError("covid_model should be of type CovidModel")

	def insert_all(self, covid_models):
		for covid_model in covid_models:
			self.insert(covid_model)

	def get_all_data(self):
		self.cur.execute("SELECT * FROM covid_data")
		data = self.cur.fetchall()
		return self.as_CovidModel_list(data)

	@staticmethod
	def as_CovidModel_list(data_list):
		covid_model_list = []
		for data in data_list:
			model = CovidModel(
				state_name=data[1],
				confirmed=data[2],
				active=data[3],
				recovered=data[4],
				deceased=data[5],
				tested=data[6],
				vaccine_doses=data[7]
			)
			covid_model_list.append(model)
		return covid_model_list
			
	def delete_old_and_create_new_table(self):
		self.cur.execute("DROP TABLE covid_data")
		self.create_table()


if __name__ == "__main__":
    pass
