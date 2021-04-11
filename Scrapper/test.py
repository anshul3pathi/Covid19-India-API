import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / ".env" 
load_dotenv(dotenv_path=env_path)
print(env_path)
print(load_dotenv())

# print(os.environ.get("CHROME_DRIVER_PATH"))
# chrome_options = webdriver.ChromeOptions()
# print(chrome_options.binary_location)
# print("anshul")
# chrome_options.binary_location = ""
# print(chrome_options.binary_location)
# os.getenv()
print(os.getenv('GOOGLE_CHROME_PATH'))
print(os.getenv("DEBUG"))