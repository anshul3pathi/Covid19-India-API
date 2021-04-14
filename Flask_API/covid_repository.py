from .Scrapper import CovidScrapper
from .database import Database
from .covid_model import CovidModel
from datetime import datetime
import os
from dotenv import load_dotenv

"""This module contains the CovieRepository classs"""

load_dotenv()

FORMAT = '%Y-%m-%d %H:%M:%S.%f'
UPDATE_INTERVAL_IN_MINUTES = int(os.getenv('DATA_UPDATE_INTERVAL_IN_MINUTES'))

class CovidRepository:
    """this class acts as a bridge between data and api endpoint,
    it takes care of all the task related to data and datafetching and
    makes the decesion to fetch new data if data in database is stale"""

    def __init__(self):
        """initialises database object"""
        self.db = Database()

    def __del__(self):
        """disconnects the databse"""
        self.db.close_database()

    def scrape_new_data(self):
        """
        this method scrapes new data using the CovidScrapper class
        :returns: list[dict]
        """
        scrapper = CovidScrapper()
        covid_data = scrapper.get_covid_data()
        scrapper.tear_driver()
        return covid_data

    def get_covid_data(self):
        """
        this method takes the decision whether to fetch new data if data
        in database is stale or to fetch data saved in database
        the databse is the single source of truth
        :return: list[CovidModel]
        """
        if self.is_data_stale():
            data_from_db = self.fetch_data_from_db()
            new_data = self.scrape_new_data()
            self.insert_new_data_into_db(new_data)
            return data_from_db
        else:
            return self.fetch_data_from_db()

    def insert_new_data_into_db(self, state_data):
        """
        inserts new data into the database
        :param: list[dict]
        """
        test = state_data[0]
        print(test['Confirmed'])
        data_to_be_inserted = []
        for state in state_data:
            data = CovidModel(
                state_name=state['state_name'],
                confirmed=state['Confirmed'],
                active=state['Active'],
                recovered=state['Recovered'],
                deceased=state['Deceased'],
                tested=state['Tested'],
                vaccine_doses=state['Vaccine Doses Administered']
            )
            data_to_be_inserted.append(data)
        self.db.delete_old_and_create_new_table()
        self.db.insert_all(data_to_be_inserted)
        self.write_to_should_fetch()

    def fetch_data_from_db(self):
        """
        fetches saved data from the database
        :return: list[CovidModel]
        """
        return self.db.get_all_data()

    def write_to_should_fetch(self):
        """
        writes the time at which new data is fetched to the
        requirements.txt file
        """
        with open("Flask_API/should_fetch.txt", 'w') as file:
            file.write(str(datetime.now()))

    def is_data_stale(self):
        """
        reads the time of last update from requirement.txt file
        returns True if the data in database is older than UPDATE_INTERVAL_IN_MINUTES
        :returns: boolean
        """
        try:
            with open("Flask_API/should_fetch.txt", 'r') as file:
                written_time = file.read()
                print(written_time)
                try:
                    written_time = datetime.strptime(written_time, FORMAT)
                    delta_time = ((datetime.now() - written_time).total_seconds()) / 60
                    print(f"delta_time - {delta_time}")
                    if delta_time >= UPDATE_INTERVAL_IN_MINUTES:
                        return True
                    else:
                        False
                except ValueError:
                    return True
        except FileNotFoundError:
            self.write_to_should_fetch()
            return True

if __name__ == "__main__":
    repo = CovidRepository()
    data = repo.get_covid_data()
    print(data)
    print(f"size of data - {len(data)}")
