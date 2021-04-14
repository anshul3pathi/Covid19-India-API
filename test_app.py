import requests

BASE_URL = "http://127.0.0.1:5000/"

DEPLOYED_BASE_URL = "https://covid19indiaorgapi.herokuapp.com/"

response = requests.get(DEPLOYED_BASE_URL + "statecoviddata")
array = response.json()
print(array)
print(len(array))