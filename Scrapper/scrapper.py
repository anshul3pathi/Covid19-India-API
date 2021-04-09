import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class CovidScrapper:
	"""
	this class deals with scraping data
	from covid19.org and converts that data into 
	JSON Array format.
	:public methods - get_covid_data
	"""

	PATH = "C:\\Program Files (x86)\\chromedriver.exe"  # path to chrome driver
	URL = "https://www.covid19india.org/"  # website url

	def __init__(self):
		"""
		intializes the selenium webdriver
		"""
		self.__driver = self.__get_driver()

	def __get_driver(self):
		"""
		creates the selenium webdriver with arguments
		:return: driver = selenium chrome webdriver
		"""
		options = Options()
		options.add_argument("--headless")
		options.add_argument("--window-size=1920x1080")
		driver = webdriver.Chrome(options=options, executable_path=CovidScrapper.PATH)
		return driver

	def __clean_data(self, data):
		"""
		removes ',', "Cr", "L", "K", '.' from 
		the numbers of all states and returns the values as 
		integers
		:param: data = list[str]
		:return: new_data = list[int]
		"""
		zeroes_in_cr = 7
		zeroes_in_lakh = 5
		zeroes_in_thousand = 3
		new_data = []

		for item in data:
			if "Cr" in item:
				trailing_zeres = 0
				if '.' in item:
					dot_index = item.index('.') + 1
					trailing_zeres = zeroes_in_cr - len(item.replace("Cr", '')[dot_index:])
					new_data.append(int(item.replace('.', '').replace("Cr", '') + trailing_zeres * '0'))
				else:
					new_data.append(int(item.replace("Cr", '') + zeroes_in_cr * '0'))
			elif 'L' in item:
				if '.' in item:
					dot_index = item.index('.') + 1
					trailing_zeres = zeroes_in_lakh - len(item.replace('.', '').replace('L', '')[dot_index:])
					new_data.append(int(item.replace(".", '').replace("L", "") + trailing_zeres * '0'))
				else:
					new_data.append(int(item.replace("L", '') + zeroes_in_lakh * '0'))
			elif 'K' in item:
				if '.' in item:
					dot_index = item.index('.') + 1
					trailing_zeres = zeroes_in_thousand - len(item.replace('.', '').replace('K', '')[dot_index:])
					new_data.append(int(item.replace(".", '').replace("K", "") + trailing_zeres * '0'))
				else:
					new_data.append(int(item.replace("K", '') + zeroes_in_lakh * '0'))
			else:
				# new_data.append(int(item.replace(',', '')))
				new_data.append(int(item.replace(',', '').replace('-', '0')))

		return new_data

	def __scrape_data(self, table_container):
		"""
		scrape the relevant data from the given data container 
		:param: table_container = selenium web element 
		:return: headings = list[str] list of all the attributes 
		:return: state_names = list[str] list of all the state names
		:return: figures = list[int] list of all the relevant data
		"""
		cell_heading = table_container.find_elements_by_class_name("cell.heading")
		
		headings = []
		state_names = []
		figures = []

		for heading in cell_heading:
			headings.append(heading.text)

		headings = headings[1:]

		state_name_rows = table_container.find_elements_by_class_name("state-name.fadeInUp")

		for row in state_name_rows:
			state_names.append(row.text)

		figures_tag = table_container.find_elements_by_class_name("total")

		for total in figures_tag:
			figures.append(total.text)

		figures = self.__clean_data(figures)

		return headings, state_names, figures

	def __convert_to_JSON_Array(self, headings, state_names, figures):
		"""
		converts the raw data into JSON Array 
		[
			{
				"key1": value1,
				"key2": value2,
			},
		]
		:param: headings = list[str] list of all the attributes 
		:param: state_names = list[str] list of all the state names
		:param: figures: list[int] list of all the relevant data
		:return: json_array = list[dict] list of dict, it is analogous to JSON Array
		"""
		step = len(headings)

		json_array = []

		for i in range(0, len(figures), step):
			state_dict = {}
			state_figures = figures[i: i+step]
			state_dict["state_name"] = state_names[i//step]
			for j in range(0, len(headings)):
				state_dict[headings[j]] = state_figures[j]
			json_array.append(state_dict)

		return json_array

	def get_covid_data(self):
		"""
		retrieves the data in JSON Array format
		and returns it.
		:return: json_array = list[dict] list which is analogous to JSON Array
		"""
		self.__driver.get(CovidScrapper.URL)
		root = WebDriverWait(self.__driver, 10).until(
				EC.presence_of_element_located((By.ID, "root"))
			)

		table_container = WebDriverWait(self.__driver, 10).until(
				EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[5]'))
			)

		headings, state_names, figures = self.__scrape_data(table_container)

		return self.__convert_to_JSON_Array(headings, state_names, figures)

	def tear_driver(self):
		"""
		destroy the selenium chrome webdriver 
		:return: None
		"""
		self.__driver.quit()

if __name__ == "__main__":
	scrapper = CovidScrapper()
	all_data = scrapper.get_covid_data ()
	scrapper.tear_driver()
	print(all_data)
	print(len(all_data))
