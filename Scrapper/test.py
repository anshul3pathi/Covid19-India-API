from scrapper import CovidScrapper

scrapper = CovidScrapper()
print(scrapper.get_covid_data())
scrapper.tear_driver()
