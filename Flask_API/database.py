import sqlite3
from .covid_model import CovidModel

"""This module contains the Database class which is used to interface
with the sqlite3 database.
"""


class Database:
    """
    This class is used to interface with the sqlite3 databse.
    """
    def __init__(self):
        """
        initialses the connection and creates covid_database table if
        it doesn't already exist
        """
        self.conn = sqlite3.connect(
            "./Flask_API/covid_database.db",
            check_same_thread=False
        )
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        this function creates the covid_database if it already doesn't exist
        """
        self.cur.execute(
            
        )
        self.conn.commit()

    def insert(self, covid_model):
        """
        this function inserts a single entry into the database
        :param: covid_model = CovidModel
        """
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
        """
        this method inserts a list of entries into the databse
        :param: covid_models = list[CovidModel]
        """
        for covid_model in covid_models:
            self.insert(covid_model)

    def get_all_data(self):
        """
        fetches data from covid_database
        return: list[CovidModel]
        """
        self.cur.execute("SELECT * FROM covid_data")
        data = self.cur.fetchall()
        return self.as_CovidModel_list(data)

    @staticmethod
    def as_CovidModel_list(data_list):
        """
        this static method converts a list of database objects in a list
        of CovidModel objects
        :param: list[database.object]
        return: list[CovidModel]
        """
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
        """
        this method drops the existing covid_data table and creates a new on
        in it's place
        """
        self.cur.execute("DROP TABLE covid_data")
        self.create_table()

    def close_database(self):
        """
        closes the database connection
        """
        self.conn.close()


if __name__ == "__main__":
    pass
