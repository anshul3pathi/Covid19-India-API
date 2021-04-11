import os 
from selenium import webdriver

print(os.environ.get("GOOGLE_CHROME_PATH"))
chrome_options = webdriver.ChromeOptions()
print(chrome_options.binary_location)
print("anshul")
chrome_options.binary_location = ""
print(chrome_options.binary_location)
